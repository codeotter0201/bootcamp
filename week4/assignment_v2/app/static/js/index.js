function appendNumberToAction() {
    var input = document.getElementById("square").value;
    if (isNaN(input) || input <= 0) {
        alert("Please enter a positive number");
        return false;
    }
    var form = document.getElementById("square_form");
    form.action += input;
    return true;
}
$(document).ready(function() {
    // 監聽表單提交事件
    $("#loginForm").submit(function(event) {
        event.preventDefault(); // 阻止表單自動提交

        // 檢查 checkOK 是否已勾選
        let checkOK = $("#checkOK").prop("checked");
        if (!checkOK) {
            alert("Please agree to the terms and conditions");
            return;
        }

        // 獲取用戶輸入的用戶名和密碼
        let username = $("#username").val();
        let password = $("#password").val();

        // 發送 POST 請求到 /signin
        $.ajax({
            url: "/signin",
            type: "POST",
            dataType: "json",
            data: {
                username: username,
                password: password
            },
            success: function(response) {
                let msg = response.message;
                if (msg == "ok"){
                    window.location.href = "/member";
                }else {
                    window.location.href = "/error?message=" + msg;
                }
                console.log(response)
            },
            error: function(response) {
                console.log(response)
            },
        });
    });
});