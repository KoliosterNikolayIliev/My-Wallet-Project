import React from "react";
import { Link } from "react-router-dom";

const ProfileButton = () => {
  return (
    <button>
      <Link to={"/profile"}>Profile</Link>
    </button>
  );
};

export default ProfileButton;
