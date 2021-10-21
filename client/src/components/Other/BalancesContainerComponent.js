import React from "react";
import BalanceComponent from "./BalanceComponent";

const BalancesContainerComponent = ({ data }) => {
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        if (value.status === "success") {
          return (
            <ul>
              {Object.entries(value.content).map(([key, value]) => {
                return (
                  <li>
                    <BalanceComponent
                      key={key}
                      providerName={value.providerName}
                      amount={value.balanceData.amount}
                      currency={value.balanceData.currency}
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
