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
    $("#clear_form").submit(function(event) {
        event.preventDefault(); // 阻止表單自動提交
        $.ajax({
            url: "/clear",
            type: "GET",
            success: function(response) {
                console.log(response)
                // window.location.href='/member';
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});