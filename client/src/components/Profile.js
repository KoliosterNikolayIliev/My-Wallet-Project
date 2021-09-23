import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

// Profile component to display user information. Purely for demonstration purposes. Not intended for use in the app.
const Profile = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    isAuthenticated && (
      <div>
        <h2>{user.name}</h2>
        <p>{user.email}</p>
      </div>
    )
  );
};

export default Profile;
