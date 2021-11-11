import React from "react";

const HoldingComponent = ({ data, baseSymbol, nest }) => {
  return (
    <div>
      {!nest && (
        <p>
          {data.symbol}: {data.quantity}; {data.base_currency.toFixed(2)}{" "}
          {baseSymbol}
        </p>
      )}
      {nest && (
        <li>
          {data.symbol}: {data.quantity}; {data.base_currency.toFixed(2)}{" "}
          {baseSymbol}
        </li>
      )}
    </div>
  );
};

export default HoldingComponent;
