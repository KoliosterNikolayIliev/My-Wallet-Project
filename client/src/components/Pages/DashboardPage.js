import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import ProfileButton from "../Buttons/ProfileButton";

import {
  getAssets,
  getTransactions,
  getAllRecentTransactions,
} from "../../utils/portfolio";
import { getUser } from "../../utils/account";

import GroupsContainerComponent from "../Other/GroupsContainerComponent";
import RecentTransactionsContainerComponent from "../Other/RecentTransactionsContainerComponent";

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";
import Header from "../Other/HeaderComponent";
import SubHeader from "../Other/SubHeaderComponent";
import ChartComponent from "../Other/ChartComponent";
import AddNewSourceComponent from "../Other/AddNewSourceComponent";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [groups, setGroups] = useState({});
  const [transactions, setTransactions] = useState({});
  const [recentTransactions, setRecentTransactions] = useState([]);
  const [base, setBase] = useState("");
  const [total, setTotal] = useState(0);

  const [loading, setLoading] = useState(true);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  useEffect(() => {
    const getUserData = async () => {
      if (!window.sessionStorage.getItem("base")) {
        const token = await getAccessTokenSilently();
        const response = await getUser(token);
        setBase(response.base_currency);
      } else {
        setBase(window.sessionStorage.getItem("base"));
      }
    };
    getUserData();
  }, []);

  const getData = async () => {
    setLoading(true);
    if (
      window.sessionStorage.getItem("total") &&
      window.sessionStorage.getItem("assets") &&
      window.sessionStorage.getItem("recentTransactions")
    ) {
      setTotal(JSON.parse(window.sessionStorage.getItem("total")));
      setGroups(JSON.parse(window.sessionStorage.getItem("assets")));
      setRecentTransactions(
        JSON.parse(window.sessionStorage.getItem("recentTransactions"))
      );
    } else {
      const token = await getAccessTokenSilently();
      // fetch all of the data in parllel using Promise.all
      await Promise.all([
        (async () => {
          const assets = await getAssets(token);
          const total = assets.total;
          delete assets.total;

          window.sessionStorage.setItem("total", JSON.stringify(total));
          window.sessionStorage.setItem("assets", JSON.stringify(assets));
          setTotal(total);
          setGroups(assets);
        })(),
        (async () => {
          const transactions = await getRecentTransactions(token);
          window.sessionStorage.setItem(
            "recentTransactions",
            JSON.stringify(transactions)
          );
          setRecentTransactions(transactions);
        })(),
      ]);
    }

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
    const token = await getAccessTokenSilently();
    const transactions = await getAllRecentTransactions(token);
    return transactions.content;
  };

  // fetch all data on first render
  useEffect(() => {
    getData();
  }, []);

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading || loading) {
    return Loader();
  }

  // Redirect the user to the landing page if the user is not logged in
  if (!isAuthenticated) {
    return <Redirect to={"/"} />;
  }

  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        <SubHeader user={user} />
        <ChartComponent />
        <ProfileButton />
        <div style={{ margin: "3% 0" }}>
          <p style={{ display: "inline", paddingRight: "20px", fontSize: "x-large", fontWeight: "bold" }}>Accounts</p>
          <AddNewSourceComponent/>
        </div>
        <div className="dashboard-container">
          <GroupsContainerComponent
            baseSymbol={base}
            data={groups}
            total={total}
            getTransactionsFunc={getAccountTransactions}
          />

          <div className="transactions data-source recent-transactions">
            <p className="recent-transactions-header">Recent Transactions</p>
            <RecentTransactionsContainerComponent data={recentTransactions} />
          </div>
        </div>
      </div>
    )
  );
};

export default DashboardPage;
