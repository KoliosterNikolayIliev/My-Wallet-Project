import { useEffect, useState } from "react";
// import { countries } from "../../utils/nordigen";
import { DropDownList } from "@progress/kendo-react-dropdowns";
import { BanksContainer } from "./BanksContainer";

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
  // Store currently selected category
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [data, setData] = useState([]);

  useEffect(() => {
    countries.forEach((country) => {
      setCategories((prev) => [...prev, country]);
    });
  }, []);

  useEffect(() => {
    // TODO: get data for country from account
  }, [selectedCategory]);

  return (
    <div>
      <section className="k-my-8">
        <form className="k-form k-mb-4">
          <label className="k-label k-mb-3">Category</label>
          <DropDownList
            data={categories}
            onChange={(e) => setSelectedCategory(e.value)}
          />
        </form>
      </section>
      <BanksContainer data={data} />
    </div>
  );
};

export default CountriesDropDownList;
