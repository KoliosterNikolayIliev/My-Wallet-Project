import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import LogOutButton from "../Buttons/LogOutButton";
import getAssets from "../../utils/portfolio";

import BalancesContainerComponent from "../Other/BalancesContainerComponent";
import HoldingsContainerComponent from "../Other/HoldingsContainerComponent";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [balances, setBalances] = useState({});
  const [holdings, setHoldings] = useState({});

  const [loading, setLoading] = useState(false);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  const getAssetsData = async () => {
    setLoading(true);
    const token = await getAccessTokenSilently();
    const data = await getAssets(token);

    setBalances(data.balances);
    setHoldings(data.holdings);

    setLoading(false);
  };

  useEffect(() => {
    getAssetsData();
  }, []);

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

        <div>
          <h1>Balances</h1>
          <BalancesContainerComponent data={balances} />
        </div>

        <div>
          <h1>Holdings</h1>
          <HoldingsContainerComponent data={holdings} />
        </div>

        <LogOutButton />
      </div>
    )
  );
};

export default DashboardPage;
