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


    // 空き時間取得
    const stylistSelect =
        document.getElementById("stylist_id");

    const dateInput =
        document.getElementById("date");

    const timeArea =
        document.getElementById("time-area");

    const timeInput =
        document.getElementById("time");


    function loadTimes(){

        const stylistId = stylistSelect.value;
        const date = dateInput.value;


        if(!stylistId || !date){
            return;
        }


        fetch(
            `/reservation/times?date=${date}&stylist_id=${stylistId}`
        )
        .then(response => response.json())
        .then(schedule => {


            timeArea.innerHTML = "";


            for(let time in schedule){


                const button =
                    document.createElement("button");


                button.type = "button";


                button.textContent =
                    `${time} ${schedule[time]}`;



                if(schedule[time] === "×"){

                    button.disabled = true;


                }else{


                    button.onclick = function(){


                        timeInput.value = time;


                        document
                        .querySelectorAll("#time-area button")
                        .forEach(btn => {
                            btn.classList.remove("selected");
                        });


                        button.classList.add("selected");

                    };

                }


                timeArea.appendChild(button);

            }


        });

    }



    if(stylistSelect && dateInput){


        stylistSelect.addEventListener(
            "change",
            loadTimes
        );


        dateInput.addEventListener(
            "change",
            loadTimes
        );

    }

});