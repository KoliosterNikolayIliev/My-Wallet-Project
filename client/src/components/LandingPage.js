import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import LogInButton from "./LogInButton";

// Landing page to explain our product. Includes a button to log in.
const LandingPage = () => {
  const { isLoading } = useAuth0();

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    <>
      <LogInButton />
      <h2>This is the landing page</h2>
    </>
  );
};

export default LandingPage;
