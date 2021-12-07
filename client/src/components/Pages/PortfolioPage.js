import React, {useState, useEffect} from "react";
import {useAuth0} from "@auth0/auth0-react";
import {Redirect} from "react-router";

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";
import {useRecoilState} from "recoil";
import {getUser} from "../../utils/account";
import Header from "../Other/HeaderComponent";
import {balanceHistoryAtom, baseAtom} from "../../recoil";
import {getHistoricalBalances} from "../../utils/portfolio";

// Dashboard page to be filled in with user account data
const PortfolioPage = () => {


  const [balanceHistory, setBalanceHistory] = useRecoilState(
    balanceHistoryAtom
  );
  const [base, setBase] = useRecoilState(baseAtom);

  const [isLoading, setIsLoading] = useState(true);

  // const [colors, setColors] = useState({
  //   bank: { "background-color": "#ffa04370", color: "#FFA043" },
  //   crypto: { "background-color": "#00a5ff70", color: "#00A5FF" },
  // });

  const {isAuthenticated, user, loading, getAccessTokenSilently} = useAuth0();

  const getBase = async () => {
    if (!window.sessionStorage.getItem("base")) {
      const token = await getAccessTokenSilently();
      const response = await getUser(token);
      setBase(response.base_currency);
    } else {
      setBase(window.sessionStorage.getItem("base"));
    }
  };

  const HistoricalBalances = async () => {
    const token = await getAccessTokenSilently();
    const balanceHistory = await getHistoricalBalances(token);

    window.sessionStorage.setItem(
      "balanceHistory",
      JSON.stringify(balanceHistory.content)
    );
    setBalanceHistory(balanceHistory.content);
  };

  useEffect(() => {
    if (balanceHistory === "" || !balanceHistory) {
      HistoricalBalances();
    }
    if (base === "" || !base) {
      getBase();
    }
    setIsLoading(false);
  }, []);

  if (isLoading || balanceHistory === "" || !balanceHistory) {
    return Loader();
  }

  const currentBalances = balanceHistory.balances[balanceHistory.balances.length-1]
  const currentSourceBalances = currentBalances.source_balances_history
  const currentTotalBalance = currentBalances.balance
  console.log(currentTotalBalance)
  console.log(currentSourceBalances)
  // for (let entry of balanceHistory.balances){
  //   console.log(JSON.stringify(entry))
  // }
  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        <div className="transactions-table">
          <div className="headings">
            <p>Sources</p>
            <p>+</p>
            <p>%PORTFOLIO</p>
            <p>VALUE-1M</p>
            <p>LATEST VALUE</p>
            <p>PERFORMANCE</p>
          </div>
          {JSON.stringify(balanceHistory)}
        </div>
      </div>
    )
  );
};

export default PortfolioPage;
