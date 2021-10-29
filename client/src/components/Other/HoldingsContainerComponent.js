import React from "react";
import HoldingComponent from "./HoldingComponent";

const HoldingsContainerComponent = ({data, getTransactionsFunc}) => {
  let provider;
  let account;
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        if (value.status === "success") {
          provider = key
          return (
            <ul>
              {Object.entries(value.content).map(([key, value]) => {
                account = key

                if (provider === 'coinbase') {
                  return (
                    <li>
                      <HoldingComponent
                        key={key}
                        symbol={value.symbol}
                        quantity={value.quantity}
                        provider={provider}
                        account={account}
                        getTransactionsFunc={getTransactionsFunc}
                      />
                    </li>
                  );
                } else {
                  return (
                    <li>
                      <HoldingComponent
                        key={key}
                        symbol={value.symbol}
                        quantity={value.quantity}
                      />
                    </li>
                  );
                }
              })}
            </ul>
          );
        }
      })}
    </div>
  );
};

export default HoldingsContainerComponent;
