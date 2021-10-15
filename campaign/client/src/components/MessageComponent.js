import React from "react";

const MessageComponent = ({ counter }) => {
  return (
    <article>
      <div class="message">
        <p>
          Join the <span class="purple">{counter}</span> people that have signed up
          for our early January launch.
        </p>
        <p>
          Only <span class="purple">5.000</span> spots available!
        </p>
      </div>
    </article>
  );
};

export default MessageComponent;
