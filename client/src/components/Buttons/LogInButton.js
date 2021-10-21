import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

// This component is used to display the login button. When clicked, it redirects the user to the Auth0 login page.
const LogInButton = () => {
  const { loginWithRedirect, isAuthenticated } = useAuth0();

  return (
    !isAuthenticated && (
      <button className="LogInButton" onClick={() => loginWithRedirect()}>
        Log In
      </button>
    )
  );
};

export default LogInButton;
