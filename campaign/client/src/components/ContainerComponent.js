import React from "react";

const ContainerComponent = ({ imagePath, paragraphOne, subtitle }) => {
  return (
    <article>
      <div className="col-sm-6">
        <div className="sub-title">{subtitle}</div>
        <span className="more-info">
          <p>{paragraphOne}</p>
        </span>
        <div className="start">
          <a href="#">Get started -- </a>
        </div>
      </div>

      <div className="col-sm-2">
        <img src={imagePath} alt="Marketing"/>
      </div>
    </article>
  );
};

export default ContainerComponent;
