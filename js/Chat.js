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
    const messageList = [] //guarda los mensajes de la conversacion
    const chatMessages = document.body.querySelector(".chat-column.chat-window-log");
    const userMessageTemplate = chatMessages.querySelector(".from-me").cloneNode(true) //clona el mensaje del usuario
    const agentMessageTemplate = chatMessages.querySelector(".from-them").cloneNode(true) //clona el mensaje del agente
    const btnForm = document.getElementById("form-send-text");
    const messageInput = document.getElementById("input-message")



    //un listener del boton, cuando se clickea se abre el chat
    btnOpen.addEventListener('click', (async(e) => {
        e.preventDefault() //  Esto es una práctica común para asegurarse de que el comportamiento deseado se ejecute sin interferencias.
        refreshMessageList() //realmente lo carga en el chat (vista final para el usuario)
        chat.style.display = "flex";
        btnOpen.style.display = "none"
        btnClose.style.display = "flex";
        const sb = document.querySelector(".chat-window-log");
        sb.scrollTop = sb.scrollHeight;
    })); //los estilos para css

    const btnClose = document.getElementById("modal-button-chat-off");
    btnClose.addEventListener('click', ((e) => {
        e.preventDefault()
        chat.style.display = "none";
        btnOpen.style.display = "inline-block";
        btnClose.style.display = "none";
    }));
    const btnCloseMini = document.getElementById("modal-button-chat-off-1");
    btnCloseMini.addEventListener('click', ((e) => {
        e.preventDefault()
        chat.style.display = "none";
        btnOpen.style.display = "inline-block";
        btnClose.style.display = "none";
    }));


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
                chatMessage.querySelector("p").innerHTML = `<img src="${message.image}" style="width: 100%"/>` //a futuro
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