import {Menu, MenuItem} from "@mui/material";
import '../../styles/main_content.scss'

const AddNewSourceMenu = ({openMenuFunc, openBool, anchorEl, closeMenuFunc, modalFunc}) => {
  return (
    <div style={{display: 'inline'}}>
      <button className='add-new-source' onClick={openMenuFunc}>+ Add new source</button>
      <Menu open={openBool} onClose={closeMenuFunc} anchorEl={anchorEl}>
        <MenuItem onClick={() => modalFunc('banks')}>
          Banks
        </MenuItem>

        <MenuItem onClick={() => modalFunc('brokers')}>
          Brokers
        </MenuItem>

        <MenuItem onClick={() => modalFunc('crypto')}>
          Crypto
        </MenuItem>

        <MenuItem onClick={() => modalFunc('custom entry')}>
          Custom Entry
        </MenuItem>
      </Menu>
    </div>
  );
}

export default AddNewSourceMenu;
