import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import LogOutButton from "../Buttons/LogOutButton";
import { Redirect } from "react-router";

// Profile component to display user information.
const Profile = () => {
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
        <h2>Hi, {user.name}, this is the profile page</h2>
        <LogOutButton />
      </div>
    )
  );
};

export default Profile;
