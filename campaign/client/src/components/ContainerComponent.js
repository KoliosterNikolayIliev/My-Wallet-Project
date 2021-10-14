import React from "react";

const ContainerComponent = ({
  imagePath,
  paragraphOne,
  paragraphTwo,
  subtitle,
}) => {
  return (
    <article>
          <div class="col-sm-6">
            <div class="sub-title">{subtitle}</div>
            <span class="more-info">
              <p>{paragraphOne}</p>
            </span>
            <div class="start"><a href="#">Get started -- </a>
              </div>
          </div>

          <div class="col-sm-2">
            <img src={imagePath} alt="Marketing"></img>
          </div>

    </article>
  );
};

export default ContainerComponent;
