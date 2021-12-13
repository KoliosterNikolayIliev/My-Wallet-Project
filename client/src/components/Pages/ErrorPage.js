import { useState } from "react";
import { Redirect } from "react-router";

import "../../styles/error.scss";

const ErrorPage = () => {
	const [reloaded, setReloaded] = useState(false);
	return (
		<div className="body">
			{reloaded ? (
				<Redirect to="/dashboard" />
			) : (
				<div className="error-page">
					<h1 className="heading">Ooops</h1>
					<p className="content">
						Something went wrong! Try{" "}
						<button
							className="reload-button"
							onClick={() => {
								console.log("are de");
								window.sessionStorage.clear();
								setReloaded(true);
							}}
						>
							reloading the page.
						</button>
					</p>
				</div>
			)}
		</div>
	);
};

export default ErrorPage;
