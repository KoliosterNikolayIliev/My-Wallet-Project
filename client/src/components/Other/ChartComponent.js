import React from "react";
import "../../styles/chart_component.scss";
import fakeGraph from "../../images/fake_graph.png";

const ChartComponent = ({ total, base }) => {
  return (
    <div className="info-container">
      <div className="total-balance">
        <div className="total-balance-text">
          <p className="total-balance-title">Total Balance</p>
          <p className="total-balance-base">{base}</p>
        </div>
        <p className="total-balance-value">{Number(total).toFixed(2)}</p>
      </div>
      <div className="chart-container">
        <div className="chart">
          <img src={fakeGraph} alt="graph" />
        </div>

        <div className="notifications">
          <p className="notifications-title">Notifications</p>
          <div>
            <p className="notifications-message">No notifications to show</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChartComponent;
