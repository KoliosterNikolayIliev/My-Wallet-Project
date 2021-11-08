import React from "react";
import GroupComponent from "./GroupComponent";

const GroupsContainerComponent = ({ data, getTransactionsFunc }) => {
  let source;
  return (
    <div>
      {Object.entries(data).map(([key, value]) => {
        source = key;
        return (
          <div>
            <h3>{source[0].toUpperCase() + source.slice(1)}</h3>
            <ul>
              {value.map((account) => {
                return (
                  <GroupComponent
                    provider={account.provider}
                    account={account}
                    getTransactionsFunc={getTransactionsFunc}
                  />
                );
              })}
            </ul>
          </div>
        );
      })}
    </div>
  );
};

export default GroupsContainerComponent;
