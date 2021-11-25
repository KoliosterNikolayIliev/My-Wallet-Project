import {useAuth0} from "@auth0/auth0-react";
import {getAccessToken} from "../../utils/account";
import React from "react";

const AddYodleeComponent = () => {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();
  const addYodleeSource = async () => {
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
          console.log(data);
        },
        onError: (error) => {
          console.log(error);
        },
      },
      "container-fastlink"
    );
  };
  return (
    <div id="container-fastlink">
      <button onClick={() => addYodleeSource()}>Add source</button>
    </div>
  )
}


export default AddYodleeComponent