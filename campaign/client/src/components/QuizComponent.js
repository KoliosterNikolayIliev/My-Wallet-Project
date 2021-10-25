import React from "react";
import {useState, useEffect} from "react";
import Container from '@material-ui/core/Container';


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
        setAnswerSheet({...answerSheet, [question]: answer});
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
            if (e.target.type === "text" || e.target.type === "textarea") {
                setAnswer([e.target.value]);
                // update the answer state if the question has only one answer
            }else{
                setAnswer([e.target.innerText]);
            }
        } else {
            // update the answer state if the question has more than one answers
            if (e.target.type === "text" || e.target.type === "textarea") {
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
        if (quizState < 4) {
            setQuizState(quizState + 1);
        }
    };

    // render the quiz if the question is closed-answer
    if (questionType === "closed")
        return (
            <Container>
                <div className="question-answer-container">
                    <h4 className="question">{question}</h4>
                    <p className="answer" onClick={selectAnswer}>{answer1}</p>
                    <p className="answer" onClick={selectAnswer}>{answer2}</p>
                    <p className="answer" onClick={selectAnswer}>{answer3}</p>
                    <p className="answer" onClick={selectAnswer}>{answer4}</p>
                    <input className="answer" type="text" placeholder="Other (Please specify):" onMouseOut={selectAnswer}/>

                </div>
                <div className="btn-holder">
                    <button className={quizState !== 1 ? "active-back modal-btn" : "modal-btn back-btn"}
                        disabled={quizState === 1}
                            onClick={previousQuizState}>Back
                    </button>
                    <button className={answerSelected ? "active-next modal-btn" : "modal-btn"} onClick={nextQuizState}
                            disabled={!answerSelected}>Next
                    </button>
                </div>
            </Container>
        );
    // render the quiz if the question is open-answer
    else if (questionType === "open")
        return (
            <Container>
                <div className="question-answer-container">
                    <h4 className="question">{question}</h4>
                    <p className="additional-info">(some examples for the types of platforms: Traditional banks, Neobanks, Stock brokers, Crypto exchanges and others)</p>
                    <textarea className="submit-text-area" placeholder="...." onMouseOut={selectAnswer} onTouchEnd={selectAnswer}/>
                </div>
                <div className="btn-holder">
                    <button className={quizState !== 1 ? "active-back modal-btn" : "modal-btn back-btn"}
                            onClick={previousQuizState}>Back
                    </button>
                    <button className={answerSelected ? "active-next modal-btn" : "modal-btn"}
                            disabled={!answerSelected}
                            onClick={submitFunction}>Finish
                    </button>
                </div>
            </Container>
        );
};

export default QuizComponent;
