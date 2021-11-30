import { atom } from "recoil";

const recentTransactionsAtom = atom({
  key: "recentTransactionsState",
  default: "",
});

export default recentTransactionsAtom;
