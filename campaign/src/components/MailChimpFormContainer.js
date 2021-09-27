import MailchimpSubscribe from "react-mailchimp-subscribe";
import EarlyAccessForm from "./EarlyAccessForm";

const MailchimpFormContainer = (props) => {
  const postUrl = `https://gmail.us5.list-manage.com/subscribe/post?u=8ae517b7914a1084896fca77c&id=f2cc0739a0`;

  return (
    <div className="mc__form-container">
      <MailchimpSubscribe
        url={postUrl}
        render={({ subscribe, status, message }) => (
          <EarlyAccessForm
            status={status}
            message={message}
            onValidated={(formData) => subscribe(formData)}
          />
        )}
      />
    </div>
  );
};

export default MailchimpFormContainer;
