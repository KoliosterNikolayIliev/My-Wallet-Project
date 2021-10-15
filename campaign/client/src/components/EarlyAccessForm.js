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
const EarlyAccessForm = ({
  counter,
  setCounter,
  status,
  message,
  onSubmitted,
}) => {
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
    setCounter(counter + 1);
  };

  return (
    <article>
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
            questionType={"closed"}
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={
              "What do you hope Trivial will help you with? (Select all that apply)"
            }
            answer1={"Seeing all my investment accounts in one place"}
            answer2={"Setting clear and meaningful financial goals"}
            answer3={"Making better financial decisions"}
            answer4={"Getting my taxes in order"}
          />
        )}

        {quizState === 2 && (
          <QuizComponent
            questionType={"closed"}
            numberOfAnswers={1}
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={
              "What do you use to solve this problem now? (Select only one option)"
            }
            answer1={"Nothing"}
            answer2={"Spreadsheets"}
            answer3={"I've set up my own API"}
            answer4={"Financial advisor"}
          />
        )}

        {quizState === 3 && (
          <QuizComponent
            questionType={"open"}
            quizState={quizState}
            setQuizState={setQuizState}
            answerSheet={answerSheet}
            setAnswerSheet={setAnswerSheet}
            submitFunction={sendAnswers}
            question={
              "Please list all of the investment platforms you use today?"
            }
          />
        )}

        {/* <button onClick={sendAnswers}>Submit answers</button>
        <button onClick={closeModal}>I don't want to answer</button> */}
      </ReactModal>
    </article>
  );
};

export default EarlyAccessForm;
