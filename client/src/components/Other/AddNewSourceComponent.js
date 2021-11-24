import React, {useState} from 'react'
import AddNewSourceMenu from "./AddNewSourceMenu";

const AddNewSourceComponent = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const openMenuBul = Boolean(anchorEl)
  const openMenu = (event) => {
    setAnchorEl(event.currentTarget)
  }

  const closeMenu = () => {
    setAnchorEl(null);
  }
  return (
    <AddNewSourceMenu
      openMenuFunc={openMenu}
      openBul={openMenuBul}
      anchorEl={anchorEl}
      closeMenuFunc={closeMenu}
      modalFunc={closeMenu}
    />
  )
}

export default AddNewSourceComponent