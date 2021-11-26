import React, {useState} from "react";
import {updateUser} from "../../utils/account";
import {useAuth0} from "@auth0/auth0-react";
import {Link, Redirect} from "react-router-dom";

const AddCryptoSource = (selected) => {
  const {user, isAuthenticated, isLoading, getAccessTokenSilently} =
    useAuth0();

  const [key, setKey] = useState(null);
  const [secret, setSecret] = useState(null);

  const saveChanges = async () => {
    let data = {};
    const token = await getAccessTokenSilently();
    if (selected === "binance") {
      data["binance_key"] = key;
      data["binance_secret"] = secret;
    } else if (selected === "coinbase") {
      data["coinbase_api_key"] = key;
      data["coinbase_api_secret"] = secret;
    }
    updateUser(token, data);
    window.sessionStorage.clear();
    window.location.reload()
  }

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  if (!isAuthenticated) {
    return <Redirect to={"/"}/>;
  }

  return (
    <div>
      <label>API Key</label>
      <input
        type={"text"}
        onChange={(e) => setKey(e.target.value)}
        placeholder={"API Key goes here"}
        required={true}
      />
      <label>API Secret</label>
      <input
        type={"text"}
        onChange={(e) => setSecret(e.target.value)}
        placeholder={"API Secret goes here"}
        required={true}
      />
      <button onClick={saveChanges}>Save</button>
    </div>
  )
}

export default AddCryptoSource
