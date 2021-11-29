import {ListItemIcon, Menu, MenuItem} from "@mui/material";
import '../../styles/main_content.scss'
import '../../styles/add-source-menu.scss'

const AddNewSourceMenu = ({openMenuFunc, openBool, anchorEl, closeMenuFunc, modalFunc}) => {
  return (
    <div style={{display: 'inline'}}>
      <button className='add-new-source' onClick={openMenuFunc}>+ Add new source</button>
      <Menu open={openBool} onClose={closeMenuFunc} anchorEl={anchorEl}>
        <MenuItem onClick={() => modalFunc('banks')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-envelope-open-dollar icon"></i>
          </ListItemIcon>
          Banks
        </MenuItem>

        <MenuItem onClick={() => modalFunc('brokers')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-envelope-open-dollar icon"></i>
          </ListItemIcon>
          Brokers
        </MenuItem>

        <MenuItem onClick={() => modalFunc('crypto')}>
          <ListItemIcon className='icon-container'>
            <i className="fab fa-bitcoin icon"></i>
          </ListItemIcon>
          Crypto
        </MenuItem>

        <MenuItem onClick={() => modalFunc('custom entry')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-plus-circle icon"></i>
          </ListItemIcon>
          Custom Entry
        </MenuItem>
      </Menu>
    </div>
  );
}

export default AddNewSourceMenu;
