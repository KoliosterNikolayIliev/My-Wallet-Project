import React, { useState } from "react";
import { Box, Modal } from "@mui/material";
import Loader from "./LoaderComponent";
import GroupComponent from "./GroupComponent";
import HoldingComponent from "./HoldingComponent";
import "../../styles/add-source-modal.scss";
import "../../styles/dashboard.scss";

const ExpandSourceModal = ({
  openModal,
  closeModalFunc,
  name,
  source,
  user,
  base,
}) => {
  if (openModal) {
    return (
      <Modal open={openModal} onClose={closeModalFunc}>
        <Box className="expand-modal">
          <div className="data-source expand-data-source">
            <div className="data-source-header">
              <p>{name[0].toUpperCase() + name.slice(1)} </p>
              <p className="data-source-total">
                {source.total.toFixed(2)} {base}
              </p>
            </div>
            <div className="data-source-content">
              <ul>
                {(source.accounts.length > 1 ||
                  source === "coinbase" ||
                  (source.accounts.length === 1 &&
                    source === "yodlee" &&
                    source.accounts[0].holdings.length === 0)) &&
                  source.accounts.map((account) => {
                    return (
                      <GroupComponent
                        source={name[0].toUpperCase() + name.slice(1)}
                        baseSymbol={base}
                        provider={account.provider}
                        account={account}
                        type={account.data.accountType}
                      />
                    );
                  })}
                {source.accounts.length <= 1 &&
                  source.accounts.map((account) => {
                    if (account.holdings) {
                      if (account.holdings.length > 0) {
                        return account.holdings.map((holding) => {
                          return (
                            <HoldingComponent
                              nest={false}
                              account={account}
                              data={holding}
                              baseSymbol={base}
                            />
                          );
                        });
                      }
                      return null;
                    }
                    return null;
                  })}
                {source.accounts.length > 1 &&
                  source.accounts.map((account) => {
                    if (account.holdings) {
                      if (account.holdings.length > 0) {
                        return (
                          <ul>
                            {account.holdings.map((holding) => {
                              return (
                                <HoldingComponent
                                  nest={true}
                                  data={holding}
                                  baseSymbol={base}
                                />
                              );
                            })}
                          </ul>
                        );
                      }
                      return null;
                    }
                    return null;
                  })}
              </ul>
              <div className="expand-button" onClick={closeModalFunc}>
                <p>Collapse</p>
                {/* <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M18.0281 9.96444C18.0281 9.55023 17.6923 9.21444 17.2781 9.21444L14.7855 9.21444V6.7218C14.7855 6.30759 14.4497 5.9718 14.0355 5.9718C13.6213 5.9718 13.2855 6.30759 13.2855 6.7218V9.96444C13.2855 10.3787 13.6213 10.7144 14.0355 10.7144L17.2781 10.7144C17.6923 10.7144 18.0281 10.3787 18.0281 9.96444Z"
                    fill="#9031DB"
                  />
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M14.0355 18.0281C14.4497 18.0281 14.7855 17.6923 14.7855 17.2781L14.7855 14.7855L17.2782 14.7855C17.6924 14.7855 18.0282 14.4497 18.0282 14.0355C18.0282 13.6213 17.6924 13.2855 17.2782 13.2855L14.0355 13.2855C13.6213 13.2855 13.2855 13.6213 13.2855 14.0355L13.2855 17.2781C13.2855 17.6923 13.6213 18.0281 14.0355 18.0281Z"
                    fill="#9031DB"
                  />
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M9.96444 18.0281C9.55023 18.0281 9.21444 17.6923 9.21444 17.2781V14.7855H6.7218C6.30759 14.7855 5.9718 14.4497 5.9718 14.0355C5.9718 13.6213 6.30759 13.2855 6.7218 13.2855L9.96444 13.2855C10.3787 13.2855 10.7144 13.6213 10.7144 14.0355L10.7144 17.2781C10.7144 17.6923 10.3787 18.0281 9.96444 18.0281Z"
                    fill="#9031DB"
                  />
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M5.97183 9.96444C5.97183 9.55023 6.30761 9.21444 6.72183 9.21444H9.21447L9.21447 6.7218C9.21447 6.30759 9.55026 5.9718 9.96447 5.9718C10.3787 5.9718 10.7145 6.30759 10.7145 6.7218L10.7145 9.96444C10.7145 10.3787 10.3787 10.7144 9.96447 10.7144L6.72183 10.7144C6.30761 10.7144 5.97183 10.3787 5.97183 9.96444Z"
                    fill="#9031DB"
                  />
                </svg> */}
              </div>
            </div>
          </div>
          <div className={"expand-modal-extra-info"}>
            <div className={"total-value"}>
              <p>Total Value</p>
              <p>
                {Number(source.total).toFixed(2)} {base}
              </p>
            </div>
            <div className={"remove-account"}>
              <div className={"account-info"}>
                <p>{name}</p>
                <p>{user.email}</p>
              </div>
              <div className={"remove-button"}>
                {/* <svg
                  width="15"
                  height="14"
                  viewBox="0 0 15 14"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M6.54619 13.6667H3.28886C1.65953 13.6667 0.333527 12.3407 0.333527 10.71V3.29071C0.333527 1.66004 1.65953 0.333374 3.28886 0.333374H6.53886C8.16953 0.333374 9.49619 1.66004 9.49619 3.29071V3.91204C9.49619 4.18804 9.27219 4.41204 8.99619 4.41204C8.72019 4.41204 8.49619 4.18804 8.49619 3.91204V3.29071C8.49619 2.21071 7.61819 1.33337 6.53886 1.33337H3.28886C2.21086 1.33337 1.33353 2.21071 1.33353 3.29071V10.71C1.33353 11.7894 2.21086 12.6667 3.28886 12.6667H6.54619C7.62086 12.6667 8.49619 11.792 8.49619 10.7174V10.0887C8.49619 9.81271 8.72019 9.58871 8.99619 9.58871C9.27219 9.58871 9.49619 9.81271 9.49619 10.0887V10.7174C9.49619 12.344 8.17219 13.6667 6.54619 13.6667"
                    fill="#FC3400"
                  />
                  <mask
                    id="mask0_33752_442"
                    style="mask-type:alpha"
                    maskUnits="userSpaceOnUse"
                    x="4"
                    y="6"
                    width="11"
                    height="2"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M4.99741 6.5H14.0247V7.5H4.99741V6.5Z"
                      fill="white"
                    />
                  </mask>
                  <g mask="url(#mask0_33752_442)">
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M13.5247 7.5H5.49741C5.22141 7.5 4.99741 7.276 4.99741 7C4.99741 6.724 5.22141 6.5 5.49741 6.5H13.5247C13.8007 6.5 14.0247 6.724 14.0247 7C14.0247 7.276 13.8007 7.5 13.5247 7.5"
                      fill="#FC3400"
                    />
                  </g>
                  <mask
                    id="mask1_33752_442"
                    style="mask-type:alpha"
                    maskUnits="userSpaceOnUse"
                    x="11"
                    y="4"
                    width="4"
                    height="6"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M11.0731 4.55688H14.0247V9.44405H11.0731V4.55688Z"
                      fill="white"
                    />
                  </mask>
                  <g mask="url(#mask1_33752_442)">
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M11.5729 9.44405C11.4449 9.44405 11.3163 9.39539 11.2189 9.29672C11.0243 9.10072 11.0249 8.78472 11.2203 8.59005L12.8163 7.00005L11.2203 5.41072C11.0249 5.21605 11.0236 4.90005 11.2189 4.70405C11.4136 4.50805 11.7296 4.50805 11.9256 4.70272L13.8776 6.64605C13.9723 6.73939 14.0249 6.86739 14.0249 7.00005C14.0249 7.13272 13.9723 7.26072 13.8776 7.35405L11.9256 9.29805C11.8283 9.39539 11.7003 9.44405 11.5729 9.44405"
                      fill="#FC3400"
                    />
                  </g>
                </svg> */}

                <p>Disconnect account</p>
                {/* <svg
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M8.33334 5L7.15834 6.175L10.975 10L7.15834 13.825L8.33334 15L13.3333 10L8.33334 5Z"
                    fill="#FC3400"
                  />
                </svg> */}
              </div>
            </div>
          </div>
        </Box>
      </Modal>
    );
  } else {
    return null;
  }
};

export default ExpandSourceModal;
