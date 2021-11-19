import React from "react";
import "../../styles/chart_component.scss";
import fakeGraph from "../../images/fake_graph.png"
import fakeNotifications from "../../images/fake_notifications.png"

const ChartComponent = () => {
  return <div className="chart-container">
    <div className="chart">
      <img src={fakeGraph} alt="graph"/>
    </div>
    <div>
      <div className="notifications">
        <img src={fakeNotifications} alt="notifications"/>
      </div>
    </div>
  </div>
};

export default ChartComponent;