import React, {useState} from 'react';
import {Menu, MenuItem} from "@mui/material";

const AddNewSourceMenu = ({openMenuFunc, openBul, anchorEl, closeMenuFunc, modalFunc}) => {
  return (
    <div>
      <button onClick={openMenuFunc}>Add new source</button>
      <Menu open={openBul} onClose={closeMenuFunc} anchorEl={anchorEl}>
        <MenuItem onClick={modalFunc}>
          Banks
        </MenuItem>

        <MenuItem onClick={modalFunc}>
          Crypto
        </MenuItem>

        <MenuItem onClick={modalFunc}>
          Custom Entry
        </MenuItem>
      </Menu>
    </div>
  );
}

export default AddNewSourceMenu;
