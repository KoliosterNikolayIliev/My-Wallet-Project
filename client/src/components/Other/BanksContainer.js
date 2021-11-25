import {useAuth0} from "@auth0/auth0-react";
import {linkAccount} from "../../utils/nordigen";
import {IconButton, ImageList, ImageListItem, ImageListItemBar, ListSubheader} from "@mui/material";
import {Fragment} from "react";

function InfoIcon() {
  return null;
}

export const BanksContainer = ({data}) => {
  const {getAccessTokenSilently} = useAuth0();

  const addBankAccount = async (id) => {
    const token = await getAccessTokenSilently();
    const redirect = await linkAccount(token, id);

    window.location.href = redirect.confirmation_link;
  };

  if (data === []) return null;
  return (
    <ImageList sx={{ width: 500, height: 450 }} cols={3}>
      {data.map((item) => (
        <ImageListItem key={item.logo}>
          <img onClick={() => addBankAccount(item.id)}
            src={`${item.logo}?w=248&fit=crop&auto=format`}
            srcSet={`${item.logo}?w=248&fit=crop&auto=format&dpr=2 2x`}
            alt={item.name}
            loading="lazy"
          />
          <ImageListItemBar
            title={item.name}
          />
        </ImageListItem>
      ))}
    </ImageList>
  );
};

export default BanksContainer;
