/**
 * ======================================
 * Salon Booking System
 * JavaScript
 * ======================================
 */

document.addEventListener("DOMContentLoaded", () => {

    console.log("JavaScriptを読み込みました。");

    // パスワード一致確認
    const registerForm = document.querySelector('form[action="/register"]');

    if (registerForm) {

        registerForm.addEventListener("submit", function (event) {

            const password =
                document.getElementById("password").value;

            const confirm =
                document.getElementById("confirm_password").value;

            if (password !== confirm) {

                alert("パスワードが一致しません。");

                event.preventDefault();

            }

        });

    }

    // 予約確認
    const reservationForm = document.querySelector('form[action="/reservation/create"]');

    if (reservationForm) {

        reservationForm.addEventListener("submit", function (event) {

            const result = confirm("この内容で予約しますか？");

            if (!result) {

                event.preventDefault();

            }

        });

    }

});