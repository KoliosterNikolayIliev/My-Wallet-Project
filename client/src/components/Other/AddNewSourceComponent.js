import React, {useState} from 'react'
import AddNewSourceMenu from "./AddNewSourceMenu";
import AddNewSourceModal from "./AddNewSourceModal";

const AddNewSourceComponent = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const openMenuBool = Boolean(anchorEl)

  const openMenuFunc = (event) => {
    setAnchorEl(event.currentTarget)
  }
  const closeMenuFunc = () => {
    setAnchorEl(null);
  }

  const [openModal, setOpenModal] = useState(false)
  const [source, setSource] = useState(null)

  const openModalFunc = (selectedSource) => {
    setSource(selectedSource)
    setAnchorEl(null);
    setOpenModal(true)
  }
  const closeModalFunc = () => {
    setOpenModal(false)
  }

  return (
    <div>
      <AddNewSourceMenu
        openMenuFunc={openMenuFunc}
        openBool={openMenuBool}
        anchorEl={anchorEl}
        closeMenuFunc={closeMenuFunc}
        modalFunc={openModalFunc}
      />
      <AddNewSourceModal openModal={openModal} closeModalFunc={closeModalFunc} source={source}/>
    </div>
  )
}

export default AddNewSourceComponent