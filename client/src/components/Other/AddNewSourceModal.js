import React, {useState} from 'react'
import {Box, Modal} from "@mui/material";
import CountriesDropDownList from "./CountriesDropDownList";
import AddYodleeComponent from "./AddYodleeComponent";
import AddCryptoSource from "./AddCryptoSource";

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  background: '#FFFFFF',
  border: '2px solid #000',
  width: '685px',
  height: '810px',
}

const AddNewSourceModal = ({openModal, closeModalFunc, source}) => {

  const [content, setContent] = useState()

  const selectProvider = (selected) => {
    if (selected === 'binance') {
      setContent(
        <AddCryptoSource selected={'binance'}/>
      )
    }else if (selected === 'coinbase') {
      setContent(
        <AddCryptoSource selected={'coinbase'}/>
      )
    }

  }

  let sources;
  if (source === 'banks') {
    sources = <CountriesDropDownList/>
  } else if (source === 'brokers') {
    sources = <AddYodleeComponent/>
  } else if (source === 'crypto') {
    sources = (
      <div>
        <button onClick={() => {
          selectProvider('binance')
        }}>binance
        </button>
        <button onClick={() => selectProvider('coinbase')}>coinbase</button>
      </div>
    );
  } else {
    sources = <h1>custom entry</h1>;
  }

  const handleClose = () => {
    window.fastlink.close()
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
