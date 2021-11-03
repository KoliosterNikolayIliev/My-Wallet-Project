import React, { useState, useEffect } from "react";
import ReactModal from "react-modal";
import QuizComponent from "./QuizComponent";
import cross from "../images/cross.svg";
import CongratulateComponent from "./CongratulateComponent";

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
    await fetch("https://server.jointrivial.com/save-form-data", {
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
    setQuizState(1);
  };

  // send answers to database
  const sendAnswers = () => {
    setQuizState(1);
    setAnswerSheet([]);
    sendData();
    clearFields();
    // closeModal();
    setQuizState(4);
  };
  const statusMessage = {
    success: "Thanks for subscribing!",
    error: "Invalid email",
    sending: "Sending...",
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
        <input
          type="email"
          value={email}
          placeholder={
            status === null ? "Your email..." : statusMessage[status]
          }
          onChange={(e) => setEmail(e.target.value)}
        />
        <input className="get-early-access-btn" type="submit" value="Get early access" />
      </form>
      <p style={{ display: "block" }}>
        {status === "sending" && <span>Sending...</span>}
        {status === "error" && (
          <span style={{ color: "#7000ff" }}>Already subscribed or Invalid email !</span>
        )}
        {/*{status === "success" && <span>Thanks for subscribing!</span>}*/}
      </p>

      <ReactModal
        isOpen={modalIsOpen}
        // onRequestClose={closeModal}
        className="Modal"
        overlayClassName="Overlay"
        contentLabel="Example Modal"
        ariaHideApp={false}
      >
        {quizState !== 4 ? (
          <div className="heading-text">
            <span className="modalHeading">Thank you for subscribing!</span>
            <button className="modal-close-button" onClick={closeModal}>
              <img alt={"missing"} src={cross} />
            </button>

            <p className="sub-heading">
              We would really appreciate it if you answered a few questions that
              can help us with the development of the platform.
            </p>
            <div className="modal-border-container">
              <span className="purple-modal-border" />
              <span
                className={
                  quizState > 1 ? "purple-modal-border" : "grey-modal-border"
                }
              />
              <span
                className={
                  quizState > 2 ? "purple-modal-border" : "grey-modal-border"
                }
              />
              <span className="grey-modal-border" />
            </div>
          </div>
        ) : (
          <button className="modal-close-button" onClick={closeModal}>
            <img alt={"missing"} src={cross} />
          </button>
        )}

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
        {quizState === 4 && <CongratulateComponent />}

        {/* <button onClick={sendAnswers}>Submit answers</button>
        <button onClick={closeModal}>I don't want to answer</button> */}
      </ReactModal>
    </article>
  );
};

export default EarlyAccessForm;
