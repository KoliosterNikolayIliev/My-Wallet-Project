import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import LogOutButton from "../Buttons/LogOutButton";

import { getAssets, getTransactions } from "../../utils/portfolio";

import BalancesContainerComponent from "../Other/BalancesContainerComponent";
import HoldingsContainerComponent from "../Other/HoldingsContainerComponent";
import TransactionsContainerComponent from "../Other/TransactionsContainerComponent";

import "../../styles/dashboard.css";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [balances, setBalances] = useState({});
  const [holdings, setHoldings] = useState({});
  const [transactions, setTransactions] = useState({});

  const [loading, setLoading] = useState(false);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  const getData = async () => {
    setLoading(true);
    const token = await getAccessTokenSilently();
    const assetsData = await getAssets(token);
    const transactionsData = await getTransactions(token);

    setBalances(assetsData.balances);
    setHoldings(assetsData.holdings);
    setTransactions(transactionsData);

    setLoading(false);
  };

  useEffect(() => {
    getData();
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
      <div className="main">
        <h2>Hi, {user.name}, this is the dashboard</h2>
        <LogOutButton />

        <div className="dashboard-container">
          <div className="container">
            <h1>Balances</h1>
            <BalancesContainerComponent data={balances} />
          </div>

          <div className="container">
            <h1>Holdings</h1>
            <HoldingsContainerComponent data={holdings} />
          </div>

          <div className="container">
            <h1>Transactions</h1>
            <TransactionsContainerComponent data={transactions} />
          </div>
        </div>
      </div>
    )
  );
};

export default DashboardPage;
