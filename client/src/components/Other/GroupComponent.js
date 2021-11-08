import React from "react";

const GroupComponent = ({ account, provider, getTransactionsFunc }) => {
  let amount = 0;
  let currency = "";

  if (account.data.balanceData) {
    amount = account.data.balanceData.amount;
    currency = account.data.balanceData.currency;
  } else {
    amount = account.data.quantity;
    currency = account.data.symbol;
  }

  if (amount > 0) {
    return (
      <div>
        <p
          onClick={() => getTransactionsFunc(provider, account.id)}
          className="has-transactions"
        >
          {currency}: {amount}
        </p>
      </div>
    );
  }
  return null;
};

export default GroupComponent;
