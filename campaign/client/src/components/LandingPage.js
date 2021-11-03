import ContainerComponent from "./ContainerComponent";
import FooterComponent from "./FooterComponent";
import HeaderComponent from "./HeaderComponent";
import TopBodyComponent from "./TopBodyComponent";
import MailchimpFormContainer from "./MailChimpFormContainer";
import imageOne from "../images/image1.png"
import imageTwo from "../images/image2.png"
import imageThree from "../images/image3.png"

const LandingPage = () => {


    return (
        <main>
            <HeaderComponent/>
            <div className="section-content">
                <TopBodyComponent show={true}/>
            </div>
            <div className="section-content body-section">
                <ContainerComponent
                    subtitle="Seamless live feed from all your accounts"
                    paragraphOne="No more manual inputs. Connect to your bank, stock brokerage and crypto platforms once and get live updates with the latest state of your portfolio."
                    image={imageOne}
                    articleClasses="section-content-text-and-image reversed "
                    imageClass="left-image"
                />
            </div>
            <div className="section-content body-section">
                <ContainerComponent
                    subtitle="Secure, Private, Yours"
                    paragraphOne="Trivial will never sell or use your financial data for advertising. Your accounts and data are private, protected and encrypted at rest and in transit."
                    image={imageTwo}
                    articleClasses="section-content-text-and-image non-reversed"
                    imageClass="right-image"
                />
            </div>
            <div className="section-content body-section">
                <ContainerComponent
                    subtitle="Unlock the power of your data"
                    paragraphOne="With all your financial data in one place, you can make better decisions to achieve your wealth goals. We will continue bringing features to help you reach financial milestones quicker, safer and smoother."
                    image={imageThree}
                    articleClasses="section-content-text-and-image reversed "
                    imageClass="left-image"
                />
            </div>
            <div className="last-subscription">
                <MailchimpFormContainer show={false}/>
            </div>


            <FooterComponent/>
        </main>
    );
};

export default LandingPage;
