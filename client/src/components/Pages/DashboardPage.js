import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";

import { atom, useRecoilState } from "recoil";

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
import {
  recentTransactionsAtom,
  baseAtom,
  balanceHistoryAtom,
} from "../../recoil";

// Dashboard page to be filled in with user account data
export async function getTokenWithErrorHandling(getAccessTokenSilently,loginWithRedirect){
  let token;
  try {
    token = await getAccessTokenSilently();
  } catch (e) {
    if (e.error === 'login_required') {
      loginWithRedirect();
    }
    if (e.error === 'consent_required') {
      loginWithRedirect();
    }
    throw e;
  }
  return token
}

const DashboardPage = () => {
  const [groups, setGroups] = useState({});
  const [transactions, setTransactions] = useState({});
  const [recentTransactions, setRecentTransactions] = useRecoilState(
    recentTransactionsAtom
  );
  const [balanceHistory, setBalanceHistory] =
    useRecoilState(balanceHistoryAtom);
  const [base, setBase] = useRecoilState(baseAtom);
  const [total, setTotal] = useState(0);

  const [loading, setLoading] = useState(true);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently,loginWithRedirect } =
    useAuth0();

  useEffect(() => {
    const getUserData = async () => {
      if (!window.sessionStorage.getItem("base")) {

        const token = await getTokenWithErrorHandling(getAccessTokenSilently,loginWithRedirect);
        console.log(token);
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
      window.sessionStorage.getItem("recentTransactions") &&
      window.sessionStorage.getItem("balanceHistory")
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
          const cached_history = assets.balance_history;

          delete assets.total;
          delete assets.balance_history;

          window.sessionStorage.setItem("total", JSON.stringify(total));
          window.sessionStorage.setItem("assets", JSON.stringify(assets));
          window.sessionStorage.setItem(
            "balanceHistory",
            JSON.stringify(cached_history)
          );
          setTotal(total);
          setBalanceHistory(cached_history);
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
  const history = balanceHistory.balances.map((item) => item.balance)
  
  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        <SubHeader user={user} />
        {balanceHistory !== "" && (
          <ChartComponent total={total} base={base} history={history} />
        )}
        <div style={{paddingTop:'3%', paddingBottom:'3%'}}>
          <p
            style={{ display: "inline", paddingRight: "20px" }}
            className="add-source-font"
          >
            Accounts
          </p>
          <AddNewSourceComponent />
        </div>
        <div className="dashboard-container" style={Object.entries(groups).length===0?{display:'none'}:{display:'flex'}}>
          <GroupsContainerComponent
            baseSymbol={base}
            data={groups}
            total={total}
            user={user}
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
