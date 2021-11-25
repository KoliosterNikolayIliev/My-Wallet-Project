import React, {Fragment, useState} from "react";
import {updateUser} from "../../utils/account";
import {useAuth0} from "@auth0/auth0-react";
import {Link, Redirect} from "react-router-dom";

const AddBinanceSource = () => {
  const {user, isAuthenticated, isLoading, getAccessTokenSilently} =
    useAuth0();

  const [key, setKey] = useState(null);
  const [secret, setSecret] = useState(null);

  const saveChanges = async () => {
    let data = {};
    const token = await getAccessTokenSilently();
    data["binance_key"] = key;
    data["binance_secret"] = secret;
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
    <Fragment>
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
      <button onClick={saveChanges}>
        <Link to={"/dashboard"}>Save</Link>
      </button>
    </Fragment>
  )
}

export default AddBinanceSource
