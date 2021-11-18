import React from "react";

const HoldingComponent = ({
  data,
  baseSymbol,
  nest,
  account,
  getTransactionsFunc,
}) => {
  return (
    <div>
      {!nest && (
        <p
          onClick={() => getTransactionsFunc(account.provider, account.id)}
          className="has-transactions"
        >
          {data.symbol}: {data.quantity}; {data.base_currency.toFixed(2)}{" "}
          {baseSymbol}
        </p>
      )}
      {nest && (
        <li>
          {data.symbol}: {data.quantity}; {data.base_currency.toFixed(2)}{" "}
          {baseSymbol}
        </li>
      )}
    </div>
  );
};

export default HoldingComponent;
