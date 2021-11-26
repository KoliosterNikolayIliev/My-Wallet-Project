import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { BanksContainer } from "./BanksContainer";
import { getBanks } from "../../utils/nordigen";
import {InputLabel, MenuItem, Select} from "@mui/material";

const countries = [
  "Austria",
  "Croatia",
  "Denmark",
  "France",
  "Hungary",
  "Italy",
  "Liechtenstein",
  "Netherlands",
  "Portugal",
  "Slovenia",
  "United Kingdom",
  "Belgium",
  "Cyprus",
  "Estonia",
  "Germany",
  "Ireland",
  "Latvia",
  "Luxembourg",
  "Norway",
  "Romania",
  "Spain",
  "Bulgaria",
  "Czech Republic",
  "Finland",
  "Greece",
  "Iceland",
  "Lithuania",
  "Malta",
  "Poland",
  "Slovakia",
  "Sweden",
];

export const CountriesDropDownList = () => {
  const [categories, setCategories] = useState([]);
  const [country, setCountry] = useState("");
  const [data, setData] = useState([]);
  const { getAccessTokenSilently } = useAuth0();

  useEffect(() => {
    countries.forEach((country) => {
      setCategories((prev) => [...prev, country]);
    });
  }, []);

  useEffect(() => {
    if (country !== "") {
      const fetchData = async () => {
        const token = await getAccessTokenSilently();
        const banks = await getBanks(token, country);
        setData(banks);
      };
      fetchData();
    }
  }, [country]);

  return (
    <div>
      <section className="k-my-8" style={{textAlign: 'center'}}>
        <form className="k-form k-mb-4">
          <InputLabel id="simple-select" color="primary">
            Select a country
          </InputLabel>
          <Select
            labelId={'simple-select'}
            style={{width: '90%'}}
            onChange={(e) => setCountry(e.target.value)}>
            {categories.map(el => <MenuItem value={el}>{el}</MenuItem>)}
          </Select>
        </form>
      </section>
      <BanksContainer data={data} />
    </div>
  );
};

export default CountriesDropDownList;
