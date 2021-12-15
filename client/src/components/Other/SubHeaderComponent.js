import React, { useState, useEffect } from "react";
import "../../styles/subheader.scss";

const SubHeader = ({ user }) => {
  const [date, setDate] = useState(null);
  const [day, setDay] = useState(null);
  const [greeting, setGreeting] = useState(null);

  const monthNames = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
  };

  const dayNames = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
  };

  useEffect(() => {
    const today = new Date();

    const dayOfMonth = today.getDate();
    let month = today.getMonth() + 1;
    month = monthNames[month];

    let day = today.getDay();
    day = dayNames[day];

    const year = today.getFullYear();

    let hour = today.getHours();
    let greeting = 'Good morning'
    if (hour>10){
      greeting='Good day'
    }
    if (hour>17){
      greeting='Good evening'
    }
    setDate(`${dayOfMonth} ${month} ${year}`);
    setDay(day);
    setGreeting(greeting)
  }, []);

  return (
    <div className="subheader">
      <div>
        <p>{greeting}, {user.name}</p>
        <p>Have you added your investment? </p>
        <span>
          <a href="#add-source-btn">Add now</a>
        </span>
      </div>
      <div>
        <p>{day}</p>
        <p>{date}</p>
      </div>
    </div>
  );
};

export default SubHeader;

// <div className="subheader">
//   <div>
//     <h2>Hi, {user.name}, this is the dashboard</h2>
//     <p>Have you added your investment? </p>
//     <span><a href="#">Add now</a></span>
//   </div>
//   <div>
//     <p>Friday</p>
//     <p>26 November 2029</p>
//   </div>
// </div>
