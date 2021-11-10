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
    amount = account.data.balanceData.amount;
    currency = account.data.balanceData.currency;
    base_currency = account.data.balanceData.base_currency;
  } else {
    amount = account.data.quantity;
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
        {provider !== "binance" && provider !== "custom_assets" && (
          <p
            onClick={() => getTransactionsFunc(provider, account.id)}
            className="has-transactions"
          >
            {type}: {base_currency} {baseSymbol}
          </p>
        )}
        {provider === "custom_assets" && (
          <p>
            {currency}: {amount}; {base_currency} {baseSymbol}
          </p>
        )}
        {provider === "binance" && (
          <p>
            {type}: {amount}; {base_currency} {baseSymbol}
          </p>
        )}
      </div>
    );
  }
  return null;
};

export default GroupComponent;
