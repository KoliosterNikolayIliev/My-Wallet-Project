import "./App.css";
import LogInButton from "./components/LogInButton";
import Profile from "./components/Profile";

// Simple Home page to display the log in button and user info if the user is logged in
function App() {
  return (
    <>
      <LogInButton />
      <Profile />
    </>
  );
}

export default App;
