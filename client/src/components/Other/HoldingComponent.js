import React from "react";

const HoldingComponent = ({ data }) => {
  console.log(data);
  return (
    <p>
      {data.symbol}: {data.quantity}
    </p>
  );
};

export default HoldingComponent;
