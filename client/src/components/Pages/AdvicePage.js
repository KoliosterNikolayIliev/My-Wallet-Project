import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";

// Dashboard page to be filled in with user account data
const AdvicePage = () => {
  const { isAuthenticated, user, loading } = useAuth0();
  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (loading) {
    return Loader();
  }

  return (
    isAuthenticated && (
      <div>
        <h2>This is the advice page</h2>
      </div>
    )
  );
};

export default AdvicePage;
