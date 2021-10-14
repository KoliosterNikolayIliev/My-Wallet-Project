import React from "react";

const HeaderComponent = () => {
  return (
    <header>
      <div class="top-navigation">

        <div class="logo">
        <img src="/images/logo.png">
      </img>
        </div>

        <div className="top-nav-menu">
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Features</a></li>
            <li><a href="#">Contact</a></li>
          </ul>

          <div class="top-nav-btn">
          Get early access
          </div>

        </div>


      </div>

      <div class="header">
        <div class="header-text">
        <h1>Unleash your wealth</h1>
        <p>
        New-age wealth builders constantly juggle with multiple investment 
        platforms. Making sense of the big picture is arduous when it really 
        shouldn’t be.
        </p>
        <p>We bring seamless order to your wealth so you can spend more time growing it.</p>
        </div>

      <div class="header-image">
          <img src="/images/img-1.jpg">
      </img>
      </div>
      </div>

    </header>
  );
};

export default HeaderComponent;
