import { useState } from "react";

// custom form to use with MailChimpFormContainer
const EarlyAccessForm = ({ status, message, onValidated }) => {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    email &&
      onValidated({
        b_email: email,
      });
  };

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <input type="email" placeholder="Your email..." onChange={setEmail} />
      <input type="submit" value="Get early access" />
    </form>
  );
};

export default EarlyAccessForm;
