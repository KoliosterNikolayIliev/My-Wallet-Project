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
import {getAssets, getHistoricalBalances} from "../../utils/portfolio";
import ChartComponent from "../Other/ChartComponent";

// Dashboard page to be filled in with user account data
const PortfolioPage = () => {


  const [balanceHistory, setBalanceHistory] = useRecoilState(
    balanceHistoryAtom
  );
  const [base, setBase] = useRecoilState(baseAtom);

  const [isLoading, setIsLoading] = useState(true);


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
    const assets = await getAssets(token);
    const balanceHistory = assets.balance_history
    window.sessionStorage.setItem(
      "balanceHistory",
      JSON.stringify(balanceHistory)
    );
    setBalanceHistory(balanceHistory);
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

  const currentBalances = balanceHistory.balances[balanceHistory.balances.length - 1]
  const currentSourceBalances = currentBalances.source_balances_history
  const currentTotalBalance = currentBalances.balance
  const history = balanceHistory.balances.map((item) => item.source_balances_history)
  const validData = {}

  for (let entry of history) {
    for (let line of entry) {
      if (!(line.provider in validData)) {
        validData[line.provider] = []
      }
      validData[line.provider].push(line.value)
    }
  }
  console.log(validData.coinbase)
  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        {balanceHistory !== "" && (
          <ChartComponent total={currentTotalBalance} base={base} portfolio={true} history={validData} />
        )}
        <div className="transactions-table">
          <div className="headings">
            <p>Sources</p>
            <p>+</p>
            <p>%PORTFOLIO</p>
            <p>VALUE-1M</p>
            <p>LATEST VALUE</p>
            <p>PERFORMANCE</p>
          </div>
          <ul>
            {currentSourceBalances.map((element) => {
              return (
                <li>
                  <div className="transaction-row">
                    {/* Source */}
                    <p className="transaction-date">
                      {element.provider}
                    </p>

                    {/* Unknown */}
                    <p className="transaction-source">
                      ^
                    </p>

                    {/* percentage */}
                    <p>
                      {((element.value/currentTotalBalance)*100).toFixed(2)}%
                    </p>

                    {/* Value 1M */}
                    <p>
                      1-M value TODO
                    </p>

                    {/* value */}
                    <p>
                      {base} {element.value.toFixed(2)}
                    </p>
                    {/* performance*/}
                    <p>{balanceHistory !== "" && (
                      <ChartComponent
                        total={currentTotalBalance}
                        base={base}
                        history={validData[element.provider]}
                        portfolio={true}
                        embedded={true}
                        provider={element.provider}/>
                    )}</p>
                  </div>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    )
  );
};

export default PortfolioPage;
