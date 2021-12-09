import React, { useRef, useState, useEffect } from "react";
import "../../styles/chart_component.scss";
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
  Filler,
} from "chart.js";

import { Chart, Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Filler,
  Title,
  Tooltip,
  Legend
);

const ChartComponent = ({ total, base, history }) => {
  const chartRef = useRef(null);
  const [chartData, setChartData] = useState({
    datasets: [],
  });

  const labels =
    // array of days of the month until today
    Array.from(Array(new Date().getDate()).keys()).map((i) => {
      return i + 1;
    });

  const createBackgroundGradient = (ctx) => {
    const gradient = ctx.createLinearGradient(0, 0, 0, 400, 0.1);
    gradient.addColorStop(0, "rgba(190,56,242,0.4)");
    gradient.addColorStop(0.7, "rgba(190,56,242,0)");
    gradient.addColorStop(1, "rgba(0,0,0,0)");

    return gradient;
  };

  const options = {
    responsive: true,
    scales: {
      x: {
        grid: {
          display: false,
        },
      },
      y: {
        grid: {
          display: false,
        },
      },
    },
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

  useEffect(() => {
    const chart = chartRef.current;

    if (chart) {
      setChartData({
        labels,
        datasets: [
          {
            label: "Balance",
            data: history.balances.map((item) => item.balance),
            fill: true,
            borderColor: "rgba(190, 56, 242, 1)",
            tension: 0.3,
            backgroundColor: createBackgroundGradient(chart.ctx),
          },
        ],
      });
    }
  }, []);

  if (!history || history === "") {
    return <Loader />;
  }

  return (
    <div className="info-container">
      <div className="total-balance">
        <div className="total-balance-text">
          <p className="total-balance-title">Total Balance</p>
          <p className="total-balance-base">{base}</p>
        </div>
        <p className="total-balance-value">{Number(Number(total).toFixed(1)).toLocaleString()}</p>
      </div>
      <div className="chart-container">
        <div className="chart">
          <Chart
            type="line"
            ref={chartRef}
            options={options}
            data={chartData}
          />
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
