import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import { recentTransactionsAtom } from "../../recoil";
import { useRecoilState } from "recoil";

import "../../styles/dashboard.scss";
import "../../styles/main_content.scss";
import Loader from "../Other/LoaderComponent";

// Dashboard page to be filled in with user account data
const CashflowPage = () => {
  const [recentTransactions, setRecentTransactions] = useRecoilState(
    recentTransactionsAtom
  );
  const { isAuthenticated, user, loading } = useAuth0();

  useEffect(() => {
    console.log(recentTransactions);
  }, []);

  if (loading) {
    return Loader();
  }

  return (
    isAuthenticated && (
      <div>
        <h2>This is the cashflow page</h2>
      </div>
    )
  );
};

export default CashflowPage;
