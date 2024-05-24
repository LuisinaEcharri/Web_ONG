window.WebChat = {
    default: function (options, element) {


        let userId;
        if (localStorage.getItem("userId")) {
            userId = localStorage.getItem("userId");
        } else {
            userId = uuidv4();
            localStorage.setItem("userId", userId);
        }

        const backend = new backRasa('http://localhost:5006');
        const chatContainer = document.createElement('div');
        chatContainer.id = 'chat-container';
        chatContainer.style.position = 'fixed';
        chatContainer.style.top = '20%';
        chatContainer.style.left = '5%';
        chatContainer.style.width = '1000px';
        chatContainer.style.height = '380px';
        chatContainer.style.border = '1px solid #ccc';
        chatContainer.style.borderRadius = '55px 55px 55px 0px';
        chatContainer.style.backgroundColor = '#f1f1f1';
        chatContainer.innerHTML = `
            <div style="background-color: #f1f1f1; color: white; padding-top: 15px; padding-bottom: 10px; padding-left: 30px; border-radius: 55px 55px 0px 0px; border-bottom: 1.5px solid #EE002F">
                <img src="./img/backIconRed.svg" style=" height: 20px; width: 20px; padding-right: 15px; cursor: pointer" id="backButton">
                <img src="./img/botIcon.png" style="height: 25px; width: 30px">
            </div>
            <div id="messages" style="height: 250px; overflow-y: auto; padding: 10px;"></div>
            <input id="user-input" type="text" style="width: 95%; margin-left: 2.5%; padding-left: 15px; box-sizing: border-box; border-radius: 23px; height: 35px; border: none; font-family: 'Montserrat', sans-serif;" placeholder="Escribe un mensaje...">
        `;
        document.body.appendChild(chatContainer);
        

        document.getElementById('backButton').addEventListener('click', function () {
            const chatContainer = document.getElementById('chat-container');
            if (chatContainer) {
                chatContainer.remove();
            }
        });

        const messagesContainer = document.getElementById('messages');
        const userInput = document.getElementById('user-input');
        let messageList = [];

        addMessageToUI("¡Hola! Soy tu asistente virtual y estoy para ayudarte. \n¿Querías agregar o eliminar una noticia?", false);

        function addMessageToUI(message, fromUser) {
            const userMessageContainer = document.createElement('div');
            userMessageContainer.style.display = 'flex'; // Establece el contenedor como flexbox
            userMessageContainer.style.justifyContent = fromUser ? 'flex-end' : 'flex-start'; // Alinea los elementos al final del contenedor
            messagesContainer.appendChild(userMessageContainer);
            const messageDiv = document.createElement('div');
            messageDiv.textContent = message;
            messageDiv.style.textAlign = fromUser ? 'right' : 'left';
            messageDiv.style.backgroundColor = fromUser ? '#EE002F' : '#FFF';
            messageDiv.style.color = fromUser ? '#fff' : '#000';
            messageDiv.style.fontFamily = 'Montserrat, sans-serif';
            messageDiv.style.padding = '10px';
            messageDiv.style.borderRadius = fromUser ? '25px 0px 25px 25px' : '0px 25px 25px 25px';
            messageDiv.style.width = 'fit-content';
            messageDiv.style.maxWidth = '490px';
            messageDiv.style.overflowWrap = 'break-word';
            messageDiv.style.fontSize = '12px';
            messageDiv.style.fontWeight = 'bold';
            userMessageContainer.appendChild(messageDiv);
            userMessageContainer.scrollTop = userMessageContainer.scrollHeight;
        }

        userInput.addEventListener('keypress', async function (event) {
            if (event.key === 'Enter') {
                const message = event.target.value;
                if (message.trim() !== '') {
                    addMessageToUI(message, true);
                    event.target.value = '';
                    const response = await sendMessage(message);
                    response.forEach(msg => {
                        if (msg.text) {
                            addMessageToUI(msg.text, false);
                        } else if (msg.image) {
                            const img = document.createElement('img');
                            img.src = msg.image;
                            img.style.maxWidth = '100%';
                            messagesContainer.appendChild(img);
                        }
                    });
                }
            }
        });

        async function loadMessage() { //carga la conversacion
            const messages = await backend.getConversationMessages(await backend.getIdConversation(userId))
            if (messages.length >= 0) {
                messageList = [...messageList, ...messages]
            } else {
                console.log("No hay mensajes")
                messageList.push(messages)
            }
        }

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
            return response;
        }

        async function sendMessage(message) {
            const response = await backend.sendMessageToAgent(message, userId);
            //await loadMessage() //carga la conversacion
            let messageResponse = {
                sender: "ReInventar",
                receiver: response[0].receiver,
                text: response[0].text,
                image: response[0].image,
                timestamp: Date.now() / 1000
            };
            messageList.push(messageResponse)
            return response;
        }



    }
};