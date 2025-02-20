document.getElementById("fetchData").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/users") // Calls Flask backend
    .then(response => response.json()) 
    .then(data => {
        let output = document.getElementById("output");
        output.innerHTML = "<h3>Users List:</h3>";
        data.forEach(user => {
            output.innerHTML += `<p>${user.id}: ${user.name}</p>`;
        });
    })
    .catch(error => console.error("Error fetching data:", error));
});
