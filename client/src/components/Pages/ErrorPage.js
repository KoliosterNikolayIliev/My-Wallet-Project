import { useState } from "react";
import { Redirect } from "react-router";

const ErrorPage = () => {
	const [reloaded, setReloaded] = useState(false);
	return (
		<div>
			{reloaded ? (
				<Redirect to="/dashboard" />
			) : (
				<div className="error-page">
					<h1 className="heding">Ooops</h1>
					<p className="body">
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
