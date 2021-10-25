import React from "react";
import arrow from "../images/Vector.svg"

const ContainerComponent = ({ image, paragraphOne, subtitle, articleClasses, imageClass}) => {
  return (
    <article className={articleClasses}>
      <div className="section-text">
        <div className="sub-title">{subtitle}</div>
        <span className="more-info">
          <p>{paragraphOne}</p>
        </span>
        <div className="start">
          <a id="get-started" href="#get-early-access">Get started <img style={{marginLeft:5}} src={arrow} alt=""/></a>
        </div>
      </div>

      <div className={imageClass}>
        <img className="marketing-image" src={image} alt="Marketing"/>
      </div>
    </article>
  );
};

export default ContainerComponent;
