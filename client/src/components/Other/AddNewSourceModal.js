import React, {Fragment, useState} from 'react'
import {Box, Modal} from "@mui/material";
import CountriesDropDownList from "./CountriesDropDownList";
import AddYodleeComponent from "./AddYodleeComponent";
import AddBinanceSource from "./AddBinanceSource";

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

  const [content, setContent] = useState()

  const selectProvider = (selected) => {
    if (selected === 'nordigen') {
      setContent(<CountriesDropDownList/>)
    } else if (selected === 'yodlee') {
      setContent(
        <AddYodleeComponent/>
      )
    }else if (selected === 'binance') {
      setContent(
        <AddBinanceSource/>
      )
    }

  }

  let sources;
  if (source === 'banks') {
    sources = (
      <Fragment>
        <button onClick={() => selectProvider('nordigen')}>nordigen</button>
        <button onClick={() => selectProvider('yodlee')}>yodlee</button>
      </Fragment>
    );
  } else if (source === 'crypto') {
    sources = (
      <Fragment>
        <button onClick={() => {selectProvider('binance')}}>binance</button>
        <button>coinbase</button>
      </Fragment>
    );
  } else {
    sources = <h1>custom entry</h1>;
  }

  const handleClose = () => {
    setContent()
    closeModalFunc()
  }

  return (
    <Modal open={openModal} onClose={handleClose}>
      <Box style={style}>
        {content ? content : sources}
      </Box>
    </Modal>
  );
}

export default AddNewSourceModal
