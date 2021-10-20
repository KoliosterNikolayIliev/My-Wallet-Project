import React from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faInstagram} from '@fortawesome/free-brands-svg-icons'
import {faTwitter} from '@fortawesome/free-brands-svg-icons'
import {faFacebook} from '@fortawesome/free-brands-svg-icons'

const FooterComponent = () => {
    return (
        <article>
            <div className="footer">
                <div className="footer-content">
                    <span>© 2021 Trivial. All rights reserved</span>
                    <ul className="fa-icons">
                        <li>
                            <a href="#"><FontAwesomeIcon icon={faInstagram} size="1x" inverse/></a>
                        </li>
                        <li>
                            <a href="#"><FontAwesomeIcon icon={faTwitter} size="1x" inverse/></a>
                        </li>
                        <li>
                            <a href="#"><FontAwesomeIcon icon={faFacebook} size="1x" inverse/></a>
                        </li>
                    </ul>
                </div>
            </div>
        </article>
    );
};

export default FooterComponent;
