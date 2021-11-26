import React, {Fragment, useState} from 'react';
import {Menu, MenuItem} from "@mui/material";

const AddNewSourceMenu = ({openMenuFunc, openBool, anchorEl, closeMenuFunc, modalFunc}) => {
  return (
    <Fragment>
      <button onClick={openMenuFunc}>Add new source</button>
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
    </Fragment>
  );
}

export default AddNewSourceMenu;
