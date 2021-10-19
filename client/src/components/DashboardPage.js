import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import LogOutButton from "./LogOutButton";
import getBalances from "../utils/portfolio";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [balances, setBalances] = useState({});
  const [loading, setLoading] = useState(false);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  const getBalanceData = async () => {
    setLoading(true);
    const token = await getAccessTokenSilently();
    const data = await getBalances(token);
    setBalances(data);
    setLoading(false);
  };

  useEffect(() => {
    getBalanceData();
  }, []);

  const renderBalances = (providers) => {
    Object.values(providers).forEach((provider) => {
      if (provider["status"] === "success") {
        Object.values(provider["content"]).forEach((balance) => {
          console.log(balance);
        });
      }
    });
  };

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading || loading) {
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

        <h1>Balances</h1>
        {/* <button onClick={getBalanceData}>Get balances</button> */}
        <button onClick={() => renderBalances(balances)}>
          Render balances
        </button>

        <LogOutButton />
      </div>
    )
  );
};

export default DashboardPage;
