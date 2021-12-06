import React, { useEffect, useState } from "react";
import GroupComponent from "./GroupComponent";
import HoldingComponent from "./HoldingComponent";
import ExpandButton from "./ExpandButton";

import { useRecoilState } from "recoil";
import { balanceHistoryAtom } from "../../recoil";
import { getAssets } from "../../utils/portfolio";
import { useAuth0 } from "@auth0/auth0-react";
import Loader from "./LoaderComponent";

const GroupsContainerComponent = ({
  data,
  total,
  getTransactionsFunc,
  baseSymbol,
  user,
}) => {
  const { getAccessTokenSilently } = useAuth0();
  const [isLoading, setIsLoading] = useState(true);
  let source;
  const [balanceHistory, setBalanceHistory] =
    useRecoilState(balanceHistoryAtom);

  const getData = async () => {
    const token = await getAccessTokenSilently();
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
    setBalanceHistory(cached_history);
  };

  useEffect(() => {
    if (balanceHistory === "" || !balanceHistory) {
      if (window.sessionStorage.getItem("balanceHistory")) {
        setBalanceHistory(
          JSON.parse(window.sessionStorage.getItem("balanceHistory"))
        );
      } else {
        getData();
      }
    }
    setIsLoading(false);
  }, []);

  if (isLoading || balanceHistory === "" || !balanceHistory) {
    return Loader();
  }

  const source_balances_history =
    balanceHistory["balances"][0]["source_balances_history"];

  return (
    <div className="data-source-container">
      {Object.entries(data).map(([key, value]) => {
        source = key;
        let source_previous_balance;
        let percentage;

        source_balances_history.map((item) => {
          if (item.provider === source) {
            source_previous_balance = item.value;
            percentage = (source_previous_balance / value.total) * 100;
            if (percentage > 100) {
              percentage -= 100;
            } else {
              percentage = 100 - percentage;
            }
            percentage = percentage.toFixed(2);
          }
        });

        return (
          <div className="data-source">
            <div className="data-source-header">
              <p className="data-source-name">
                {source !== "custom_assets"
                  ? source[0].toUpperCase() + source.slice(1)
                  : "Assets"}{" "}
              </p>
              <p className="data-source-total">
                {value.total.toFixed(2)} {baseSymbol}
              </p>
              {value.total !== source_previous_balance ? (
                value.total < source_previous_balance ? (
                  <p className="data-source-change positive">
                    <svg
                      width="16"
                      height="11"
                      viewBox="0 0 16 11"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M 5.9588 0.1946 C 5.8565 0.0714 5.7039 0 5.5428 0 C 5.3817 0 5.2291 0.0714 5.1268 0.1946 L 0.4468 6.3758 C 0.3286 6.5319 0.3096 6.7407 0.3977 6.9152 C 0.4858 7.0897 0.6658 7.2 0.8628 7.2 H 10.2228 C 10.4198 7.2 10.5998 7.0897 10.6879 6.9152 C 10.776 6.7407 10.757 6.5319 10.6388 6.3758 L 5.9588 0.1946 Z"
                        fill="#4FBF67"
                      />
                    </svg>
                    {percentage}%
                  </p>
                ) : (
                  <p className="data-source-change negative">
                    <svg
                      width="16"
                      height="11"
                      viewBox="0 0 16 11"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      style={{ transform: "rotate(180deg)" }}
                    >
                      <path
                        d="M 5.9588 0.1946 C 5.8565 0.0714 5.7039 0 5.5428 0 C 5.3817 0 5.2291 0.0714 5.1268 0.1946 L 0.4468 6.3758 C 0.3286 6.5319 0.3096 6.7407 0.3977 6.9152 C 0.4858 7.0897 0.6658 7.2 0.8628 7.2 H 10.2228 C 10.4198 7.2 10.5998 7.0897 10.6879 6.9152 C 10.776 6.7407 10.757 6.5319 10.6388 6.3758 L 5.9588 0.1946 Z"
                        fill="#FF7A68"
                      />
                    </svg>
                    {percentage}%
                  </p>
                )
              ) : (
                <p className="data-source-change neutral">0%</p>
              )}
            </div>
            <div className="data-source-content">
              <ul>
                {(value.accounts.length > 1 ||
                  value.accounts[0].provider === "coinbase" ||
                  (value.accounts.length === 1 &&
                    value.accounts[0].provider === "yodlee" &&
                    value.accounts[0].holdings.length === 0) ||
                  value.accounts[0].provider === "custom_assets") &&
                  value.accounts.map((account) => {
                    return (
                      <GroupComponent
                        source={source[0].toUpperCase() + source.slice(1)}
                        baseSymbol={baseSymbol}
                        provider={account.provider}
                        account={account}
                        type={account.data.accountType}
                        getTransactionsFunc={getTransactionsFunc}
                      />
                    );
                  })}
                {value.accounts.length <= 1 &&
                  value.accounts.map((account) => {
                    if (account.holdings) {
                      if (account.holdings.length > 0) {
                        return account.holdings.map((holding) => {
                          return (
                            <HoldingComponent
                              nest={false}
                              account={account}
                              getTransactionsFunc={getTransactionsFunc}
                              data={holding}
                              baseSymbol={baseSymbol}
                            />
                          );
                        });
                      }
                      return null;
                    }
                    return null;
                  })}
                {value.accounts.length > 1 &&
                  value.accounts.map((account) => {
                    if (account.holdings) {
                      if (account.holdings.length > 0) {
                        return (
                          <ul>
                            {account.holdings.map((holding) => {
                              return (
                                <HoldingComponent
                                  nest={true}
                                  data={holding}
                                  baseSymbol={baseSymbol}
                                />
                              );
                            })}
                          </ul>
                        );
                      }
                      return null;
                    }
                    return null;
                  })}
              </ul>
              <ExpandButton user={user} name={source} source={value} />
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default GroupsContainerComponent;
