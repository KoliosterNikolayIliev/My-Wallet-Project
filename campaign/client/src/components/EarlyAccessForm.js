import { useState, useEffect } from "react";
import ReactModal from "react-modal";

const customStyles = {
  // style the modal here. For example:
  // content: {
  //   top: '50%',
  //   left: '50%',
  //   right: 'auto',
  //   bottom: 'auto',
  //   marginRight: '-50%',
  //   transform: 'translate(-50%, -50%)',
  // },
};

// custom form to use with MailChimpFormContainer
const EarlyAccessForm = ({ status, message, onSubmitted }) => {
  const [email, setEmail] = useState("");
  const [modalIsOpen, setIsOpen] = useState(false);

  const openModal = () => {
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  const sendAnswers = () => {
    closeModal();
    // send answers to database
  };

  useEffect(() => {
    if (status === "success") {
      clearFields();
      openModal();
    }
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
    <div>
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

      <ReactModal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        style={customStyles}
        contentLabel="Example Modal"
      >
        <div>Thank you for subscribing!</div>
        <p>
          We would really appreciate it if you answered a few questions that can
          help us with the development of the platform.
        </p>
        <form>
          <label for="question1">Question 1 (Add a question here)</label>
          <input type="text" id="question1" />
          <br />
          <label for="question2">Question 2 (Add a question here)</label>
          <input type="text" id="question2" />
          <br />
          <label for="question3">Question 3 (Add a question here)</label>
          <input type="text" id="question3" />
        </form>
        <button onClick={sendAnswers}>Submit answers</button>
        <button onClick={closeModal}>I don't want to answer</button>
      </ReactModal>
    </div>
  );
};

export default EarlyAccessForm;
