import React, { useState } from "react";
import ExpandSourceModal from "./ExpandSourceModal";
import "../../styles/dashboard.scss";
import { baseAtom } from "../../recoil";
import { useRecoilState } from "recoil";

const ExpandButton = ({ user, name, source }) => {
  const [openModal, setOpenModal] = useState(false);
  const [base, setBase] = useRecoilState(baseAtom);
  const openModalFunc = () => {
    setOpenModal(true);
  };
  const closeModalFunc = () => {
    setOpenModal(false);
  };
  return (
    <div>
      <div className="expand-button" onClick={openModalFunc}>
        <p>Expand</p>
        <svg
          width="8"
          height="12"
          viewBox="0 0 8 12"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M1.16994 1.00005C0.983691 1.18741 0.87915 1.44087 0.87915 1.70505C0.87915 1.96924 0.983692 2.22269 1.16994 2.41005L4.70994 6.00005L1.16994 9.54005C0.983692 9.72741 0.87915 9.98087 0.87915 10.2451C0.87915 10.5092 0.983692 10.7627 1.16994 10.9501C1.26291 11.0438 1.37351 11.1182 1.49537 11.1689C1.61723 11.2197 1.74793 11.2458 1.87994 11.2458C2.01195 11.2458 2.14266 11.2197 2.26452 11.1689C2.38638 11.1182 2.49698 11.0438 2.58994 10.9501L6.82994 6.71005C6.92367 6.61709 6.99806 6.50649 7.04883 6.38463C7.0996 6.26277 7.12574 6.13206 7.12574 6.00005C7.12574 5.86804 7.0996 5.73733 7.04883 5.61547C6.99806 5.49362 6.92367 5.38301 6.82994 5.29005L2.58994 1.00005C2.49698 0.906323 2.38638 0.831929 2.26452 0.78116C2.14266 0.730391 2.01195 0.704252 1.87994 0.704252C1.74793 0.704252 1.61722 0.730391 1.49537 0.78116C1.37351 0.831929 1.26291 0.906323 1.16994 1.00005Z"
            fill="#9031DB"
          />
        </svg>
      </div>
      <ExpandSourceModal
        base={base}
        openModal={openModal}
        closeModalFunc={closeModalFunc}
        name={name}
        user={user}
        source={source}
      />
    </div>
  );
};

export default ExpandButton;
