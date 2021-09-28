import { useState, useEffect } from "react";

// custom form to use with MailChimpFormContainer
const EarlyAccessForm = ({ status, message, onSubmitted }) => {
  const [email, setEmail] = useState("");

  useEffect(() => {
    if (status === "success") clearFields();
  }, [status]);

  const clearFields = () => {
    setEmail("");
  };

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
      {status === "sending" && <div>Sending...</div>}
      {status === "error" && <div>Invalid email</div>}
      {status === "success" && <div>Thanks for subscribing!</div>}
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
