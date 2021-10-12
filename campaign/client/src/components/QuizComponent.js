import React from "react";
import { useState } from "react";

const QuizComponent = ({
  questionType,
  quizState,
  setQuizState,
  answerSheet,
  setAnswerSheet,
  submitFunction,
  question,
  answer1,
  answer2,
  answer3,
}) => {
  const [answerSelected, setAnswerSelected] = useState(null);

  const selectAnswer = (e) => {
    // remove the selected class from all sibling elements
    e.target.parentElement.childNodes.forEach((node) => {
      node.classList.remove("selected");
    });

    // add the selected class to the selected answer
    e.target.classList.add("selected");

    // add the selected answer to the answer sheet
    if (e.target.type === "text") {
      setAnswerSheet({
        ...answerSheet,
        [question]: e.target.value,
      });
    } else {
      setAnswerSheet({
        ...answerSheet,
        [question]: e.target.innerText,
      });
    }

    setAnswerSelected(true);
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
      <input type="text" onChange={selectAnswer} />

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
