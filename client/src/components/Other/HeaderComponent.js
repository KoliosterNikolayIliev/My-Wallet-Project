import React from "react";
import "../../styles/header.scss";
import logo from "../../images/logo.svg";
import messages from "../../images/messages-2.svg";
import notification from "../../images/Notification.svg";
import services from "../../images/Services.svg";
import profileImage from "../../images/profile_Img.svg";
import arrow_down from "../../images/Vector_down.svg";
import BaseCurrencyDropDownList from "./BaseCurrencyDropDownList";

const Header = ({ baseSymbol, username }) => {
  const showUserMenu = () => {
    console.log("are ve");
  };

  return (
    <nav className="header">
      <div className="menu-image-container">
        <div className="img-container">
          <img src={logo} alt="" />
        </div>
        <div className="borderline" />
        <ul className="menu-rooter">
          <li>
            <a className="nav-link" href="#">
              Overview
            </a>
          </li>
          <li>
            <a className="nav-link" href="#">
              Portfolio
            </a>
          </li>
          <li>
            <a className="nav-link" href="#">
              Cashflow
            </a>
          </li>
          <li>
            <a className="nav-link" href="#">
              Advice
            </a>
          </li>
        </ul>
      </div>
      <div className="user-container">
        {/*<button className="base-currency">USD <img src={arrow} alt="arrow"/></button>*/}
        <BaseCurrencyDropDownList baseSymbol={baseSymbol} />
        <a className="nav-link" href="#">
          <img src={notification} alt="notification" />
        </a>
        <a className="nav-link" href="#">
          <img src={messages} alt="messages" />
        </a>
        <a className="nav-link" href="#">
          <img src={services} alt="services" />
        </a>
        <a className="nav-link" href="#">
          <img src={profileImage} alt="profile" />
        </a>
        <div>
          <span>{username}</span>
          <button onClick={() => showUserMenu()}>
            <img src={arrow_down} alt="user_menu" />
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Header;
