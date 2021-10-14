import React from "react";

const MessageComponent = ({ counter }) => {
  return (
    <article class="message">
      <p>
        Join the <strong>{counter}</strong> people that have signed up for our
        early January launch.
      </p>
      <p>Only 5.000 spots available!</p>
    </article>
  );
};

export default MessageComponent;
