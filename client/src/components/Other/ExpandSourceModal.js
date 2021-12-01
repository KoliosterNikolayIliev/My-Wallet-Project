import React, { useState } from "react";
import { Box, Modal } from "@mui/material";
import "../../styles/add-source-modal.scss";
import Loader from "./LoaderComponent";
import "../../styles/dashboard.scss";

const ExpandSourceModal = ({ openModal, closeModalFunc, source }) => {
  return (
    <Modal open={openModal} onClose={closeModalFunc}>
      <Box className="modal-box">
        <p>Gosho</p>
      </Box>
    </Modal>
  );
};

export default ExpandSourceModal;
