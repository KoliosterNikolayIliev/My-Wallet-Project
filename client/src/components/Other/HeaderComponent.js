import React, {Fragment} from "react";
import "../../styles/header.scss";
import logo from "../../images/logo.svg";
import arrow_down from "../../images/Vector_down.svg";
import BaseCurrencyDropDownList from "./BaseCurrencyDropDownList";
import LogOutButton from "../Buttons/LogOutButton";

import {Link} from "react-router-dom";

import {styled} from "@mui/material/styles";
import Tooltip, {tooltipClasses} from "@mui/material/Tooltip";
import ClickAwayListener from "@mui/material/ClickAwayListener";
import Button from "@mui/material/Button";
import {useLocation} from "react-router-dom";

const Header = ({baseSymbol, username}) => {
  const [open, setOpen] = React.useState(false);
  const location = useLocation();
  const border='border-bottom: 3px solid #9031db;'
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
          <img src={logo} alt=""/>
        </div>
        <div className="borderline"/>
        <ul className="menu-rooter">
          <li style={location.pathname === "/dashboard" ? {border: border} : {border: 'none'}}>
            <Link className="header-link"
                  style={location.pathname === "/dashboard" ? {color: '#9031db'} : {color: '#969aa4'}} to={"/"}>
              <p>Overview</p>
            </Link>
          </li>
          <li style={location.pathname === "/portfolio" ? {border: border} : {border: 'none'}}>
            <Link className="header-link"
                  style={location.pathname === "/portfolio" ? {color: '#9031db'} : {color: '#969aa4'}}
                  to={"/portfolio"}>
              <p>Portfolio</p>
            </Link>
          </li>
          <li style={location.pathname === "/cashflow" ? {border: border} : {border: 'none'}}>
            <Link className="header-link"
                  style={location.pathname === "/cashflow" ? {color: '#9031db'} : {color: '#969aa4'}} to={"/cashflow"}>
              <p>Cashflow</p>
            </Link>
          </li>
        </ul>
      </div>
      <div className="user-container">
        {/*<button className="base-currency">USD <img src={arrow} alt="arrow"/></button>*/}
        <BaseCurrencyDropDownList baseSymbol={baseSymbol}/>
        <a className="nav-link" href="#">
          <svg
            width="18"
            height="20"
            viewBox="0 0 18 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M15.7071 6.79633C15.7071 8.05226 16.039 8.79253 16.7695 9.64559C17.3231 10.2741 17.5 11.0808 17.5 11.956C17.5 12.8302 17.2128 13.6601 16.6373 14.3339C15.884 15.1417 14.8215 15.6573 13.7372 15.747C12.1659 15.8809 10.5937 15.9937 9.0005 15.9937C7.40634 15.9937 5.83505 15.9263 4.26375 15.747C3.17846 15.6573 2.11602 15.1417 1.36367 14.3339C0.78822 13.6601 0.5 12.8302 0.5 11.956C0.5 11.0808 0.677901 10.2741 1.23049 9.64559C1.98384 8.79253 2.29392 8.05226 2.29392 6.79633V6.3703C2.29392 4.68834 2.71333 3.58852 3.577 2.51186C4.86106 0.941697 6.91935 0 8.95577 0H9.04522C11.1254 0 13.2502 0.987019 14.5125 2.62466C15.3314 3.67916 15.7071 4.73265 15.7071 6.3703V6.79633ZM6.07367 18.0608C6.07367 17.5573 6.53582 17.3266 6.96318 17.2279C7.46309 17.1222 10.5093 17.1222 11.0092 17.2279C11.4366 17.3266 11.8987 17.5573 11.8987 18.0608C11.8738 18.5402 11.5926 18.9653 11.204 19.2352C10.7001 19.628 10.1088 19.8767 9.49057 19.9664C9.14868 20.0107 8.81276 20.0117 8.48279 19.9664C7.86362 19.8767 7.27227 19.628 6.76938 19.2342C6.37978 18.9653 6.09852 18.5402 6.07367 18.0608Z"
              fill="#B0B7C3"
            />
          </svg>
        </a>
        <a className="nav-link" href="#">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M18.47 16.83L18.86 19.99C18.96 20.82 18.07 21.4 17.36 20.97L13.9 18.91C13.66 18.77 13.6 18.47 13.73 18.23C14.23 17.31 14.5 16.27 14.5 15.23C14.5 11.57 11.36 8.59 7.50002 8.59C6.71002 8.59 5.94002 8.71 5.22002 8.95C4.85002 9.07 4.49002 8.73 4.58002 8.35C5.49002 4.71 8.99002 2 13.17 2C18.05 2 22 5.69 22 10.24C22 12.94 20.61 15.33 18.47 16.83Z"
              fill="#B0B7C3"
            />
            <path
              d="M13 15.23C13 16.42 12.56 17.52 11.82 18.39C10.83 19.59 9.26 20.36 7.5 20.36L4.89 21.91C4.45 22.18 3.89 21.81 3.95 21.3L4.2 19.33C2.86 18.4 2 16.91 2 15.23C2 13.47 2.94 11.92 4.38 11C5.27 10.42 6.34 10.09 7.5 10.09C10.54 10.09 13 12.39 13 15.23Z"
              fill="#B0B7C3"
            />
          </svg>
        </a>
        <a className="nav-link" href="#">
          <svg
            width="28"
            height="28"
            viewBox="0 0 28 28"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              opacity="0.3"
              d="M8.16663 4.66667H5.83329C5.18896 4.66667 4.66663 5.189 4.66663 5.83333V8.16667C4.66663 8.811 5.18896 9.33333 5.83329 9.33333H8.16663C8.81096 9.33333 9.33329 8.811 9.33329 8.16667V5.83333C9.33329 5.189 8.81096 4.66667 8.16663 4.66667Z"
              fill="#B0B7C3"
            />
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M5.83329 11.6667H8.16663C8.81096 11.6667 9.33329 12.189 9.33329 12.8333V15.1667C9.33329 15.811 8.81096 16.3333 8.16663 16.3333H5.83329C5.18896 16.3333 4.66663 15.811 4.66663 15.1667V12.8333C4.66663 12.189 5.18896 11.6667 5.83329 11.6667ZM12.8333 4.66667H15.1666C15.811 4.66667 16.3333 5.189 16.3333 5.83333V8.16667C16.3333 8.811 15.811 9.33333 15.1666 9.33333H12.8333C12.189 9.33333 11.6666 8.811 11.6666 8.16667V5.83333C11.6666 5.189 12.189 4.66667 12.8333 4.66667ZM12.8333 11.6667H15.1666C15.811 11.6667 16.3333 12.189 16.3333 12.8333V15.1667C16.3333 15.811 15.811 16.3333 15.1666 16.3333H12.8333C12.189 16.3333 11.6666 15.811 11.6666 15.1667V12.8333C11.6666 12.189 12.189 11.6667 12.8333 11.6667ZM19.8333 4.66667H22.1666C22.811 4.66667 23.3333 5.189 23.3333 5.83333V8.16667C23.3333 8.811 22.811 9.33333 22.1666 9.33333H19.8333C19.189 9.33333 18.6666 8.811 18.6666 8.16667V5.83333C18.6666 5.189 19.189 4.66667 19.8333 4.66667ZM19.8333 11.6667H22.1666C22.811 11.6667 23.3333 12.189 23.3333 12.8333V15.1667C23.3333 15.811 22.811 16.3333 22.1666 16.3333H19.8333C19.189 16.3333 18.6666 15.811 18.6666 15.1667V12.8333C18.6666 12.189 19.189 11.6667 19.8333 11.6667ZM5.83329 18.6667H8.16663C8.81096 18.6667 9.33329 19.189 9.33329 19.8333V22.1667C9.33329 22.811 8.81096 23.3333 8.16663 23.3333H5.83329C5.18896 23.3333 4.66663 22.811 4.66663 22.1667V19.8333C4.66663 19.189 5.18896 18.6667 5.83329 18.6667ZM12.8333 18.6667H15.1666C15.811 18.6667 16.3333 19.189 16.3333 19.8333V22.1667C16.3333 22.811 15.811 23.3333 15.1666 23.3333H12.8333C12.189 23.3333 11.6666 22.811 11.6666 22.1667V19.8333C11.6666 19.189 12.189 18.6667 12.8333 18.6667ZM19.8333 18.6667H22.1666C22.811 18.6667 23.3333 19.189 23.3333 19.8333V22.1667C23.3333 22.811 22.811 23.3333 22.1666 23.3333H19.8333C19.189 23.3333 18.6666 22.811 18.6666 22.1667V19.8333C18.6666 19.189 19.189 18.6667 19.8333 18.6667Z"
              fill="#B0B7C3"
            />
          </svg>
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
                    <LogOutButton/>
                  </Fragment>
                }
              >
                <Button onClick={handleTooltipOpen}>
                  <img src={arrow_down} alt="user_menu"/>
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
