import React from "react";

const MessageComponent = ({ counter }) => {
    
  return (

      <div className="message">
        <p>
          Join the <span className="purple">{counter}</span> people that have signed up
          for our early January launch. Only <span className="purple">5.000</span> spots available!
        </p>
      </div>
  );
};

export default MessageComponent;
