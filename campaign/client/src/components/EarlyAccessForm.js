import { useState, useEffect } from "react";
import ReactModal from "react-modal";
import QuizComponent from "./QuizComponent";

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
  const [quizState, setQuizState] = useState(1);
  const [answerSheet, setAnswerSheet] = useState([]);

  const sendData = async () => {
    let data = {
      author: email,
      quiz: answerSheet,
    };
    await fetch("http://localhost:5000/save-form-data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
  };

  const openModal = () => {
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  // send answers to database
  const sendAnswers = () => {
    setQuizState(1);
    setAnswerSheet([]);
    sendData();
    clearFields();
    closeModal();
  };

  useEffect(() => {
    if (status === "success") {
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
        {quizState === 1 && (
          <QuizComponent
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={"How do you plan to use this platform?"}
            answer1={"I plan to use the platform this way"}
            answer2={"I plan to use the platform another way"}
            answer3={"I plan to use the platform a third way"}
          />
        )}

        {quizState === 2 && (
          <QuizComponent
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={"How do you plan to use this platform ....?"}
            answer1={"I plan to use the platform this way"}
            answer2={"I plan to use the platform another way"}
            answer3={"I plan to use the platform a third way"}
          />
        )}

        {quizState === 3 && (
          <QuizComponent
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={"How do you plan to use this platform !!!!?"}
            answer1={"I plan to use the platform this way"}
            answer2={"I plan to use the platform another way"}
            answer3={"I plan to use the platform a third way"}
          />
        )}

        {/* <button onClick={sendAnswers}>Submit answers</button>
        <button onClick={closeModal}>I don't want to answer</button> */}
      </ReactModal>
    </div>
  );
};

export default EarlyAccessForm;
