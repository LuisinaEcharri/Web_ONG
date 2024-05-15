const activities = document.querySelectorAll(".activity_image");

activities.forEach((activity) => {
    activity.addEventListener("click", () => {
        openChatBot(activity, activity.getAttribute("id"));
    });
});

let actividad = " "

function openChatBot(elem, context) {
    let card = elem.parentNode.parentNode;

    if (card.classList.contains("activity_left_up")) {
        actividad = "/inicio_hockey";
    } else if (card.classList.contains("activity_right_up")) {
        actividad = "/inicio_apoyo";
    } else if (card.classList.contains("activity_left_down")) {
        actividad = "/inicio_valores";
    } else if (card.classList.contains("activity_right_down")) {
        actividad = "/inicio_generico";
    }
    let content = card.children;
    document.getElementsByClassName("rw-launcher").item(0).click();
    document.dispatchEvent(new CustomEvent('actividadUpdated', { detail: actividad }));
}