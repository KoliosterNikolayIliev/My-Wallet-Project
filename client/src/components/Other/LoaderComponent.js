import React from "react";
import "../../styles/loader.scss";

const Loader = () => {
  return <div className="loading">
    <div className="container">
      <div className="dash uno"/>
      <div className="dash dos"/>
      <div className="dash tres"/>
      <div className="dash cuatro"/>
    </div>
  </div>;
};

export default Loader;

