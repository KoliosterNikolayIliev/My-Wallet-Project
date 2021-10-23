import React from "react";
import circle from "../images/top-body-img.png"
import MailchimpFormContainer from "./MailChimpFormContainer";

const TopBodyComponent = ({show}) => {
    return (
        <div className="section-content-text-and-image">
            <div className="section-text">
                <h1>Unleash your wealth</h1>
                <p id="get_early_access">
                    New-age wealth builders constantly juggle with multiple investment
                    platforms. Making sense of the big picture is arduous when it really
                    shouldn’t be.
                </p>
                <p>
                    We bring seamless order to your wealth so you can spend more time
                    growing it.
                </p>
                <MailchimpFormContainer show/>
            </div>
            <div className="section-content-image">
                <img src={circle} alt="circle"/>
            </div>
        </div>
    );
};

export default TopBodyComponent;
