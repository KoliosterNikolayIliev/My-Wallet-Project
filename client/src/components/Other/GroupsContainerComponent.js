import React from "react";
import GroupComponent from "./GroupComponent";
import HoldingComponent from "./HoldingComponent";

const GroupsContainerComponent = ({
  data,
  getTransactionsFunc,
  baseSymbol,
}) => {
  let source;
  return (
    <div className="data-source-container">
      {Object.entries(data).map(([key, value]) => {
        source = key;
        return (
          <div className="data-source">

            <p>
              {source[0].toUpperCase() + source.slice(1)} {" "}
            </p>
            <p>{value.total.toFixed(2)} {baseSymbol}</p>
            <ul>
              {(value.accounts.length > 1 ||
                source === "coinbase" ||
                (value.accounts.length === 1 &&
                  source === "yodlee" &&
                  value.accounts[0].holdings.length === 0)) &&
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
          </div>
        );
      })}
    </div>
  );
};

export default GroupsContainerComponent;
