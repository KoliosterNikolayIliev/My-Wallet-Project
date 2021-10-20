import React from "react";

const MessageComponent = ({ counter }) => {
  return (
    <article>
      <div className="message">
        <p>
          Join the <span className="purple">{counter}</span> people that have signed up
          for our early January launch.
        </p>
        <p>
          Only <span className="purple">5.000</span> spots available!
        </p>
      </div>
    </article>
  );
};

export default MessageComponent;
