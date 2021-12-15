import React from "react";
import { Link } from "react-router-dom";

const RecentTransactionsContainerComponent = ({ data }) => {
  const monthNames = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
  };

  return (
    <div className="recent-transactions-container">
      <ul>
        {data.map((element) => {
          return Object.values(element).map((value) => {
            return (
              <li>
                {Number(value.amount.amount) < 0 && (
                  <svg
                    width="38"
                    height="38"
                    viewBox="0 0 38 38"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <circle cx="19" cy="19" r="19" fill="#FFE0DB" />
                    <path
                      d="M19 9C13.48 9 9 13.48 9 19C9 24.52 13.48 29 19 29C24.52 29 29 24.52 29 19C29 13.48 24.52 9 19 9ZM22.53 19.03C22.38 19.18 22.19 19.25 22 19.25C21.81 19.25 21.62 19.18 21.47 19.03L19.75 17.31V22.5C19.75 22.91 19.41 23.25 19 23.25C18.59 23.25 18.25 22.91 18.25 22.5V17.31L16.53 19.03C16.24 19.32 15.76 19.32 15.47 19.03C15.18 18.74 15.18 18.26 15.47 17.97L18.47 14.97C18.76 14.68 19.24 14.68 19.53 14.97L22.53 17.97C22.82 18.26 22.82 18.74 22.53 19.03Z"
                      fill="#FF7A68"
                    />
                  </svg>
                )}
                {Number(value.amount.amount) > 0 && (
                  <svg
                    width="38"
                    height="38"
                    viewBox="0 0 38 38"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <circle cx="19" cy="19" r="19" fill="#DFFBF1" />
                    <path
                      d="M19 9C13.48 9 9 13.48 9 19C9 24.52 13.48 29 19 29C24.52 29 29 24.52 29 19C29 13.48 24.52 9 19 9ZM22.53 20.03L19.53 23.03C19.38 23.18 19.19 23.25 19 23.25C18.81 23.25 18.62 23.18 18.47 23.03L15.47 20.03C15.18 19.74 15.18 19.26 15.47 18.97C15.76 18.68 16.24 18.68 16.53 18.97L18.25 20.69V15.5C18.25 15.09 18.59 14.75 19 14.75C19.41 14.75 19.75 15.09 19.75 15.5V20.69L21.47 18.97C21.76 18.68 22.24 18.68 22.53 18.97C22.82 19.26 22.82 19.74 22.53 20.03Z"
                      fill="#1AD492"
                    />
                  </svg>
                )}
                {Number(value.amount.amount) > 0 && (
                  <div className="transaction-text">
                    <p>Received</p>
                    <p>
                      {monthNames[value.date.split("-")[1]]}{" "}
                      {value.date.split("-")[2]}, {value.date.split("-")[0]}
                    </p>
                  </div>
                )}
                {Number(value.amount.amount) < 0 && (
                  <div className="transaction-text">
                    <p>Sent</p>
                    <p>
                      {monthNames[value.date.split("-")[1]]}{" "}
                      {value.date.split("-")[2]}, {value.date.split("-")[0]}
                    </p>
                  </div>
                )}
                {Number(value.amount.amount) > 0 && (
                  <div className="amount-text">
                    <p>
                      +{Number(Number(value.amount.amount).toFixed(1)).toLocaleString()}{" "}
                      {value.amount.currency}
                    </p>
                    <p>
                      {Number(Number(value.amount.base_amount).toFixed(1)).toLocaleString()}{" "}
                      {value.amount.base_currency}
                    </p>
                  </div>
                )}
                {Number(value.amount.amount) < 0 && (
                  <div className="amount-text">
                    <p>
                      {Number(Number(value.amount.amount).toFixed(1)).toLocaleString()}{" "}
                      {value.amount.currency}
                    </p>
                    <p>
                      {Math.abs(Number(value.amount.base_amount).toFixed(1)).toLocaleString()}{" "}
                      {value.amount.base_currency}
                    </p>
                  </div>
                )}
              </li>
            );
          });
        })}
      </ul>
      <div className="expand-button">
        <p>
          <Link className="recent-transactions-link" to={"/cashflow"}>
            View all
          </Link>
        </p>
        <svg
          width="8"
          height="12"
          viewBox="0 0 8 12"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M1.16994 1.00005C0.983691 1.18741 0.87915 1.44087 0.87915 1.70505C0.87915 1.96924 0.983692 2.22269 1.16994 2.41005L4.70994 6.00005L1.16994 9.54005C0.983692 9.72741 0.87915 9.98087 0.87915 10.2451C0.87915 10.5092 0.983692 10.7627 1.16994 10.9501C1.26291 11.0438 1.37351 11.1182 1.49537 11.1689C1.61723 11.2197 1.74793 11.2458 1.87994 11.2458C2.01195 11.2458 2.14266 11.2197 2.26452 11.1689C2.38638 11.1182 2.49698 11.0438 2.58994 10.9501L6.82994 6.71005C6.92367 6.61709 6.99806 6.50649 7.04883 6.38463C7.0996 6.26277 7.12574 6.13206 7.12574 6.00005C7.12574 5.86804 7.0996 5.73733 7.04883 5.61547C6.99806 5.49362 6.92367 5.38301 6.82994 5.29005L2.58994 1.00005C2.49698 0.906323 2.38638 0.831929 2.26452 0.78116C2.14266 0.730391 2.01195 0.704252 1.87994 0.704252C1.74793 0.704252 1.61722 0.730391 1.49537 0.78116C1.37351 0.831929 1.26291 0.906323 1.16994 1.00005Z"
            fill="#9031DB"
          />
        </svg>
      </div>
    </div>
  );
};

export default RecentTransactionsContainerComponent;
