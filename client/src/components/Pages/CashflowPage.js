import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import { recentTransactionsAtom, baseAtom } from "../../recoil";
import { useRecoilState } from "recoil";

import "../../styles/cashflow.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";
import Header from "../Other/HeaderComponent";
import { getAllRecentTransactions } from "../../utils/portfolio";
import { getUser } from "../../utils/account";

// Dashboard page to be filled in with user account data
const CashflowPage = () => {
  const monthNames = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
  };

  const [recentTransactions, setRecentTransactions] = useRecoilState(
    recentTransactionsAtom
  );
  const [base, setBase] = useRecoilState(baseAtom);

  const [isLoading, setIsLoading] = useState(true);

  const [colors, setColors] = useState({
    bank: { "background-color": "#ffa04370", color: "#FFA043" },
    crypto: { "background-color": "#00a5ff70", color: "#00A5FF" },
  });

  const { isAuthenticated, user, loading, getAccessTokenSilently } = useAuth0();

  const getBase = async () => {
    if (!window.sessionStorage.getItem("base")) {
      const token = await getAccessTokenSilently();
      const response = await getUser(token);
      setBase(response.base_currency);
    } else {
      setBase(window.sessionStorage.getItem("base"));
    }
  };

  const getTransactions = async () => {
    const token = await getAccessTokenSilently();
    const transactions = await getAllRecentTransactions(token);

    window.sessionStorage.setItem(
      "recentTransactions",
      JSON.stringify(transactions.content)
    );
    setRecentTransactions(transactions.content);
  };

  useEffect(() => {
    if (recentTransactions === "" || !recentTransactions) {
      getTransactions();
    }
    if (base === "" || !base) {
      getBase();
    }
    setIsLoading(false);
  }, []);

  if (isLoading || recentTransactions === "" || !recentTransactions) {
    return Loader();
  }

  return (
    isAuthenticated && (
      <div className="main">
        <Header
          baseSymbol={base}
          username={user.nickname ? user.nickname : user.name}
        />
        <div className="transactions-table">
          <div className="headings">
            <p>Date</p>
            <p>Source</p>
            <p>Type</p>
            <p>Amount</p>
            <p>Asset</p>
          </div>
          <ul>
            {recentTransactions.map((element) => {
              return Object.values(element).map((value) => {
                return (
                  <li>
                    <div className="transaction-row">
                      {/* Date */}
                      <p className="transaction-date">
                        {monthNames[value.date.split("-")[1]]}{" "}
                        {value.date.split("-")[2]}, {value.date.split("-")[0]}
                      </p>

                      {/* Source */}
                      <p className="transaction-source">{value.source}</p>

                      {/* Type */}
                      <p
                        className="transaction-type"
                        style={
                          colors[value.type]
                            ? colors[value.type]
                            : {
                                backgroundColor: "#a9acb060",
                                color: "#84868a",
                              }
                        }
                      >
                        {value.type}
                      </p>

                      {/* Amount */}
                      <p className="transaction-amount">
                        {Number(value.amount.amount) < 0
                          ? Number(value.amount.amount).toFixed(2)
                          : `+${Number(value.amount.amount).toFixed(2)}`}
                      </p>

                      {/* Asset */}
                      <p className="transaction-asset">
                        {value.amount.currency}
                      </p>
                    </div>
                  </li>
                );
              });
            })}
          </ul>
          {/* <div className="view-all-button">
            <p>Load more</p>
            <svg
              width="8"
              height="12"
              viewBox="0 0 8 12"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1.16994 1.00005C0.983691 1.18741 0.87915 1.44087 0.87915 1.70505C0.87915 1.96924 0.983692 2.22269 1.16994 2.41005L4.70994 6.00005L1.16994 9.54005C0.983692 9.72741 0.87915 9.98087 0.87915 10.2451C0.87915 10.5092 0.983692 10.7627 1.16994 10.9501C1.26291 11.0438 1.37351 11.1182 1.49537 11.1689C1.61723 11.2197 1.74793 11.2458 1.87994 11.2458C2.01195 11.2458 2.14266 11.2197 2.26452 11.1689C2.38638 11.1182 2.49698 11.0438 2.58994 10.9501L6.82994 6.71005C6.92367 6.61709 6.99806 6.50649 7.04883 6.38463C7.0996 6.26277 7.12574 6.13206 7.12574 6.00005C7.12574 5.86804 7.0996 5.73733 7.04883 5.61547C6.99806 5.49362 6.92367 5.38301 6.82994 5.29005L2.58994 1.00005C2.49698 0.906323 2.38638 0.831929 2.26452 0.78116C2.14266 0.730391 2.01195 0.704252 1.87994 0.704252C1.74793 0.704252 1.61722 0.730391 1.49537 0.78116C1.37351 0.831929 1.26291 0.906323 1.16994 1.00005Z"
                fill="#9031DB"
              />
            </svg>
          </div> */}
        </div>
      </div>
    )
  );
};

export default CashflowPage;
