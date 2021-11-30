import React, {useState} from 'react'
import {Box, Modal} from "@mui/material";
import CountriesDropDownList from "./CountriesDropDownList";
import AddYodleeComponent from "./AddYodleeComponent";
import AddCryptoSource from "./AddCryptoSource";
import '../../styles/add-source-modal.scss'
import Loader from "./LoaderComponent";

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
  console.log(sources.loading)
  return (
    <Modal open={openModal} onClose={handleClose}>
      <Box className='modal-box'>
        {sources.loading === true && <Loader />}
        {content ? content : sources}
      </Box>
    </Modal>
  );
}

export default AddNewSourceModal
