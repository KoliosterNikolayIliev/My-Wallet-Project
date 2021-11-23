import React, { useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import { Link } from "react-router-dom";

import { getAccessToken, updateUser } from "../../utils/account";
// import { countries, generateNordigenToken } from "../../utils/nordigen";
import { CountriesDropDownList } from "../Other/CountriesDropDownList";
import AssetsDropDownList from "../Other/AssetsDropDownList";
import BaseCurrencyDropDownList from "../Other/BaseCurrencyDropDownList";

// Profile component to display user information.
const Profile = () => {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();
  const [provider, setProvider] = useState(null);
  const [menu, setMenu] = useState(null);
  const [key, setKey] = useState(null);
  const [secret, setSecret] = useState(null);

  const selectProvider = (e) => {
    if (provider) {
      e.target.parentElement.childNodes.forEach((node) => {
        node.classList.remove("active");
      });
    }
    e.target.classList.add("active");
    setProvider(e.target.innerText);
  };

  const saveChanges = async (provider) => {
    let data = {};
    const token = await getAccessTokenSilently();

    if (provider === "Binance") {
      data["binance_key"] = key;
      data["binance_secret"] = secret;
    } else if (provider === "Coinbase") {
      data["coinbase_api_key"] = key;
      data["coinbase_api_secret"] = secret;
    }

    updateUser(token, data);
  };

  const addYodleeSource = async () => {
    const auth0Token = await getAccessTokenSilently();
    const yodleeToken = await getAccessToken(auth0Token);
    window.fastlink.open(
      {
        fastLinkURL:
          "https://development.node.yodlee.uk/authenticate/UKPre-Prod-203/?channelAppName=ukpreprod",
        accessToken: yodleeToken,
        params: {
          userExperienceFlow: "Aggregation",
        },
        onSuccess: (data) => {
          console.log(data);
        },
        onError: (error) => {
          console.log(error);
        },
      },
      "container-fastlink"
    );
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
          <li onClick={(e) => setMenu(e.target.innerText)}>Accounts</li>
          <li onClick={(e) => setMenu(e.target.innerText)}>Settings</li>
        </ul>

        {menu === "Accounts" && (
          <div>
            <ul>
              <li onClick={(e) => selectProvider(e)}>Binance</li>
              <li onClick={(e) => selectProvider(e)}>Coinbase</li>
              <li onClick={(e) => selectProvider(e)}>Yodlee</li>
              <li onClick={(e) => selectProvider(e)}>Nordigen</li>
              <li onClick={(e) => selectProvider(e)}>Custom Assets</li>
            </ul>

            {!provider && <p>Select a provider on the right</p>}

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

            {provider === "Coinbase" && (
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

            {provider === "Yodlee" && (
              <div id="container-fastlink">
                <button onClick={() => addYodleeSource()}>Add source</button>
              </div>
            )}

            {provider === "Nordigen" && (
              <div>
                <CountriesDropDownList />
              </div>
            )}

            {provider === "Custom Assets" && (
              <div>
                <AssetsDropDownList />
              </div>
            )}
          </div>
        )}

        {menu === "Settings" && (
          <div>
            <BaseCurrencyDropDownList
              provider={{provider}}
              saveChanges={{saveChanges}}
            />
          </div>
        )}

        {!menu && <p>Select a menu on the left</p>}

        <button onClick={() => saveChanges(provider)}>
          <Link to={"/dashboard"}>Save Changes</Link>
        </button>
      </div>
    )
  );
};

export default Profile;
