import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import LogOutButton from "../Buttons/LogOutButton";
import ProfileButton from "../Buttons/ProfileButton";

import {
  getAssets,
  getTransactions,
  getAllRecentTransactions,
} from "../../utils/portfolio";
import { getUser } from "../../utils/account";

import GroupsContainerComponent from "../Other/GroupsContainerComponent";
import TransactionsContainerComponent from "../Other/TransactionsContainerComponent";

import "../../styles/dashboard.css";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [groups, setGroups] = useState({});
  const [transactions, setTransactions] = useState({});
  const [base, setBase] = useState("");

  const [loading, setLoading] = useState(false);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  useEffect(() => {
    const getBase = async () => {
      const token = await getAccessTokenSilently();
      const response = await getUser(token);
      setBase(response.base_currency);
    };
    getBase();
  }, []);

  const getData = async () => {
    setLoading(true);
    const token = await getAccessTokenSilently();

    // fetch all of the data in parllel using Promise.all
    await Promise.all([
      (async () => {
        const assets = await getAssets(token);
        setGroups(assets);
      })(),
    ]);

    setLoading(false);
  };

  const getAccountTransactions = async (provider, account) => {
    setLoading(true);
    const token = await getAccessTokenSilently();
    const transactions = await getTransactions(token, provider, account);
    setTransactions({ transactions });
    setLoading(false);
  };

  const getRecentTransactions = async () => {
    setLoading(true);
    const token = await getAccessTokenSilently();
    const transactions = await getAllRecentTransactions(token);
    console.log(transactions);
    setLoading(false);
  };

  // fetch all data on first render
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
        <ProfileButton />
        <button onClick={() => getRecentTransactions()}>
          Recent transactions
        </button>

        <div className="dashboard-container">
          <div className="container">
            <h1>Groups</h1>
            <GroupsContainerComponent
              baseSymbol={base}
              data={groups}
              getTransactionsFunc={getAccountTransactions}
            />
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
