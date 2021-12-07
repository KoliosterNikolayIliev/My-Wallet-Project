import { atom } from "recoil";

const balancesAtom = atom({
  key: "balancesState",
  default: "",
});

export default balancesAtom;
