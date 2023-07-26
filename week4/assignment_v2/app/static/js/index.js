function handleLoginFormSubmit(event) {
    event.preventDefault();

    // 檢查 checkbox 是否已勾選
    const checkbox = document.getElementById("checkOK");
    if (!checkbox.checked) {
    alert("Please agree to the terms and conditions");
    return;
    }

    // 取得帳密
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // 發送 POST 請求
    fetch("/signin", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ username:username, "password":password })
    })
    .then(response => response.json())
    .then(data => {
        const message = data['message'];
        if (message === "ok") {
        // 跳轉到 /member
        window.location.href = "/member";
        } else {
        // 跳轉到 /error?message=msg
        window.location.href = `/error?message=${message}`;
        }
    })
    .catch(error => {
        console.error("發生錯誤:", error);
    });
}

function handleSquareSubmit(event) {
    event.preventDefault();
    let input = document.getElementById("square").value;
    if (isNaN(input) || input <= 0) {
        alert("Please enter a positive number");
        return false;
    }
    window.location.href = `/square/${input}`;
}