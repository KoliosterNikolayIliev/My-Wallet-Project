import React, {useState} from 'react';
import {Menu, MenuItem} from "@mui/material";

const AddNewSourceMenu = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl)
  const openMenu = (event) => {
    setAnchorEl(event.currentTarget)
  }

  const closeMenu = () => {
    setAnchorEl(null);
  }

  return (
    <div>
      <button onClick={openMenu}>Add new source</button>
      <Menu open={open} onClose={closeMenu} anchorEl={anchorEl}>
        <MenuItem>
          Banks
        </MenuItem>

        <MenuItem>
          Crypto
        </MenuItem>

        <MenuItem>
          Custom Entry
        </MenuItem>
      </Menu>
    </div>
  );
}

export default AddNewSourceMenu;
