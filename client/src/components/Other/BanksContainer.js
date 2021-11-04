import { useAuth0 } from "@auth0/auth0-react";
import { linkAccount } from "../../utils/nordigen";

export const BanksContainer = ({ data }) => {
  const { getAccessTokenSilently } = useAuth0();

  const addBankAccount = async (id) => {
    const token = await getAccessTokenSilently();
    const redirect = await linkAccount(token, id);

    window.location.href = redirect.confirmation_link;
  };

  if (data === []) return null;

  return (
    <div>
      <div className="banks-container">
        {data.map((bank) => {
          return (
            <div>
              <p onClick={() => addBankAccount(bank.id)}>{bank.name}</p>
              <img src={bank.logo} width={100} />
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default BanksContainer;
