import React from "react";
import BalanceComponent from "./BalanceComponent";

const BalancesContainerComponent = ({ data, getTransactionsFunc }) => {
  let provider;
  let account;
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        if (value.status === "success") {
          provider = key;
          return (
            <ul>
              {Object.entries(value.content).map(([key, value]) => {
                account = key;
                return (
                  <li>
                    <BalanceComponent
                      key={key}
                      providerName={value.providerName}
                      amount={value.balanceData.amount}
                      currency={value.balanceData.currency}
                      provider={provider}
                      account={account}
                      getTransactionsFunc={getTransactionsFunc}
                    />
                  </li>
                );
              })}
            </ul>
          );
        }
      })}
    </div>
  );
};

export default BalancesContainerComponent;
