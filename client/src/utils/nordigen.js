const getBanks = async (token, country) => {
  const banks = await fetch(
    `http://localhost:8001/api/account/user/nordigen-banks?country=${country}`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
  return banks.json();
};

export { getBanks };
