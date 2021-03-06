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
      account: account,
    },
  });

  return response.json();
};

const getAllRecentTransactions = async (token) => {
  const response = await fetch(
    "http://localhost:5001/api/recent-transactions",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.json();
};

const getHistoricalBalances = async (token) => {
  const response = await fetch(
    "http://localhost:5001/api/historical-balances",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.json();
};

const createCustomAsset = async (token, type, symbol, amount) => {
  const response = await fetch("http://localhost:5001/api/create-asset", {
    headers: {
      Authorization: `Bearer ${token}`,
      type: type,
      symbol: symbol,
      amount: amount,
    },
  });

  return response.json();
};

const deleteCustomAsset = async (token, asset, asset_type) => {
  const response = await fetch("http://localhost:5001/api/delete-asset", {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${token}`,
      asset_type: asset_type,
      asset: asset,
    },
  });

  return response.json();
}

export {
  getAssets,
  getTransactions,
  createCustomAsset,
  getAllRecentTransactions,
  getHistoricalBalances,
  deleteCustomAsset,
};
