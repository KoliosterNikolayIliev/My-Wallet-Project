import React from "react";

const HoldingComponent = ({symbol, quantity, provider, account, getTransactionsFunc}) => {
  if (!provider) {
    return (
      <div>
        <p>
          {symbol}: {quantity}
        </p>
      </div>
    );
  } else {
    return (
      <div>
        <p onClick={() => getTransactionsFunc(provider, account)} className='has-transactions'>
          {symbol}: {quantity}
        </p>
      </div>
    );
  }
};

export default HoldingComponent;
