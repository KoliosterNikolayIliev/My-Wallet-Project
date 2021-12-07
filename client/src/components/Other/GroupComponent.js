import React, { useState } from "react";
import {deleteCustomAsset} from "../../utils/portfolio";
import {useAuth0} from "@auth0/auth0-react";

const GroupComponent = ({
  account,
  source,
  type,
  provider,
  getTransactionsFunc,
  baseSymbol,
  custom_asset,
}) => {
  let amount = 0;
  let currency = "";
  let base_currency = 0;

  const {getAccessTokenSilently} = useAuth0();

  const deleteCustomAssetFunc = async (asset, asset_type) => {
    const token = await getAccessTokenSilently();
    await deleteCustomAsset(token, asset, asset_type)
    window.sessionStorage.clear();
    window.location.reload()
  }

  if (account.data.balanceData) {
    amount = Number(account.data.balanceData.amount);
    currency = account.data.balanceData.currency;
    base_currency = account.data.balanceData.base_currency;
  } else {
    amount = Number(account.data.quantity);
    currency = account.data.symbol;
    base_currency = account.data.base_currency;
  }

  if (!type) {
    type = `${source} account(${currency})`;
  } else {
    type = `${source} ${type} account(${currency})`;
  }

  if (!base_currency) {
    base_currency = "N/A";
  } else {
    base_currency = base_currency.toFixed(2);
  }

  if (amount > 0) {
    return (
      <div className="asset-root">
        {provider !== "binance" &&
          provider !== "custom_assets" &&
          provider !== "coinbase" && (
            <div
              className="asset-line"
              onClick={() => getTransactionsFunc(provider, account.id)}
            >
              <p className="data-source-asset">{type}</p>{" "}
              <p className="data-source-asset">
                {base_currency} {baseSymbol}
              </p>
            </div>
          )}
        {(provider === "custom_assets" || provider === "binance") && (
          <div className="asset-line">
            {custom_asset && <button onClick={() => deleteCustomAssetFunc(currency, custom_asset)}>X</button>}
            <p>{currency}</p>{" "}
            <p>
              {" "}
              {base_currency} {baseSymbol}
            </p>
          </div>
        )}
        {provider === "coinbase" && (
          <div
            className="asset-line"
            onClick={() => getTransactionsFunc(provider, account.id)}
          >
            <p className="data-source-asset">{currency}</p>{" "}
            <p className="data-source-asset">
              {" "}
              {base_currency} {baseSymbol}
            </p>
          </div>
        )}
      </div>
    );
  }
  return null;
};

export default GroupComponent;
