import React from "react";
import "../../styles/subheader.scss";

const SubHeader = (user) => {
  return <div className="subheader">
    <div>
      <p>Good morning, {user.name}</p>
      <p>Have you added your investment? </p>
      <span><a href="#">Add now</a></span>
    </div>
    <div>
      <p>Friday</p>
      <p>26 November 2029</p>
    </div>
  </div>
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