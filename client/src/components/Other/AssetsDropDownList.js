import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { DropDownList } from "@progress/kendo-react-dropdowns";
import { createCustomAsset } from "../../utils/portfolio";

const assetTypes = ["crypto", "stock"];

export const AssetsDropDownList = () => {
  const [categories, setCategories] = useState([]);
  const [symbol, setSymbol] = useState("");
  const [amount, setAmount] = useState(0);
  const [assetType, setAssetType] = useState("");

  const { getAccessTokenSilently } = useAuth0();

  useEffect(() => {
    assetTypes.forEach((type) => {
      setCategories((prev) => [...prev, type]);
    });
  }, []);

  const addAsset = async (e, type, symbol, amount) => {
    e.preventDefault();
    const token = await getAccessTokenSilently();
    const newAsset = await createCustomAsset(token, type, symbol, amount);
  };

  return (
    <div>
      <section className="k-my-8">
        <form
          className="k-form k-mb-4"
          onSubmit={(e) => addAsset(e, assetType, symbol, amount)}
        >
          <label className="k-label k-mb-3">Asset Type</label>
          <DropDownList
            required={true}
            data={categories}
            onChange={(e) => setAssetType(e.value)}
          />
          <input
            type="text"
            placeholder="e.g: BTC"
            onChange={(e) => setSymbol(e.target.value)}
          />
          <input
            type="float"
            placeholder="e.g: 0.01"
            onChange={(e) => setAmount(e.target.value)}
          />
          <button>Add asset</button>
        </form>
      </section>
    </div>
  );
};

export default AssetsDropDownList;
