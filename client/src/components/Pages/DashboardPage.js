import React, {useState, useEffect} from "react";
import {useAuth0} from "@auth0/auth0-react";
import {Redirect} from "react-router";

import LogOutButton from "../Buttons/LogOutButton";
import ProfileButton from "../Buttons/ProfileButton";

import {getAssets, getTransactions} from "../../utils/portfolio";
import {getUser} from "../../utils/account";

import GroupsContainerComponent from "../Other/GroupsContainerComponent";
import TransactionsContainerComponent from "../Other/TransactionsContainerComponent";

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";
import Header from "../Other/HeaderComponent";
import SubHeader from "../Other/SubHeaderComponent";
import ChartComponent from "../Other/ChartComponent";

// Dashboard page to be filled in with user account data
const DashboardPage = () => {
  const [groups, setGroups] = useState({});
  const [transactions, setTransactions] = useState({});
  const [base, setBase] = useState("");

  const [loading, setLoading] = useState(true);

  const {user, isAuthenticated, isLoading, getAccessTokenSilently} =
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
    setTransactions({transactions});
    setLoading(false);
  };
  // fetch all data on first render
  useEffect(() => {
    getData();
  }, []);

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading || loading) {
    return Loader()
  }

  // Redirect the user to the landing page if the user is not logged in
  if (!isAuthenticated) {
    return <Redirect to={"/"}/>;
  }

  return (
    isAuthenticated && (
      <div className="main">
        <Header/>
        {SubHeader(user)}
        <ChartComponent/>
        {/*<LogOutButton/>*/}
        {/*<ProfileButton/>*/}
        <div style={{margin:"3% 0"}}>
          <p style={{display:"inline",paddingRight:"20px"}}>Accounts</p>
          <a href="#">+ Add new Source</a>
        </div>
        <div className="dashboard-container">

          <GroupsContainerComponent
            baseSymbol={base}
            data={groups}
            getTransactionsFunc={getAccountTransactions}
          />

          <div className="data-source">
            <h1>Transactions</h1>
            <TransactionsContainerComponent data={transactions}/>
          </div>
        </div>
      </div>
    )
  );
};

export default DashboardPage;
