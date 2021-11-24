import React, {Fragment, useState} from 'react'
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

  const openModalFunc = () => {
    setOpenModal(true)
  }
  const closeModalFunc = () => {
    setAnchorEl(null);
    setOpenModal(false)
  }

  return (
    <Fragment>
      <AddNewSourceMenu
        openMenuFunc={openMenuFunc}
        openBool={openMenuBool}
        anchorEl={anchorEl}
        closeMenuFunc={closeMenuFunc}
        modalFunc={openModalFunc}
      />
      <AddNewSourceModal openModal={openModal} closeModalFunc={closeModalFunc}/>
    </Fragment>
  )
}

export default AddNewSourceComponent