const getAssets = async (token) => {
  const response = await fetch("http://localhost:5001/api/assets", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

const getTransactions = async (token, provider, account) => {
  const response = await fetch("http://localhost:5001/api/transactions", {
    headers: {
      Authorization: `Bearer ${token}`,
      provider: provider,
      account: account
    },
  });

  return response.json();
};

export { getAssets, getTransactions };
