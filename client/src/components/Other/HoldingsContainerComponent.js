import React from "react";
import HoldingComponent from "./HoldingComponent";

const HoldingsContainerComponent = ({ data }) => {
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        if (value.status === "success") {
          return (
            <ul>
              {Object.entries(value.content).map(([key, value]) => {
                return (
                  <li>
                    <HoldingComponent
                      key={key}
                      symbol={value.symbol}
                      quantity={value.quantity}
                    />
                  </li>
                );
              })}
            </ul>
          );
        }
      })}
    </div>
  );
};

export default HoldingsContainerComponent;
