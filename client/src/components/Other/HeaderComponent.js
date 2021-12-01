import React, { Fragment } from "react";
import "../../styles/header.scss";
import logo from "../../images/logo.svg";
import messages from "../../images/messages-2.svg";
import notification from "../../images/Notification.svg";
import services from "../../images/Services.svg";
import profileImage from "../../images/profile_Img.svg";
import arrow_down from "../../images/Vector_down.svg";
import BaseCurrencyDropDownList from "./BaseCurrencyDropDownList";
import LogOutButton from "../Buttons/LogOutButton";

import { Link } from "react-router-dom";

import { styled } from "@mui/material/styles";
import Tooltip, { tooltipClasses } from "@mui/material/Tooltip";
import ClickAwayListener from "@mui/material/ClickAwayListener";
import Button from "@mui/material/Button";

const Header = ({ baseSymbol, username }) => {
  const [open, setOpen] = React.useState(false);

  const handleTooltipClose = () => {
    setOpen(false);
  };

  const handleTooltipOpen = () => {
    setOpen(true);
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
            <Link to={"/"}>Overview</Link>
          </li>
          <li>
            <Link to={"/portfolio"}>Portfolio</Link>
          </li>
          <li>
            <Link to={"/cashflow"}>Cashflow</Link>
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
          <ClickAwayListener onClickAway={handleTooltipClose}>
            <div>
              <Tooltip
                PopperProps={{
                  disablePortal: true,
                }}
                onClose={handleTooltipClose}
                open={open}
                disableFocusListener
                disableHoverListener
                disableTouchListener
                title={
                  <Fragment>
                    <LogOutButton />
                  </Fragment>
                }
              >
                <Button onClick={handleTooltipOpen}>
                  <img src={arrow_down} alt="user_menu" />
                </Button>
              </Tooltip>
            </div>
          </ClickAwayListener>
        </div>
      </div>
    </nav>
  );
};

export default Header;
