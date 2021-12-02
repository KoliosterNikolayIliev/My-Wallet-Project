import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { BanksContainer } from "./BanksContainer";
import { getBanks } from "../../utils/nordigen";
import {InputLabel, MenuItem, Select} from "@mui/material";
import Loader from "./LoaderComponent";

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
  const [country, setCountry] = useState("United Kingdom");
  const [data, setData] = useState([]);
  const { getAccessTokenSilently } = useAuth0();
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    countries.forEach((country) => {
      setCategories((prev) => [...prev, country]);
    });
  }, []);

  useEffect(() => {
    if (country !== "") {
      const fetchData = async () => {
        setLoading(true)
        const token = await getAccessTokenSilently();
        const banks = await getBanks(token, country);
        setData(banks);
        setLoading(false)
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
            defaultValue={'United Kingdom'}
            onChange={(e) => setCountry(e.target.value)}>
            {categories.map(el => <MenuItem value={el}>{el}</MenuItem>)}
          </Select>
        </form>
      </section>
      {loading ? <Loader/> : <BanksContainer data={data} />}
    </div>
  );
};

export default CountriesDropDownList;
