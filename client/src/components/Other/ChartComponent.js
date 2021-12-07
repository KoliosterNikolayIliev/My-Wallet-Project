import React from "react";
import "../../styles/chart_component.scss";
import fakeGraph from "../../images/fake_graph.png";
import Loader from "./LoaderComponent";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ChartComponent = ({ total, base, history }) => {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: "Historical Balance Chart",
      },
    },
  };

  if (!history) {
    return <Loader />;
  }

  const labels =
    // array of days of the month until today
    Array.from(Array(new Date().getDate()).keys()).map((i) => {
      return i + 1;
    });
  const data = {
    labels,
    datasets: [
      {
        label: "Balance",
        data: history.balances.map((item) => item.balance),
        borderColor: "#BE38F2",
        backgroundColor: "#BE38F2",
      },
    ],
  };

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
          <Line options={options} data={data} />
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
