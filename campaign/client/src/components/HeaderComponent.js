import React from "react";
import Logo from "../images/Logo.svg"

const HeaderComponent = () => {
  return (
    <header>
      <nav>
          <article>
              <img src={Logo} alt="logo"/>
          </article>

          {/* 
          Removed
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">Features</a>
            </li>
            <li>
              <a href="#">Contact</a>
            </li>
          </ul> */}
          <a href="#get_early_access" className="top-nav-btn">Get early access</a>
      </nav>
    </header>
  );
};

export default HeaderComponent;
