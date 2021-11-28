import React from "react";

const RecentTransactionsContainerComponent = ({ data }) => {
  const monthNames = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
  };

  return (
    <div>
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
                    <p>Paid</p>
                    <p>
                      {monthNames[value.date.split("-")[1]]}{" "}
                      {value.date.split("-")[2]}, {value.date.split("-")[0]}
                    </p>
                  </div>
                )}
                {Number(value.amount.amount) > 0 && (
                  <p>
                    +{Number(value.amount.amount).toFixed(2)}{" "}
                    {value.amount.currency}
                  </p>
                )}
                {Number(value.amount.amount) < 0 && (
                  <p>
                    {Number(value.amount.amount).toFixed(2)}{" "}
                    {value.amount.currency}
                  </p>
                )}
              </li>
            );
          });
        })}
      </ul>
    </div>
  );
};

export default RecentTransactionsContainerComponent;
