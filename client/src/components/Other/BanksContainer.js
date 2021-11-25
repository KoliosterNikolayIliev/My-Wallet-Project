import {useAuth0} from "@auth0/auth0-react";
import {linkAccount} from "../../utils/nordigen";
import "../../styles/banks-container-grid.scss"

function InfoIcon() {
  return null;
}

export const BanksContainer = ({data}) => {
  console.log(data)
  const {getAccessTokenSilently} = useAuth0();

  const addBankAccount = async (id) => {
    const token = await getAccessTokenSilently();
    const redirect = await linkAccount(token, id);
    window.sessionStorage.clear();
    window.location.href = redirect.confirmation_link;
  };

  if (data === []) return null;
  return (
    <div className={'bank-container'}>
      {data.map((item) => (
        <div className={'bank-item'} onClick={() => addBankAccount(item.id)}>
          <img style={{marginLeft: '10%'}} width={40}
            src={`${item.logo}?w=248&fit=crop&auto=format`}
            srcSet={`${item.logo}?w=248&fit=crop&auto=format&dpr=2 2x`}
          />
          <span className={'bank-name'}>{item.name}</span>
        </div>
      ))}
    </div>
  );
};

export default BanksContainer;
