import React, { useState } from "react";
import { Box, Modal } from "@mui/material";
import CountriesDropDownList from "./CountriesDropDownList";
import AddYodleeComponent from "./AddYodleeComponent";
import AddCryptoSource from "./AddCryptoSource";
import "../../styles/add-source-modal.scss";
import Loader from "./LoaderComponent";
import "../../styles/dashboard.scss";
import AssetsDropDownList from "./AssetsDropDownList";

const AddNewSourceModal = ({ openModal, closeModalFunc, source }) => {
  const [content, setContent] = useState();

  const selectProvider = (selected) => {
    if (selected === "binance") {
      setContent(<AddCryptoSource selected={"binance"} />);
    } else if (selected === "coinbase") {
      setContent(<AddCryptoSource selected={"coinbase"} />);
    }
  };

  let sources;
  if (source === "banks") {
    sources = <CountriesDropDownList />;
  } else if (source === "brokers") {
    sources = <AddYodleeComponent />;
  } else if (source === "crypto") {
    sources = (
      <div className="buttons-div">
        <button
          className="button-main-big"
          onClick={() => {
            selectProvider("binance");
          }}
        >
          binance
        </button>
        <button
          className="button-main-big"
          onClick={() => selectProvider("coinbase")}
        >
          coinbase
        </button>
      </div>
    );
  } else {
    sources = <AssetsDropDownList />;
  }

  const handleClose = () => {
    window.fastlink.close();
    setContent();
    closeModalFunc();
  };
  console.log(sources.loading);
  return (
    <Modal open={openModal} onClose={handleClose}>
      <Box className="modal-box">{content ? content : sources}</Box>
    </Modal>
  );
};

export default AddNewSourceModal;
