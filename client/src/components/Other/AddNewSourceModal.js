import React from 'react'
import {Box, Modal} from "@mui/material";

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  background: '#FFFFFF',
  border: '2px solid #000',
  width: '30%',
  height: '80%',
}

const AddNewSourceModal = ({openModal, closeModalFunc, source}) => {
    let sources;
    if (source === 'banks') {
      sources = <h1>banks</h1>;
    }else if (source === 'crypto') {
      sources = <h1>crypto</h1>;
    }else {
      sources = <h1>custom entry</h1>;
    }
  return (
    <Modal open={openModal} onClose={closeModalFunc}>
      <Box style={style}>
        {sources}
      </Box>
    </Modal>
  );
}

export default AddNewSourceModal
