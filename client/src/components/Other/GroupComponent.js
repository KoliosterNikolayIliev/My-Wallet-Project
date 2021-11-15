import React, { useState } from "react";

const GroupComponent = ({
  account,
  source,
  type,
  provider,
  getTransactionsFunc,
  baseSymbol,
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
    base_currency = base_currency.toFixed(2);
  }

  if (amount > 0) {
    return (
      <div>
        {provider !== "binance" &&
          provider !== "custom_assets" &&
          provider !== "coinbase" && (
            <p
              onClick={() => getTransactionsFunc(provider, account.id)}
              className="has-transactions"
            >
              {type}: {base_currency} {baseSymbol}
            </p>
          )}
        {(provider === "custom_assets" || provider === "binance") && (
          <p>
            {currency}: {amount.toFixed(2)}; {base_currency} {baseSymbol}
          </p>
        )}
        {provider === "coinbase" && (
          <p
            onClick={() => getTransactionsFunc(provider, account.id)}
            className="has-transactions"
          >
            {currency}: {amount.toFixed(2)}; {base_currency} {baseSymbol}
          </p>
        )}
      </div>
    );
  }
  return null;
};

export default GroupComponent;
