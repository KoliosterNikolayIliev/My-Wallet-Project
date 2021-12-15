import { useAuth0 } from "@auth0/auth0-react";
import { getAccessToken } from "../../utils/account";
import React, {useEffect, useState} from "react";
import Loader from "./LoaderComponent";

const AddYodleeComponent = () => {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  const [loading, setLoading] = useState(false)
  const addYodleeSource = async () => {
    setLoading(true)
    const auth0Token = await getAccessTokenSilently();
    const yodleeToken = await getAccessToken(auth0Token);
    window.fastlink.open(
      {
        fastLinkURL:
          "https://development.node.yodlee.uk/authenticate/UKPre-Prod-203/?channelAppName=ukpreprod",
        accessToken: yodleeToken,
        params: {
          userExperienceFlow: "Aggregation",
        },
        onSuccess: (data) => {
          window.sessionStorage.clear();
        },
        onError: (error) => {
          console.log(error);
        },
      },
      "container-fastlink"
    );
    setLoading(false)
  };

  useEffect(() => {
    addYodleeSource();
  }, []);

  return (
    <div id="container-fastlink">
      {loading === true && <Loader/>}
    </div>
  );
};

export default AddYodleeComponent;
