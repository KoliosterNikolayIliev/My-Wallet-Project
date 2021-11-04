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

const linkAccount = async (token, bank) => {
  const response = await fetch("http://localhost:8001/api/account/user/bank", {
    method: "POST",
    body: JSON.stringify({ institution_id: bank }),
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

export { getBanks, linkAccount };
