import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

// This component is used to display the logout button. When clicked, the user gets logged o
const LogOutButton = () => {
  const { logout, isAuthenticated } = useAuth0();

  return (
    isAuthenticated && (
      <button
        className="LogOutButton"
        onClick={() => logout({ returnTo: window.location.origin })}
      >
        Log Out
      </button>
    )
  );
};

export default LogOutButton;
