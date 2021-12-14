import React from "react";

class ErrorBoundary extends React.Component {
	state = { hasError: false };
	static getDerivedStateFromError(error) {
		return { hasError: true };
	}
	componentDidCatch(error, errorInfo) {
		console.log({ error, errorInfo });
	}
	render() {
		if (this.state.hasError) {
			return (
				<div className="errorPage">
					<h1>Ooops</h1>
					<p>Something went wrong! Try reloading the page.</p>
				</div>
			);
		}
		return this.props.children;
	}
}
