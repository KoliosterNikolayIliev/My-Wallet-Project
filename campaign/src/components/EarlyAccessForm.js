import { useState, useEffect } from "react";

// custom form to use with MailChimpFormContainer
const EarlyAccessForm = ({ status, message, onSubmitted }) => {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    email &&
      email.indexOf("@") > -1 &&
      onSubmitted({
        EMAIL: email,
      });
  };

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <input
        type="email"
        value={email}
        placeholder="Your email..."
        onChange={(e) => setEmail(e.target.value)}
      />
      <input type="submit" value="Get early access" />
    </form>
  );
};

export default EarlyAccessForm;
