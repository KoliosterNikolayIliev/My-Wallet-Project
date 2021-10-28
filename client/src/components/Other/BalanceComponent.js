import React from "react";

const BalanceComponent = ({ providerName, amount, currency, provider, account, getTransactionsFunc }) => {
  return (
    <div>
      <p onClick={() => getTransactionsFunc(provider, account)} className='has-transactions'>
        {providerName}: {amount} {currency}
      </p>
    </div>
  );
};

export default BalanceComponent;
