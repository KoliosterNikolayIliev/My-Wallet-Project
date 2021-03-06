import React, {useRef, useState, useEffect} from "react";
import "../../styles/chart_component.scss";
import Loader from "./LoaderComponent";
import {useLocation} from "react-router-dom";
import {
  Chart as ChartJS,
  registerables
} from "chart.js";

import {Chart} from "react-chartjs-2";
import NotificationComponent from "./NotificationComponent";

ChartJS.register(
  ...registerables
);

export function hashCode(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  return hash;
}

export function intToRGB(i) {
  let c = (i & 0x00FFFFFF)
    .toString(16)
    .toUpperCase();

  return "#" + "00000".substring(0, 6 - c.length) + c;
}


const ChartComponent = ({total, base, history,timestamps, portfolio = false, embedded = false, provider = ''}) => {
  const location = useLocation();
  const chartRef = useRef(null);
  const [chartData, setChartData] = useState({
    datasets: [],
  });

  const labels =
    // array of days of the month until today
    Array.from(Array(new Date().getUTCDate()).keys()).map((i) => {
      return i + 1;
    });
  const createBackgroundGradient = (ctx, color) => {
    const gradient = ctx.createLinearGradient(0, 0, 0, 450, 0.1);
    if (color.startsWith('#')) {
      color = color + '0D'
    }
    gradient.addColorStop(0, color);
    gradient.addColorStop(1, "#FFFFFF1A");


    return gradient;
  };
  const datasets = []
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        grid: {
          display: false,
        },
      },
      y: {
        grid: {
          display: true,
          borderDash:[3]

        },
      },
    },
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
      },
    },
  };

  if (embedded) {
    options.scales.x.display = false
    options.scales.y.display = false
  }
  function validateOneMonthHistory(history,timestamps){
    if (history.length==0){
      return history
    }
    const currentMonth = new Date().getUTCMonth()+1
    let validTimestamps = []
    for (let timestamp of timestamps){
      let month=timestamp.slice(5,7)
      if(month==currentMonth){
        validTimestamps.push(timestamp)
      }
    }
    if (validTimestamps==0 && history.length>0){
      history=[history[history.length-1]]
      return history
    }
    history=history.slice(history.length-validTimestamps.length)
    return history
  }

  useEffect(() => {
    const chart = chartRef.current;

    if (chart) {
      let color = "rgba(190,56,242,0.1)"
      if (!portfolio) {
        setChartData({
          labels,
          datasets: [
            {
              label: "Balance",
              data: validateOneMonthHistory(history,timestamps),
              fill: true,
              borderColor: "rgba(190, 56, 242, 1)",
              borderWidth:2,
              tension: 0.3,
              // backgroundColor:"transparent"
              backgroundColor: createBackgroundGradient(chart.ctx, color),
            },
          ],
        });
      } else if (!embedded) {
        Object.entries(history).map(entry => {
          let key = entry[0];
          let value = entry[1];
          datasets.push({
            label: key,
            data: validateOneMonthHistory(value,timestamps),
            fill: true,
            borderColor: intToRGB(hashCode(key)),
            borderWidth:2,
            tension: 0.3,
            // backgroundColor:"transparent"
            backgroundColor: createBackgroundGradient(chart.ctx, intToRGB(hashCode(key))),
          });
        });
        setChartData({
          labels,
          datasets: datasets,
        });
      } else {
        setChartData({
          labels,
          datasets: [
            {
              label: provider,
              data: validateOneMonthHistory(history,timestamps),
              borderColor: intToRGB(hashCode(provider)),
              borderWidth:1,
              tension: 0.3,
              elements: {
                point: {
                  radius: 0
                }
              }
            },
          ],
        });
      }
    }
  }, []);
  if (!history || history === "") {
    return <Loader/>;
  }

  return !embedded ? (
    <div className={location.pathname !== '/portfolio'?"chart-container":"portfolio-chart-container"}>
      <div className={'balance-chart-container'}>
        {location.pathname !== '/portfolio' ?
          <div className="total-balance">
            <div className="total-balance-text">
              <p className="total-balance-title">Total Balance</p>
              <p className="total-balance-base">{base}</p>
            </div>
            <p className="total-balance-value">{Number(Number(total).toFixed(1)).toLocaleString()}</p>
          </div> :
          <p className="portfolio-chart-title">Portfolio performance</p>
          }
        <div className={'only-chart'}>
          <div className="chart">
            <Chart
              type="line"
              ref={chartRef}
              options={options}
              data={chartData}
            />
          </div>
        </div>
      </div>
      {location.pathname !== '/portfolio' ? NotificationComponent() : null}
    </div>
  ) : <div><Chart
    type="line"
    ref={chartRef}
    options={options}
    data={chartData}
  /></div>
};


export default ChartComponent;
