import React, { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { DropDownList } from "@progress/kendo-react-dropdowns";
import { updateUser } from "../../utils/account";

const supportedCurrencies = [
  "AED",
  "AFN",
  "ALL",
  "AMD",
  "ANG",
  "AOA",
  "ARS",
  "AUD",
  "AWG",
  "AZN",
  "BAM",
  "BBD",
  "BDT",
  "BGN",
  "BHD",
  "BIF",
  "BMD",
  "BND",
  "BOB",
  "BRL",
  "BSD",
  "BTC",
  "BTN",
  "BWP",
  "BYN",
  "BZD",
  "CAD",
  "CDF",
  "CHF",
  "CLF",
  "CLP",
  "CNH",
  "CNY",
  "COP",
  "CRC",
  "CUC",
  "CUP",
  "CVE",
  "CZK",
  "DJF",
  "DKK",
  "DOP",
  "DZD",
  "EGP",
  "ERN",
  "ETB",
  "EUR",
  "FJD",
  "FKP",
  "GBP",
  "GEL",
  "GGP",
  "GHS",
  "GIP",
  "GMD",
  "GNF",
  "GTQ",
  "GYD",
  "HKD",
  "HNL",
  "HRK",
  "HTG",
  "HUF",
  "IDR",
  "ILS",
  "IMP",
  "INR",
  "IQD",
  "IRR",
  "ISK",
  "JEP",
  "JMD",
  "JOD",
  "JPY",
  "KES",
  "KGS",
  "KHR",
  "KMF",
  "KPW",
  "KRW",
  "KWD",
  "KYD",
  "KZT",
  "LAK",
  "LBP",
  "LKR",
  "LRD",
  "LSL",
  "LYD",
  "MAD",
  "MDL",
  "MGA",
  "MKD",
  "MMK",
  "MNT",
  "MOP",
  "MRO",
  "MRU",
  "MUR",
  "MVR",
  "MWK",
  "MXN",
  "MYR",
  "MZN",
  "NAD",
  "NGN",
  "NIO",
  "NOK",
  "NPR",
  "NZD",
  "OMR",
  "PAB",
  "PEN",
  "PGK",
  "PHP",
  "PKR",
  "PLN",
  "PYG",
  "QAR",
  "RON",
  "RSD",
  "RUB",
  "RWF",
  "SAR",
  "SBD",
  "SCR",
  "SDG",
  "SEK",
  "SGD",
  "SHP",
  "SLL",
  "SOS",
  "SRD",
  "SSP",
  "STD",
  "STN",
  "SVC",
  "SYP",
  "SZL",
  "THB",
  "TJS",
  "TMT",
  "TND",
  "TOP",
  "TRY",
  "TTD",
  "TWD",
  "TZS",
  "UAH",
  "UGX",
  "USD",
  "UYU",
  "UZS",
  "VES",
  "VND",
  "VUV",
  "WST",
  "XAF",
  "XAG",
  "XAU",
  "XCD",
  "XDR",
  "XOF",
  "XPD",
  "XPF",
  "XPT",
  "YER",
  "ZAR",
  "ZMW",
  "ZWL",
];

export const BaseCurrencyDropDownList = ({
  baseSymbol,
  saveChanges,
  provider,
}) => {
  const [categories, setCategories] = useState([]);

  const { getAccessTokenSilently } = useAuth0();

  useEffect(() => {
    supportedCurrencies.forEach((type) => {
      setCategories((prev) => [...prev, type]);
    });
  }, []);

  const setBaseCurrency = async (currency) => {
    const token = await getAccessTokenSilently();
    const data = {
      base_currency: currency,
    };
    updateUser(token, data);
    window.sessionStorage.clear();
  };

  return (
    <DropDownList
      data={categories}
      defaultItem={baseSymbol}
      style={{
        width: "17%",
        minWidth: "85px",
        fontFamily: "Inter sans-serif",
        fontSize: "16px",
        fontWeight: 600,
      }}
      onChange={(e) => [
        setBaseCurrency(e.value),
        () => saveChanges(provider),
        window.location.reload(),
      ]}
    />
  );
};

export default BaseCurrencyDropDownList;
