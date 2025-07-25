async function addUser() {
    const name = document.getElementById("nameInput").value;
    const res = await fetch("/add_user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name })
    });
    const data = await res.json();
    alert(data.message);
    loadUsers();
}

async function loadUsers() {
    const res = await fetch("/get_users");
    const users = await res.json();
    const list = document.getElementById("userList");
    list.innerHTML = "";
    users.forEach(user => {
        const li = document.createElement("li");
        li.innerText = user[1]; // user[1] is name
        list.appendChild(li);
    });
}

window.onload = loadUsers;
