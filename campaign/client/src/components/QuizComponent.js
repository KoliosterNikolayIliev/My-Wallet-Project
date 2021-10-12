import React from "react";
import { useState, useEffect } from "react";

const QuizComponent = ({
  questionType,
  numberOfAnswers,
  quizState,
  setQuizState,
  answerSheet,
  setAnswerSheet,
  submitFunction,
  question,
  answer1,
  answer2,
  answer3,
  answer4,
}) => {
  const [answerSelected, setAnswerSelected] = useState(null);
  const [answer, setAnswer] = useState([]);

  useEffect(() => {
    setAnswerSheet({ ...answerSheet, [question]: answer });
    return console.log(answerSheet);
  }, [answer]);

  const selectAnswer = (e) => {
    if (numberOfAnswers) {
      // remove the selected class from all sibling elements
      e.target.parentElement.childNodes.forEach((node) => {
        node.classList.remove("selected");
      });
    }

    // add the selected class to the selected answer
    e.target.classList.add("selected");

    if (numberOfAnswers) {
      setAnswer([e.target.innerText]);
    } else {
      if (e.target.type === "text") {
        setAnswer([...answer, e.target.value]);
      } else {
        setAnswer([...answer, e.target.innerText]);
      }
    }

    setAnswerSelected(true);
  };

  // Increment the state of the quiz
  const nextQuizState = () => {
    if (quizState < 3) {
      setQuizState(quizState + 1);
    }
  };

  if (questionType === "closed")
    return (
      <div>
        <h4>{question}</h4>
        <p onClick={selectAnswer}>{answer1}</p>
        <p onClick={selectAnswer}>{answer2}</p>
        <p onClick={selectAnswer}>{answer3}</p>
        <p onClick={selectAnswer}>{answer4}</p>
        <input type="text" placeholder="Other" onBlur={selectAnswer} />

        {/* Show the submit button if this is the last question in the quiz */}
        {quizState === 3 && (
          <div>
            <button onClick={submitFunction}>Submit</button>
          </div>
        )}

        {answerSelected && quizState !== 3 && (
          <div>
            <button onClick={nextQuizState}>Next</button>
          </div>
        )}
      </div>
    );
  else if (questionType === "open")
    return (
      <div>
        <h4>{question}</h4>
        <input type="text" placeholder="Other" onBlur={selectAnswer} />

        {/* Show the submit button if this is the last question in the quiz */}
        {answerSelected && quizState === 3 && (
          <div>
            <button onClick={submitFunction}>Submit</button>
          </div>
        )}

        {answerSelected && quizState !== 3 && (
          <div>
            <button onClick={nextQuizState}>Next</button>
          </div>
        )}
      </div>
    );
};

export default QuizComponent;
