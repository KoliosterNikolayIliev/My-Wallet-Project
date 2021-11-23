import React from "react";

const RecentTransactionsContainerComponent = ({ data }) => {
  return (
    <div>
      <ul>
        {data.map((element) => {
          return Object.values(element).map((value) => {
            return (
              <li>
                {value.amount.amount} {value.amount.currency}
              </li>
            );
          });
        })}
      </ul>
    </div>
  );
};

export default RecentTransactionsContainerComponent;
