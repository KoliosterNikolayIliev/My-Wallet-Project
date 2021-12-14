import "@progress/kendo-theme-default/dist/all.css";
import "./App.css";
import DashboardPage from "./components/Pages/DashboardPage";
import ProfilePage from "./components/Pages/ProfilePage";
import LandingPage from "./components/Pages/LandingPage";
import PortfolioPage from "./components/Pages/PortfolioPage";
import CashflowPage from "./components/Pages/CashflowPage";
import ErrorPage from "./components/Pages/ErrorPage";

import {
	BrowserRouter as Router,
	Route,
	Switch,
	Redirect,
} from "react-router-dom";

import { RecoilRoot, atom } from "recoil";

import { useAuth0 } from "@auth0/auth0-react";

// Simple Home page to display the log in button and user info if the user is logged in
function App() {
	const { isAuthenticated } = useAuth0();

	return (
		<RecoilRoot>
			{/* Wrap app in a router to handle routing */}
			<Router>
				{/* Add switch for react router */}
				<Switch>
					{/* If the user is logged in directly redirect them to the dashboard, otherwise show the landing page */}
					<Route path="/" exact>
						{isAuthenticated ? (
							<Redirect to="/dashboard" />
						) : (
							<LandingPage />
						)}
					</Route>
					<Route path="/dashboard" exact component={DashboardPage} />
					<Route path="/profile" exact component={ProfilePage} />
					<Route path="/portfolio" exact component={PortfolioPage} />
					<Route path="/cashflow" exact component={CashflowPage} />
					<Route path="*" component={ErrorPage} />
				</Switch>
			</Router>
		</RecoilRoot>
	);
}

export default App;
