const getUser = async (token) => {
  const response = await fetch("http://localhost:8001/api/account/user", {
    method: "GET",
    headers: {
      authorization: `Bearer ${token}`,
    },
  });

  return response.json();
};

export default getUser;
