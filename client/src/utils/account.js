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
  const response = await fetch("http://localhost:8001/api/account/user/bank", {
    method: "DELETE",
    body: {institution_id: JSON.stringify(institution_id)},
    headers: {
      authorization: `Bearer ${token}`,
    },
  });
  console.log(response.json())
}

export { getUser, updateUser, getAccessToken, deleteNordigenAccount };
