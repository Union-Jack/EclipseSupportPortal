document.addEventListener("DOMContentLoaded", function () {
    const togglePassword = document.getElementById("togglePassword");
    const passwordField = document.getElementById("passwordField");

    if (togglePassword && passwordField) {

        togglePassword.addEventListener("mousedown", function () {
            passwordField.type = "text";
        });
        
        togglePassword.addEventListener("mouseup", function () {
            passwordField.type = "password";
        });

        togglePassword.addEventListener("mouseleave", function () {
            passwordField.type = "password";
        });
    }
});