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
          <p className="data-source-asset-value">
            {Number(data.base_currency.toFixed(1)).toLocaleString()} {baseSymbol}
          </p>
        </div>
      )}
      {nest && (
        <div
          className="asset-line"
          onClick={() => getTransactionsFunc(account.provider, account.id)}
        >
            <p className={'data-source-asset'}>{data.symbol}</p>{" "}
            <p className={'data-source-asset-value'}>
              {Number(data.base_currency.toFixed(1)).toLocaleString()} {baseSymbol}
            </p>
        </div>
      )}
    </div>
  );
};

export default HoldingComponent;
