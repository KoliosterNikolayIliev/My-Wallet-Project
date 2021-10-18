import React from "react";

const HeaderComponent = () => {
  return (
    <header>
      <article>
        <img src="/images/logo.png" alt="logo"></img>
      </article>
      <nav>
        <div className="top-nav-menu">
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
          <div class="top-nav-btn">Get early access</div>
        </div>
      </nav>
    </header>
  );
};

export default HeaderComponent;
