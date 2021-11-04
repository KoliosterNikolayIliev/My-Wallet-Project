import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { DropDownList } from "@progress/kendo-react-dropdowns";
import { BanksContainer } from "./BanksContainer";
import { getBanks } from "../../utils/nordigen";

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
      <section className="k-my-8">
        <form className="k-form k-mb-4">
          <label className="k-label k-mb-3">Category</label>
          <DropDownList
            data={categories}
            onChange={(e) => setCountry(e.value)}
          />
        </form>
      </section>
      <BanksContainer data={data} />
    </div>
  );
};

export default CountriesDropDownList;
