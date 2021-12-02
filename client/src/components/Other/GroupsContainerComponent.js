import React from "react";
import GroupComponent from "./GroupComponent";
import HoldingComponent from "./HoldingComponent";
import ExpandButton from "./ExpandButton";

const GroupsContainerComponent = ({
  data,
  total,
  getTransactionsFunc,
  baseSymbol,
  user,
}) => {
  let source;
  return (
    <div className="data-source-container">
      {Object.entries(data).map(([key, value]) => {
        source = key;
        return (
          <div className="data-source">
            <div className="data-source-header">
              <p>{source[0].toUpperCase() + source.slice(1)} </p>
              <p className="data-source-total">
                {value.total.toFixed(2)} {baseSymbol}
              </p>
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
