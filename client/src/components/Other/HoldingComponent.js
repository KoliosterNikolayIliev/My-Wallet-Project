import React from "react";

const HoldingComponent = ({ data, baseSymbol }) => {
  return (
    <p>
      {data.symbol}: {data.quantity}; {data.base_currency.toFixed(2)}{" "}
      {baseSymbol}
    </p>
  );
};

export default HoldingComponent;
