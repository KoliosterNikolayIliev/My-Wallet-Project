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
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.json();
};

const deleteNordigenAccount = async (token, institution_id) => {
  await fetch("http://localhost:8001/api/account/user/bank", {
    method: "DELETE",
    body: JSON.stringify({institution_id: institution_id}),
    headers: {
      authorization: `Bearer ${token}`,
    },
  });
}

export { getUser, updateUser, getAccessToken, deleteNordigenAccount };
