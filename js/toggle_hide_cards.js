
// -------------------------------HIDE CARDS--------------------------------------------

const activities = document.querySelectorAll(".activity_card_image");

activities.forEach((activity) => {
    activity.addEventListener("click", () => {
        // Ocultar el div 1

        var divs1 = document.querySelectorAll("#cards");
        divs1.forEach(function(div) {
            div.classList.remove("visible");
            div.classList.add("oculto");
        });

        // Mostrar el div 2
        document.getElementById("Interfaz.chat-widget").classList.remove("oculto");
        document.getElementById("Interfaz.chat-widget").classList.add("visible");
    })
})