import {getAccessToken} from "./account";

const deleteYodleeAccount = async (token, account_id) => {
  const yodleeToken = await getAccessToken(token);
  const response = await fetch(
    `https://development.api.yodlee.uk/ysl/accounts/${account_id}`, {
      method: "DELETE",
      headers: {
        'Api-Version': 1.1,
        Authorization: `Bearer ${yodleeToken}`,
      },
    }
  );
  return response
}

export default deleteYodleeAccount