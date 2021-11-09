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
    <div>
      {Object.entries(data).map(([key, value]) => {
        source = key;
        return (
          <div>
            <h3>
              {source[0].toUpperCase() + source.slice(1)}: total balance-{" "}
              {value.total.toFixed(2)} {baseSymbol}
            </h3>
            <ul>
              {value.accounts.map((account) => {
                return (
                  <GroupComponent
                    baseSymbol={baseSymbol}
                    provider={account.provider}
                    account={account}
                    getTransactionsFunc={getTransactionsFunc}
                  />
                );
              })}
              {value.accounts.map((account) => {
                if (account.holdings) {
                  if (account.holdings.length > 0) {
                    return account.holdings.map((holding) => {
                      return (
                        <HoldingComponent
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
            </ul>
          </div>
        );
      })}
    </div>
  );
};

export default GroupsContainerComponent;
