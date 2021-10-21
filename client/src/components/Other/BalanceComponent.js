import React from "react";

const BalanceComponent = ({ providerName, amount, currency }) => {
  return (
    <div>
      <p>
        {providerName}: {amount} {currency}
      </p>
    </div>
  );
};

export default BalanceComponent;
