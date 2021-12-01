import React, {useState} from 'react'
import AddNewSourceMenu from "./AddNewSourceMenu";
import AddNewSourceModal from "./AddNewSourceModal";

const AddNewSourceComponent = () => {
  const [openModal, setOpenModal] = useState(false)
  const [source, setSource] = useState(null)

  const openModalFunc = (selectedSource) => {
    let el = document.getElementById('popup-1')
    if (el) {el.style.display = 'none'}
    setSource(selectedSource)
    setOpenModal(true)
  }
  const closeModalFunc = () => {
    setOpenModal(false)
  }

  return (
    <div style={{display: 'inline'}}>
      <AddNewSourceMenu
        modalFunc={openModalFunc}
      />
      <AddNewSourceModal openModal={openModal} closeModalFunc={closeModalFunc} source={source}/>
    </div>
  )
}

export default AddNewSourceComponent