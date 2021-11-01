import React, { useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import { Link } from "react-router-dom";

import { updateUser } from "../../utils/account";

// Profile component to display user information.
const Profile = () => {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();
  const [provider, setProvider] = useState(null);
  const [key, setKey] = useState(null);
  const [secret, setSecret] = useState(null);

  const saveChanges = async (provider) => {
    let data = {};
    const token = await getAccessTokenSilently();

    if (provider === "Binance") {
      data["binance_key"] = key;
      data["binance_secret"] = secret;
    }

    updateUser(token, data);
  };

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading) {
    return <div>Loading ...</div>;
  }

  // Redirect the user to the landing page if the user is not logged in
  if (!isAuthenticated) {
    return <Redirect to={"/"} />;
  }

  return (
    isAuthenticated && (
      <div>
        <h2>Hi, {user.name}, this is the profile page</h2>
        <ul>
          <li onClick={(e) => setProvider(e.target.innerText)}>Binance</li>
          <li onClick={(e) => setProvider(e.target.innerText)}>Coinbase</li>
          <li onClick={(e) => setProvider(e.target.innerText)}>Yodlee</li>
          <li onClick={(e) => setProvider(e.target.innerText)}>Nordigen</li>
        </ul>

        {!provider && <p>Ello</p>}

        {provider === "Binance" && (
          <form>
            <label>API Key</label>
            <input
              type={"text"}
              onChange={(e) => setKey(e.target.value)}
              placeholder={"API Key goes here"}
            />
            <label>API Secret</label>
            <input
              type={"text"}
              onChange={(e) => setSecret(e.target.value)}
              placeholder={"API Secret goes here"}
            />
          </form>
        )}

        <button onClick={() => saveChanges(provider)}>
          <Link to={"/dashboard"}>Save Changes</Link>
        </button>
      </div>
    )
  );
};

export default Profile;
