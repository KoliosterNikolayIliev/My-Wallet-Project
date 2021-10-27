import MailchimpSubscribe from "react-mailchimp-subscribe";
import EarlyAccessForm from "./EarlyAccessForm";
import React, { useEffect, useState } from "react";
import MessageComponent from "./MessageComponent";

const MailchimpFormContainer = ({ show }) => {
  const postUrl = `https://gmail.us5.list-manage.com/subscribe/post?u=f813380dbeb308d67ea08fca7&id=3052096cd5`;
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    fetch("http://localhost:5000/subscribers").then((response) =>
      response.json().then((data) => setCounter(data["count"]))
    );
  }, [counter]);
  return (
    <div className="mail-info">
      <MailchimpSubscribe
        counter={counter}
        setCounter={setCounter}
        url={postUrl}
        render={({ subscribe, status, message }) => (
          <div>
            <EarlyAccessForm
              counter={counter}
              setCounter={setCounter}
              status={status}
              message={message}
              onSubmitted={(formData) => subscribe(formData)}
            />
          </div>
        )}
      />
      {show ? <MessageComponent counter={counter} /> : null}
    </div>
  );
};

export default MailchimpFormContainer;
