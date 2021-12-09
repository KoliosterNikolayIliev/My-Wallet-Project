import React, {useRef, useState, useEffect} from "react";
import "../../styles/chart_component.scss";
import Loader from "./LoaderComponent";
import {useLocation} from "react-router-dom";
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

import {Chart, Line} from "react-chartjs-2";
import NotificationComponent from "./NotificationComponent";

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

const ChartComponent = ({total, base, history, portfolio = false, embedded = false}) => {
  const location = useLocation();
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
  const datasets = []
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

  if (portfolio) {
    options.plugins.title.text = "Portfolio performance"
  }
  if (embedded) {
    delete options.plugins.title.text
    options.scales.x.display = false
    options.scales.y.display = false
  }

  useEffect(() => {
    const chart = chartRef.current;

    if (chart) {
      if (!portfolio) {
        setChartData({
          labels,
          datasets: [
            {
              label: "Balance",
              data: history,
              fill: true,
              borderColor: "rgba(190, 56, 242, 1)",
              tension: 0.3,
              backgroundColor: createBackgroundGradient(chart.ctx),
            },
          ],
        });
      } else if (!embedded) {


        Object.entries(history).map(entry => {
          let key = entry[0];
          let value = entry[1];
          datasets.push({
            label: key,
            data: value,
            fill: true,
            borderColor: "rgba(190, 56, 242, 1)",
            tension: 0.3,
            backgroundColor: createBackgroundGradient(chart.ctx),
          });
        });
        // console.log(datasets)
        setChartData({
          labels,
          datasets: datasets,
        });
      } else {
        setChartData({
          labels,
          datasets: [
            {
              label: "Balance",
              data: history,
              borderColor: "rgba(190, 56, 242, 1)",
              tension: 0.3,
            },
          ],
        });
      }
    }
  }, []);
  // console.log(history.balances.map((item) => item.source_balances_history.map((item)=>item)[2]).map((item=>item.value)))
  if (!history || history === "") {
    return <Loader/>;
  }

  return !embedded ? (
    <div className="info-container">
      {location.pathname !== '/portfolio' ?
        <div className="total-balance">
          <div className="total-balance-text">
            <p className="total-balance-title">Total Balance</p>
            <p className="total-balance-base">{base}</p>
          </div>
          <p className="total-balance-value">{Number(total).toFixed(2)}</p>
        </div> : null}

      <div className="chart-container">
        <div className="chart">
          <Chart
            type="line"
            ref={chartRef}
            options={options}
            data={chartData}
          />
        </div>
        {location.pathname !== '/portfolio' ? NotificationComponent() : null}
      </div>
    </div>
  ) : <div><Chart
    type="line"
    ref={chartRef}
    options={options}
    data={chartData}
  /></div>
};

export default ChartComponent;
