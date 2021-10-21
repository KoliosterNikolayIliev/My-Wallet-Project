import React from "react";

const HoldingComponent = ({ symbol, quantity }) => {
  return (
    <div>
      <p>
        {symbol}: {quantity}
      </p>
    </div>
  );
};

export default HoldingComponent;
