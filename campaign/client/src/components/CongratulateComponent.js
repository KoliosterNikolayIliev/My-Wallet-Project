import React from "react";
import Logo from "../images/Logo.svg";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faTwitter} from "@fortawesome/free-brands-svg-icons";

const CongratulateComponent = () => {
    return (
        <div className="end-questionnaire-container">
            <div className="modal-close">
                <img src={Logo} alt=""/>
            </div>
            <h4 className="modalHeading">Thanks for supporting us!</h4>
            <p className="reminder">Don’t forget to tell your friends and keep your eyes peeled for the
                launch! 🚀</p>
            <button className="follow-btn">
                <FontAwesomeIcon className="twitter-button" icon={faTwitter} size="1x" inverse/>
                Follow us on Twitter
            </button>
        </div>
    );
};

export default CongratulateComponent;