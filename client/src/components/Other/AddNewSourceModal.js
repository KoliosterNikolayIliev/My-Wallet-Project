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
  const getSources = () => {
    if (source === 'banks') {
      return <h1>banks</h1>;
    }else if (source === 'crypto') {
      return <h1>crypto</h1>;
    }else {
      return <h1>custom entry</h1>
    }
  }
  return (
    <Modal open={openModal} onClose={closeModalFunc}>
      <Box style={style}>
        {getSources()}
      </Box>
    </Modal>
  );
}

export default AddNewSourceModal
