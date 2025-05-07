// Login
document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const response = await fetch("http://localhost:8000/token", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
          username: document.getElementById("username").value,
          password: document.getElementById("password").value
      })
  });
  if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.access_token);
      window.location.href = "dashboard.html";
  }
});

// Exemplo: Carregar tecidos
async function loadTecidos() {
  const token = localStorage.getItem("token");
  const response = await fetch("http://localhost:8000/tecidos", {
      headers: { "Authorization": `Bearer ${token}` }
  });
  if (response.ok) {
      const tecidos = await response.json();
      console.log(tecidos);
  }
}