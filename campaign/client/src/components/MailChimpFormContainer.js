import MailchimpSubscribe from "react-mailchimp-subscribe";
import EarlyAccessForm from "./EarlyAccessForm";

const MailchimpFormContainer = (props) => {
  const postUrl = `https://gmail.us5.list-manage.com/subscribe/post?u=8ae517b7914a1084896fca77c&id=f2cc0739a0`;

  return (
    <MailchimpSubscribe
      url={postUrl}
      render={({ subscribe, status, message }) => (
        <div class="subscribe">
          <EarlyAccessForm
            status={status}
            message={message}
            onSubmitted={(formData) => subscribe(formData)}
          />
        </div>
      )}
    />
  );
};

export default MailchimpFormContainer;
