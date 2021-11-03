const getBanks = async ({ token, country }) => {
  const banks = await fetch(
    "http://localhost:8001/api/account/user/nordigen-banks",
    {
      headers: {
        Authorization: `Bearer ${token}`,
        country: country,
      },
    }
  );
  return banks.json();
};

export { getBanks };
