import "./App.css";
import Dashboard from "./components/Dashboard";
import Profile from "./components/Profile";
import Landing from "./components/Landing";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

// Simple Home page to display the log in button and user info if the user is logged in
function App() {
  const { isAuthenticated } = useAuth0();

  return (
    // Wrap app in a router to handle routing
    <Router>
      {/* Add switch for react router */}
      <Switch>
        {/* If the user is logged in directly redirect them to the dashboard, otherwise show the landing page */}
        <Route path="/" exact>
          {isAuthenticated ? <Redirect to="/dashboard" /> : <Landing />}
        </Route>
        <Route path="/profile" exact component={Profile} />
        <Route path="/dashboard" exact component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;
