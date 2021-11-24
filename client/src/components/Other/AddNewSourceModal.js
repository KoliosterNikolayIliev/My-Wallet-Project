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

const AddNewSourceModal = ({openModal, closeModalFunc}) => {
  return (
    <Modal open={openModal} onClose={closeModalFunc}>
      <Box style={style}>
        <h1>TEST</h1>
      </Box>
    </Modal>
  )
}

export default AddNewSourceModal
