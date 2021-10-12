import React from "react";
import MailchimpFormContainer from "./MailChimpFormContainer";
import ContainerComponent from "./ContainerComponent";
import FooterComponent from "./FooterComponent";
import HeaderComponent from "./HeaderComponent";
import MessageComponent from "./MessageComponent";

const LandingPage = () => {
  return (
    <main>
      <HeaderComponent />

      <div>
        <MailchimpFormContainer />
      </div>

      <MessageComponent />

      <ContainerComponent
        subtitle="Subititle 1"
        paragraphOne="Paragraph text one"
        paragraphTwo="Paragraph text two"
        imagePath="/images/image-woman.jpg"
      />

      <ContainerComponent
        subtitle="Subititle 2"
        paragraphOne="Paragraph text one"
        paragraphTwo="Paragraph text two"
        imagePath="/images/image-people.jpg"
      />

      <ContainerComponent
        subtitle="Subititle 3"
        paragraphOne="Paragraph text one"
        paragraphTwo="Paragraph text two"
        imagePath="/images/image-woman-second.jpg"
      />

      <div>
        <MailchimpFormContainer />
      </div>

      <FooterComponent />
    </main>
  );
};

export default LandingPage;
