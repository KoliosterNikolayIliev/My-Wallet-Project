import React from "react";
import { useState } from "react";

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
  const [answerNumber, setAnswerNumber] = useState(1);
  const selectAnswer = (e) => {
    if (numberOfAnswers) {
      // remove the selected class from all sibling elements
      e.target.parentElement.childNodes.forEach((node) => {
        node.classList.remove("selected");
      });
    }

    // add the selected class to the selected answer
    e.target.classList.add("selected");

    // add the selected answer to the answer sheet
    if (e.target.type === "text") {
      setAnswerSheet({
        ...answerSheet,
        [question]: {
          [answerNumber]: e.target.value,
        },
      });
      setAnswerNumber(answerNumber + 1);
    } else {
      if (numberOfAnswers) {
        setAnswerSheet({
          ...answerSheet,
          [question]: e.target.innerText,
        });
      } else {
        setAnswerSheet({
          ...answerSheet,
          [question]: {
            [answerNumber]: e.target.innerText,
          },
        });
        setAnswerNumber(answerNumber + 1);
      }
    }

    setAnswerSelected(true);
  };

  // Increment the state of the quiz
  const previousQuizState = () => {
    if (quizState > 1) {
      setQuizState(quizState - 1);
    }
  };

  // Increment the state of the quiz
  const nextQuizState = () => {
    if (quizState < 3) {
      setQuizState(quizState + 1);
    }
  };

  return (
    <div>
      <h4>{question}</h4>
      <p onClick={selectAnswer}>{answer1}</p>
      <p onClick={selectAnswer}>{answer2}</p>
      <p onClick={selectAnswer}>{answer3}</p>
      <p onClick={selectAnswer}>{answer4}</p>
      <input type="text" placeholder={"Other"} onChange={selectAnswer} />

      {/* Show the submit button if this is the last question in the quiz */}
      {answerSelected && quizState === 3 && (
        <div>
          <button onClick={submitFunction}>Submit</button>
        </div>
      )}

      {answerSelected && quizState !== 3 && (
        <div>
          {quizState > 1 && <button onClick={previousQuizState}>Back</button>}
          <button onClick={nextQuizState}>Next</button>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
