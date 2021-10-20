import React from "react";
import circle from "../images/Screenshot from 2021-10-20 13-31-42.png"

const TopBodyComponent = () => {
  return (
    <article>
      <div className="top-body">
        <div className="top-body-text">
          <h1>Unleash your wealth</h1>
          <p>
            New-age wealth builders constantly juggle with multiple investment
            platforms. Making sense of the big picture is arduous when it really
            shouldn’t be.
          </p>
          <p>
            We bring seamless order to your wealth so you can spend more time
            growing it.
          </p>
        </div>

        <div className="top-body-image">
          <img src={circle} alt="circle"/>
        </div>
      </div>
    </article>
  );
};

export default TopBodyComponent;
