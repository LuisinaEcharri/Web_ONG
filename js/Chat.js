(() => {
    let userId // le asigna un id al usuario para diferenciarlo con otros
    if (localStorage.getItem("userId")) { // si ya existe un id de usuario en el local storage, lo toma para levantar el flujo anterior
        userId = localStorage.getItem("userId")
    } else {
        userId = uuidv4() // si no existe un id de usuario en el local storage, le asigna un id nuevo
        localStorage.setItem("userId", userId)
    }
    const backend = new backRasa('http://localhost:5005'); //Cambiar a IP publica
    const title = document.getElementById("titulo-contenedor")
    const chat = document.querySelector(".chat-conteiner");
    const btnOpen = document.getElementById("modal-button-chat");
    //const messageList = [] //guarda los mensajes de la conversacion
    const chatMessages = document.body.querySelector(".chat-column.chat-window-log");
    const userMessageTemplate = chatMessages.querySelector(".from-me").cloneNode(true) //clona el mensaje del usuario
    const agentMessageTemplate = chatMessages.querySelector(".from-them").cloneNode(true) //clona el mensaje del agente
    const btnForm = document.getElementById("form-send-text");
    const messageInput = document.getElementById("input-message")
    let activities = document.querySelectorAll(".activity_image");
    //let btnOpen = document.getElementById("modal-button-chat");
    //const close = document.querySelectorAll("button.rw-launcher.rw-hide-sm");
    let messageListHockey = [];
    let messageListTaller = [];
    let messageEducativo = [];
    let messageListActivi = [];
    let messageList = [];
    let actividad = "";
    let silenceMessage = "";

    activities.forEach((activity) => {
        activity.addEventListener("click", () => {
            //paso por parametro el card y el messageList correspondiente dependiendo de la actividad
            let card = activity.parentNode.parentNode;
            let NombreTitulo
            if (card.classList.contains("activity_left_up")) {
                messageList = messageListHockey.slice();
                actividad = "hockey";
                NombreTitulo = "Hockey"
                silenceMessage = "Se activo boton hockey"
            } else if (card.classList.contains("activity_left_down")) {
                messageList = messageListTaller.slice();
                actividad = "generico";
                NombreTitulo = "Taller educativo"
                silenceMessage = "Se activo boton generico"
            } else if (card.classList.contains("activity_right_up")) {
                messageList = messageEducativo.slice();
                actividad = "apoyo";
                NombreTitulo = "Apoyo escolar"
                silenceMessage = "Se activo boton apoyo"
            } else if (card.classList.contains("activity_right_down")) {
                messageList = messageListActivi.slice();
                actividad = "actividades";
                NombreTitulo = "Actividades recreativas"
                silenceMessage = "Se activo boton de actividades"
            }
            title.innerHTML = `ReInventar ${NombreTitulo}`
            btnOpen.click();
        });
    });

    //un listener del boton, cuando se clickea se abre el chat
    btnOpen.addEventListener('click', (async(e) => {
        e.preventDefault() //  Esto es una práctica común para asegurarse de que el comportamiento deseado se ejecute sin interferencias.
        sendMessageSilence(silenceMessage)
        refreshMessageList() //realmente lo carga en el chat (vista final para el usuario)
        chat.style.display = "flex";
        btnOpen.style.display = "none"
        btnClose.style.display = "flex";
        const sb = document.querySelector(".chat-window-log");
        sb.scrollTop = sb.scrollHeight;
    }));

    async function sendMessageSilence(message) {
        console.log("Enviando mensaje de silencio", message)
        const response = await backend.sendMessageToAgent(message, userId) //envia el mensaje al agente
        console.log(response)
        let messageResponse = {
            sender: "ReInventar",
            receiver: response[0].receiver,
            text: response[0].text,
            image: response[0].image,
            timestamp: Date.now() / 1000
        };
        messageList.push(messageResponse)
        refreshMessageList() //actualiza la vista del chat
    }

    const btnClose = document.getElementById("modal-button-chat-off");
    btnClose.addEventListener('click', ((e) => {
        e.preventDefault()
        chat.style.display = "none";
        btnOpen.style.display = "inline-block";
        btnClose.style.display = "none";
        loadConversation();
    }));
    const btnCloseMini = document.getElementById("modal-button-chat-off-1");
    btnCloseMini.addEventListener('click', ((e) => {
        e.preventDefault()
        clearChatMessages();
        chat.style.display = "none";
        btnOpen.style.display = "inline-block";
        btnClose.style.display = "none";
        loadConversation();
    }));

    async function loadConversation() {
        if (actividad === "hockey") {
            messageListHockey = messageList;
            messageList = [];
        } else if (actividad === "generico") {
            messageListTaller = messageList;
            messageList = [];
        } else if (actividad === "apoyo") {
            messageEducativo = messageList;
            messageList = [];
        } else if (actividad === "actividades") {
            messageListActivi = messageList;
            messageList = [];
        }

    }
    btnForm.addEventListener('submit', ((e) => {
        e.preventDefault();
        sendMessage(messageInput.value)
        messageInput.value = ""
    }));

    async function loadMessage() { //carga la conversacion
        const messages = await backend.getConversationMessages(await backend.getIdConversation(userId))
        if (messages.length >= 0) {
            messageList = [...messageList, ...messages]
        } else {
            console.log("No hay mensajes")
            messageList.push(messages)
        }
    }

    function clearChatMessages() {
        chatMessages.innerHTML = ""; //limpia el guardador de mensajes del chat
    }

    async function sendMessage(message) {
        const response = await backend.sendMessageToAgent(message, userId) //envia el mensaje al agente
        await loadMessage() //carga la conversacion
        let messageResponse = {
            sender: "ReInventar",
            receiver: response[0].receiver,
            text: response[0].text,
            image: response[0].image,
            timestamp: Date.now() / 1000
        };
        messageList.push(messageResponse)
        refreshMessageList() //actualiza la vista del chat
    }

    function refreshMessageList() {
        clearChatMessages()
        for (const message of messageList) {
            let chatMessage
            if (message.sender === "ReInventar") {
                chatMessage = agentMessageTemplate.cloneNode(true) // asigna quien es el emisor del mensaje
            } else {
                chatMessage = userMessageTemplate.cloneNode(true) // asigna quien es el emisor del mensaje
            }
            if (message.text) {
                chatMessage.querySelector("p").innerText = message.text //asigna el texto del mensaje
            } else if (message.image) {
                chatMessage.querySelector("p").innerHTML = ` < img src = "${message.image}"
                                style = "width: 100%" / > ` //a futuro
            } else {
                chatMessage.querySelector("p").innerHTML = "<i>Unsupported message</i>"
            }
            const div = document.createElement("div")
            div.style.fontSize = "0.65em"
            div.style.marginTop = "-12px"
            div.style.padding = "10px 9px 0px"
            div.style.fontStyle = "italic"
            div.style.opacity = "0.6"
            div.innerText = dayjs.unix(message.timestamp).format("DD/MM/YYYY HH:mm:ss")
            chatMessages.appendChild(chatMessage)
            chatMessage.appendChild(div)
        } //formato por si lo queremos cambiar.
        chatMessages.scrollTo(0, chatMessages.scrollHeight) //hace scroll automatico al final del chat caundo se envia el mensaje
    }

    function toggleVisibility(element) {
        if (element.style.display === "none") {
            element.style.display = "block"
        } else {
            element.style.display = "none"
        }
    }
})()