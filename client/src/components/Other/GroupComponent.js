import React, { useState } from "react";

const GroupComponent = ({
  account,
  source,
  type,
  provider,
  baseSymbol,
  custom_asset,
  deleteCustomAssetFunc,
}) => {
  let amount = 0;
  let currency = "";
  let base_currency = 0;

  if (account.data.balanceData) {
    amount = Number(account.data.balanceData.amount);
    currency = account.data.balanceData.currency;
    base_currency = account.data.balanceData.base_currency;
  } else {
    amount = Number(account.data.quantity);
    currency = account.data.symbol;
    base_currency = account.data.base_currency;
  }

  if (!type) {
    type = `${source} account(${currency})`;
  } else {
    type = `${source} ${type} account(${currency})`;
  }

  if (!base_currency) {
    base_currency = "N/A";
  } else {
    base_currency = Number(base_currency.toFixed(1)).toLocaleString();
  }

  if (amount > 0) {
    return (
      <div className="asset-root">
        {provider !== "binance" &&
          provider !== "custom_assets" &&
          provider !== "coinbase" && (
            <div
              className="asset-line"
            >
              <p className="data-source-asset">{type}</p>{" "}
              <p className="data-source-asset">
                {base_currency} {baseSymbol}
              </p>
            </div>
          )}
        {(provider === "custom_assets" || provider === "binance") && (
          <div className="asset-line">
            {custom_asset && <button onClick={() => deleteCustomAssetFunc(currency, custom_asset)}>X</button>}
            <p>{currency}</p>{" "}
            <p>
              {" "}
              {base_currency} {baseSymbol}
            </p>
          </div>
        )}
        {provider === "coinbase" && (
          <div
            className="asset-line"
          >
            <p className="data-source-asset">{currency}</p>{" "}
            <p className="data-source-asset">
              {" "}
              {base_currency} {baseSymbol}
            </p>
          </div>
        )}
      </div>
    );
  }
  return null;
};

export default GroupComponent;
