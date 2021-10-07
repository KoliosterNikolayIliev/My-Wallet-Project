import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Redirect } from "react-router";
import LogOutButton from "./LogOutButton";
import axios from "axios";

// Dashboard page to be filled in with user account data



const DashboardPage = () => {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } = useAuth0();

    //Print user data in console. User needs to be authenticated. Only for testing.
    async function getUserData() {
        const token = await getAccessTokenSilently()
        try {
            const getUser = await axios.get('http://localhost:8000/api/account/user/',{
                headers:{
                    Authorization: `Bearer ${token}`
                }
            })
            console.log(getUser)
        } catch (error) {
            console.log(error.message)
        }
    }
    //Deletes user. Only for testing.
    async function deleteUser() {
        const token = await getAccessTokenSilently()
        try {
            const serverDelete = await axios.delete('http://localhost:8000/api/account/user/delete',{
                headers:{
                    authorization: `Bearer ${token}`
                }
            })
            console.log(serverDelete)

            // console.log(authDelete)
        } catch (error) {
            console.log(error.message)
        }
    }
    async function editUser() {
        const token = await getAccessTokenSilently()
        try {
            const serverEdit = await axios.post('http://localhost:8000/api/account/user/edit',{
                    user_identifier: `${token}`,
                    base_currency : 'USD',
                    source_label:'Whatever',
                    binance_key:'xxx',
                    binance_secret:'YYY',
                    yodlee_login_name:''
            })
            await console.log(serverEdit)

            // console.log(authDelete)
        } catch (error) {
            console.log(error.message)
        }
    }

  //   Return this if Auth0 is still loading. Can be replaced with an animation in the future
  if (isLoading) {
    return <div>Loading ...</div>;
  }

  // Redirect the user to the landing page if the user is not logged in
  if (!isAuthenticated) {
    return <Redirect to={"/"} />;
  }

  return (
    isAuthenticated && (
      <div>
        <h2>Hi, {user.name}, this is the dashboard</h2>
        <span>{user.birthdate},{user.email}</span>
          <ul>
              <li><button onClick={getUserData}>Get user data(create user if not existing)</button></li>
              <li><button onClick={deleteUser}>Delete user</button></li>
              <li><button onClick={editUser}>Change user data</button></li>
          </ul>
        <LogOutButton/>
      </div>
    )
  );
};

export default DashboardPage;
