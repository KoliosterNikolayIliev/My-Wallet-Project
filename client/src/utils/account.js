const getUser = async (token) => {
  const response = await fetch("http://localhost:8001/api/account/user", {
    method: "GET",
    headers: {
      authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

const updateUser = async (token, user) => {
  const response = await fetch("http://localhost:8001/api/account/user", {
    method: "PUT",
    body: JSON.stringify(user),
    headers: {
      authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

const getAccessToken = async (token) => {
  const response = await fetch(
    "http://localhost:8001/api/account/user/yodlee-token",
    {
      headers: {
        Authorization: token,
      },
    }
  );

  return response.json();
};

export { getUser, updateUser, getAccessToken };
