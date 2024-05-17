const activities = document.querySelectorAll(".activity_image");
//const close = document.querySelectorAll("button.rw-launcher.rw-hide-sm");
let entro = false;
activities.forEach((activity) => {
    activity.addEventListener("click", () => {
        // Check for existing instance before creating a new one
        if (!activity.hasAttribute('data-chatbot-instance')) {
            createChatBotInstance(activity, activity.getAttribute("id"));
            setTimeout(function() {
                // Access and open the chatbot interface (assuming WebChat library methods)
                const instanceId = activity.getAttribute('data-chatbot-instance');
                console.log("Opening chatbot for new instance:", instanceId);
                document.getElementsByClassName("rw-launcher").item(0).click();
                const closeButton = document.querySelector("button.rw-launcher.rw-hide-sm");
                closeButton.addEventListener("click", () => {
                    console.log("entro");
                    //if (!entro) {
                    removeChatBotInstance(activity, activity.getAttribute("id"));
                    //}
                    //entro = true;
                });
            }, 1000);
        } else {
            console.log("ChatBot instance already exists for this activity.");
            // Access and open the chatbot interface (assuming WebChat library methods)
            const instanceId = activity.getAttribute('data-chatbot-instance');
            console.log("Opening chatbot for existing instance:", instanceId);
            document.getElementsByClassName("rw-launcher").item(0).click();

            // const closeButton = document.querySelector("button.rw-launcher.rw-hide-sm");
            // if (closeButton) {
            //     closeButton.addEventListener("click", () => {
            //         console.log("entro");
            //         removeChatBotInstance(activity, instanceId);
            //     });
            // }
        }
    });
});

function createChatBotInstance(actividad, context) {
    let card = actividad.parentNode.parentNode;

    // Determine activity based on class names
    let actividadUrl;
    if (card.classList.contains("activity_left_up")) {
        actividadUrl = "/inicio_hockey";
    } else if (card.classList.contains("activity_right_up")) {
        actividadUrl = "/inicio_apoyo";
    } else if (card.classList.contains("activity_left_down")) {
        actividadUrl = "/inicio_generico";;
    } else if (card.classList.contains("activity_right_down")) {
        actividadUrl = "/inicio_actividades";
    }

    let content = card.children;

    // Create script element dynamically without polluting global scope
    const script = document.createElement("script");
    script.src = "./js/index.js";
    script.async = true;

    // Store instance ID for later removal
    const instanceId = Math.random().toString(36).substring(2, 15); // Generate unique ID
    actividad.setAttribute('data-chatbot-instance', instanceId);

    script.onload = () => {

        window.localStorage.clear();
        window.sessionStorage.clear();

        // Use window.WebChat instead of potentially global WebChat.default
        if (window.WebChat) {
            window.WebChat.default({
                initPayload: actividadUrl,
                socketUrl: "http://localhost:5005"
            }, null);
        } else {
            console.error("WebChat library not available. ChatBot creation failed.");
        }

        // Update to store a reference to the WebChat instance (if available)
        const webChatInstance = window.WebChat && window.WebChat.instances[context]; // Assuming context matches instance ID
        actividad.setAttribute('data-chatbot-instance', webChatInstance); // Or store reference directly in an object
    };

    // Add script element safely (recommended approach)
    const head = document.head || document.getElementsByTagName("head")[0];
    head.insertBefore(script, head.firstChild);

    // Add removal functionality (consider using a button or event listener)
    // Replace with your desired removal logic (e.g., button click event)
    // close.forEach(boton => {
    //     boton.addEventListener("click", () => {
    //         console.log("entro");
    //         removeChatBotInstance(actividad, instanceId);
    //     });
    // });

}

function removeChatBotInstance(actividad, instanceId) {
    const scripts = document.querySelectorAll('script');
    console.log(scripts);
    for (const script of scripts) {
        // if (script.src.includes('./js/index.js') && script.parentNode) {
        console.log("entro removeinstance");
        script.parentNode.removeChild(script);
        actividad.removeAttribute('data-chatbot-instance');
        break; // Remove only the first matching script (assuming one per activity)
        // }
    }
}