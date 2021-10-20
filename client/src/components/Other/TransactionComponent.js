import React from "react";

const TransactionComponent = ({ amount, currency }) => {
  return (
    <p>
      {amount} {currency}
    </p>
  );
};

export default TransactionComponent;
