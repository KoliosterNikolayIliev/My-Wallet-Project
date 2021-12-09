import React from "react";

const HoldingComponent = ({
  data,
  baseSymbol,
  nest,
  account,
  getTransactionsFunc,
}) => {
  return (
    <div className="asset-root">
      {!nest && (
        <div
          className="asset-line"
          onClick={() => getTransactionsFunc(account.provider, account.id)}
        >
          <p className="data-source-asset">{data.symbol}</p>
          <p className="data-source-asset">
            {Number(data.base_currency.toFixed(1)).toLocaleString()} {baseSymbol}
          </p>
        </div>
      )}
      {nest && (
        <div
          className="asset-line"
          onClick={() => getTransactionsFunc(account.provider, account.id)}
        >
          <li className="data-source-asset">
            <p>{data.symbol}</p>{" "}
            <p>
              {Number(data.base_currency.toFixed(1)).toLocaleString()} {baseSymbol}
            </p>
          </li>
        </div>
      )}
    </div>
  );
};

export default HoldingComponent;
