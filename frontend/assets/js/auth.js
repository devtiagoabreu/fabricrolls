document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const response = await fetch("http://localhost:8000/token", {
      method: "POST",
      headers: {
          "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
          username: document.getElementById("username").value,
          password: document.getElementById("password").value,
          grant_type: "password"
      })
  });

  if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.access_token);
      window.location.href = "dashboard.html";
  } else {
      alert("Login falhou!");
  }
});