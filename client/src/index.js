import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Auth0Provider } from "@auth0/auth0-react";

// Configure Auth0
const authDomain = process.env.REACT_APP_AUTH0_DOMAIN;
const authClientId = process.env.REACT_APP_AUTH0_CLIENT_ID;
// unable to use audience from .env
// const authAudience = process.env.REACT_APP_AUTH0_AUDIENCE;


ReactDOM.render(
  <Auth0Provider
    domain={authDomain}
    clientId={authClientId}
    redirectUri={window.location.origin}
    audience="https://dev-kbl8py41.us.auth0.com/api/v2/"
    scope="profile email"
  >
    <App />
  </Auth0Provider>,
  document.getElementById("root")
);
