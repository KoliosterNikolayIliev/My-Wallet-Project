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

  // update the answer sheet every time the answer state is updated
  useEffect(() => {
    setAnswerSheet({ ...answerSheet, [question]: answer });
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
      // update the answer state if the question has only one answer
      setAnswer([e.target.innerText]);
    } else {
      // update the answer state if the question has more than one answers
      if (e.target.type === "text") {
        setAnswer([...answer, e.target.value]);
      } else {
        setAnswer([...answer, e.target.innerText]);
      }
    }

    setAnswerSelected(true);
  };

  // Decrement the state of the quiz
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

  // render the quiz if the question is closed-answer
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
            <button onClick={previousQuizState}>Back</button>
            <button onClick={submitFunction}>Submit</button>
          </div>
        )}

        {answerSelected && quizState !== 3 && (
          <div>
            {quizState !== 1 && (
              <button onClick={previousQuizState}>Back</button>
            )}
            <button onClick={nextQuizState}>Next</button>
          </div>
        )}
      </div>
    );
  // render the quiz if the question is open-answer
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

        {/* Show the next button if this isn't the last element */}
        {answerSelected && quizState !== 3 && (
          <div>
            <button onClick={nextQuizState}>Next</button>
          </div>
        )}
      </div>
    );
};

export default QuizComponent;
