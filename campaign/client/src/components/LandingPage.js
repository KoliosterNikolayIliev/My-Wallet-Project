import React from "react";
import MailchimpFormContainer from "./MailChimpFormContainer";
import ContainerComponent from "./ContainerComponent";
import FooterComponent from "./FooterComponent";
import HeaderComponent from "./HeaderComponent";
import TopBodyComponent from "./TopBodyComponent";
import MessageComponent from "./MessageComponent";

const LandingPage = () => {
  return (
    <main>
      <HeaderComponent />

      <TopBodyComponent />

      <div class="subsc-form">
        <MailchimpFormContainer />
      </div>

      <MessageComponent />

      <div class="main-content">
        <ContainerComponent
          subtitle="Seamless live feed from all your accounts"
          paragraphOne="No more manual inputs. Connect to your bank, stock brokerage and crypto platforms once and get live updates with the latest state of your portfolio."
          imagePath="/images/img-2.jpg"
        />

        <ContainerComponent
          subtitle="Secure, Private, Yours"
          paragraphOne="Trivial will never sell or use your financial data for advertising. Your accounts and data are private, protected and encrypted at rest and in transit."
          imagePath="/images/img-3.jpg"
        />

        <ContainerComponent
          subtitle="Unlock the power of your data"
          paragraphOne="With all your financial data in one place, you can make better decisions to achieve your wealth goals. We will continue bringing features to help you reach financial milestones quicker, safer and smoother."
          imagePath="/images/img-2.jpg"
        />
      </div>

      <div>
        <MailchimpFormContainer />
      </div>

      <FooterComponent />
    </main>
  );
};

export default LandingPage;
