// -------------------------------HIDE CHAT--------------------------------------------
const back = document.querySelectorAll(".modal-button-chat-off-mini");

back.forEach((activity) => {
    activity.addEventListener("click", () => {
        // Ocultar el div 1

        var cardsDivs = document.querySelectorAll("#cards");
        cardsDivs.forEach(function(div) {
            div.classList.remove("oculto");
            div.classList.add("visible");
        });

        // Mostrar el div 2
        document.getElementById("Interfaz.chat-widget").classList.remove("visible");
        document.getElementById("Interfaz.chat-widget").classList.add("oculto");
    })
})