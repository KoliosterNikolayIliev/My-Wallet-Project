import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import LogOutButton from "./LogOutButton";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

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
        <h2>Hi, {user.name}, this is the dashboard</h2>
        <span>{user.birthdate},{user.email},{user.gender}</span>
        <LogOutButton></LogOutButton>
      </div>
    )
  );
};

export default DashboardPage;
