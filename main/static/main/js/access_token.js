var loginUrl = "/login/";

function checkAccessTokenAndRedirect() {
    // Check for access token in localStorage
    const accessToken = localStorage.getItem("access_token");
    
    console.log("JS FILE:", accessToken);

    // Redirect to login if no access token
    if (!accessToken) {
        // Use the login URL variable
        window.location.href = loginUrl;
        return; // Exit the function if redirected
    }
}

// Call the function to check access token and redirect
checkAccessTokenAndRedirect();
