import React from "react";
import TransactionComponent from "./TransactionComponent";

const TransactionsContainerComponent = ({ data }) => {
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        if (value.status === "success") {
          return (
            <div>
              {Object.entries(value.content).map(([key, value]) => {
                return (
                  <div>
                    <h3>{key}</h3>
                    {console.log(value)}
                    <ul>
                      {Object.entries(value).map(([key, value]) => {
                        return (
                          <li>
                            <TransactionComponent
                              key={key}
                              amount={value.amount}
                              currency={value.currency}
                            />
                          </li>
                        );
                      })}
                    </ul>
                  </div>
                );
              })}
            </div>
          );
        }
      })}
    </div>
  );
};

export default TransactionsContainerComponent;
