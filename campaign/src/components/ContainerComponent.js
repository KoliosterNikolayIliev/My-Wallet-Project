import React from "react";

const ContainerComponent = ({
  imagePath,
  paragraphOne,
  paragraphTwo,
  subtitle,
}) => {
  return (
    <article>
      <div class="container">
        <div class="row">
          <div class="col-sm-6">
            <div class="sub-title">{subtitle}</div>
            <span class="more-info">
              <p>{paragraphOne}</p>
              <p>{paragraphTwo}</p>
            </span>
          </div>

          <div class="col-sm-2">
            <img src={imagePath} alt="Marketing"></img>
          </div>
        </div>
      </div>
    </article>
  );
};

export default ContainerComponent;
