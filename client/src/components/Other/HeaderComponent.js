import React from "react";
import "../../styles/header.scss";
import logo from "../../images/logo.svg"
import arrow from "../../images/double-arrow.svg"
import messages from "../../images/messages-2.svg"
import notification from "../../images/Notification.svg"
import services from "../../images/Services.svg"
import profileImage from "../../images/profile_Img.svg"
import arrow_down from "../../images/Vector_down.svg"


const Header = () => {
  return <nav className="header">
    <span className="img-container"><img src={logo} alt=""/></span>
        <span>
            <a className="nav-link" href="#">Overview</a>
            <a className="nav-link" href="#">Portfolio</a>
            <a className="nav-link" href="#">Cashflow</a>
            <a className="nav-link" href="#">Advice</a>
        </span>
    <span>
      <button className="base-currency">USD <img src={arrow} alt="arrow"/></button>
      <a className="nav-link" href="#"><img src={notification} alt="notification"/></a>
      <a className="nav-link" href="#"><img src={messages} alt="messages"/></a>
      <a className="nav-link" href="#"><img src={services} alt="services"/></a>
      <a className="nav-link" href="#"><img src={profileImage} alt="profile"/></a>
      <span>TestAccount</span>
      <a href="#"><img src={arrow_down} alt="user_menu"/></a>
    </span>
  </nav>
};

export default Header;