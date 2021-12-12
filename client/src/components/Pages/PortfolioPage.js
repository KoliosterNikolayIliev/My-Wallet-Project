import React, {useState, useEffect} from "react";
import {useAuth0} from "@auth0/auth0-react";
import {Redirect} from "react-router";
import {buildStyles, CircularProgressbar} from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import "../../styles/portfolio-page.scss";
import Loader from "../Other/LoaderComponent";
import {useRecoilState} from "recoil";
import {getUser} from "../../utils/account";
import Header from "../Other/HeaderComponent";
import {balanceHistoryAtom, baseAtom} from "../../recoil";
import {getAssets, getHistoricalBalances} from "../../utils/portfolio";
import ChartComponent, {hashCode, intToRGB} from "../Other/ChartComponent";
import {getTokenWithErrorHandling} from "./DashboardPage";

// Dashboard page to be filled in with user account data
const PortfolioPage = () => {


  const [balanceHistory, setBalanceHistory] = useRecoilState(
    balanceHistoryAtom
  );
  const [base, setBase] = useRecoilState(baseAtom);

  const [isLoading, setIsLoading] = useState(true);


  const {isAuthenticated, user, loading, getAccessTokenSilently, loginWithRedirect} = useAuth0();

  const getBase = async () => {
    if (!window.sessionStorage.getItem("base")) {
      const token = await getTokenWithErrorHandling(getAccessTokenSilently, loginWithRedirect);
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
  const date = new Date();
  const firstDayOfTheMonth = new Date(date.getFullYear(), date.getMonth(), 2).toISOString()
  const currentBalances = balanceHistory.balances[balanceHistory.balances.length - 1]
  const firstDayOfTheMonthBalance = balanceHistory.balances.filter(
    (element) => element.timestamp.slice(0, 10) === firstDayOfTheMonth.slice(0, 10))[0].source_balances_history
  const currentSourceBalances = currentBalances.source_balances_history
  const currentTotalBalance = currentBalances.balance
  const history = balanceHistory.balances.map((item) => item.source_balances_history)
  const validData = {}
  const extendedCurrentSourceBalance = []

  for (let obj of currentSourceBalances) {
    let addedValue = firstDayOfTheMonthBalance.filter((entry) => entry.provider === obj.provider)
    if (addedValue.length > 0) {
      addedValue = addedValue[0].value
    } else {
      addedValue = 0
    }

    let newObj = {
      provider: obj.provider,
      value: obj.value,
      startMonthValue: addedValue
    }
    extendedCurrentSourceBalance.push(newObj)
  }

  // console.log(extendedCurrentSourceBalance)
  for (let entry of history) {
    for (let line of entry) {
      if (!(line.provider in validData)) {
        validData[line.provider] = []
      }
      validData[line.provider].push(line.value)
    }
  }
  // console.log(validData)
  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        {balanceHistory !== "" && (
          <ChartComponent total={currentTotalBalance} base={base} portfolio={true} history={validData}/>
        )}
        <div className="portfolio-table">
          <div className="table-container">
            <div className="portfolio-headings">
              <p>sources</p>
              {/*<p>+</p>*/}
              <p>%PORTFOLIO</p>
              <p>VALUE-1M</p>
              <p>LATEST VALUE</p>
              <p>PERFORMANCE</p>
            </div>
            <ul>
              {extendedCurrentSourceBalance.map((element) => {
                return (
                  <li>
                    <div className="portfolio-table-row">
                      {/* Source */}
                      <p className="portfolio-source-name" style={{color:intToRGB(hashCode(element.provider))}}>
                        {element.provider.includes('_') ? element.provider.replace('_', ' ') : element.provider}
                      </p>

                      {/*/!* Unknown *!/*/}
                      {/*<p className="transaction-source">*/}
                      {/*  ^*/}
                      {/*</p>*/}

                      {/* percentage */}
                      <p style={{display:'flex', alignItems:'center'}}>
                        <div style={{ width: 20, height: 20, marginRight:'4%', }}><CircularProgressbar
                          value={((element.value / currentTotalBalance) * 100).toFixed(2)} strokeWidth={15}
                          styles={buildStyles(
                            {
                              pathColor:intToRGB(hashCode(element.provider)),
                              trailColor:intToRGB(hashCode(element.provider))+'1A',
                              }
                          )}
                        /></div>

                        {((element.value / currentTotalBalance) * 100).toFixed(2)}%
                      </p>

                      {/* Value 1M */}
                      <p>
                        {base} {Number(Number(element.startMonthValue).toFixed(1)).toLocaleString()}
                      </p>

                      {/* value */}
                      <p>
                        {base} {Number(Number(element.value).toFixed(1)).toLocaleString()}
                      </p>
                      {/* performance*/}
                      <p className={'small-chart-container'}>{balanceHistory !== "" && (
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
      </div>
    )
  );
};

export default PortfolioPage;
