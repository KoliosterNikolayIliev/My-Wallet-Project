import {ListItemIcon, Menu, MenuItem} from "@mui/material";
import '../../styles/main_content.scss'
import '../../styles/add-source-menu.scss'
import '../../styles/dashboard.scss'


const menuStyles = {
  borderRadius: 25,
  width: 370,
  height: 484,
}

const AddNewSourceMenu = ({openMenuFunc, openBool, anchorEl, closeMenuFunc, modalFunc}) => {
  return (
    <div style={{display: 'inline'}}>
      <button className='add-new-source add-source-font' onClick={openMenuFunc}>+ Add new source</button>
      <Menu PaperProps={{style: menuStyles}} open={openBool} onClose={closeMenuFunc} anchorEl={anchorEl}>
        <div className='menu-item' onClick={() => modalFunc('banks')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-envelope-open-dollar icon"></i>
          </ListItemIcon>
          Banks
        </div>

        <div className='menu-item' onClick={() => modalFunc('brokers')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-envelope-open-dollar icon"></i>
          </ListItemIcon>
          Brokers
        </div>

        <div className='menu-item' onClick={() => modalFunc('crypto')}>
          <ListItemIcon className='icon-container'>
            <i className="fab fa-bitcoin icon"></i>
          </ListItemIcon>
          Crypto
        </div>

        <div className='menu-item' onClick={() => modalFunc('custom entry')}>
          <ListItemIcon className='icon-container'>
            <i className="fas fa-plus-circle icon"></i>
          </ListItemIcon>
          Custom Entry
        </div>
      </Menu>
    </div>
  );
}

export default AddNewSourceMenu;
