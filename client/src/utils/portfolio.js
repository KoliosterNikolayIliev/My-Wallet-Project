const getBalances = async (token) => {
  const response = await fetch("http://localhost:5001/api/balances", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

export default getBalances;
