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
        let file = null;
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
            <div style="display: flex; justify-content: space-between;"> 
                <div style="width: 95%;"> 
                    <input id="user-input" type="text" style="width: 98%; margin-left: 2.5%; padding-left: 15px; box-sizing: border-box; border-radius: 23px; height: 35px; border: none; font-family: 'Montserrat', sans-serif;" required placeholder="Escribe un mensaje...">
                    <div id="selected-container" style="display:none; margin-top: 2px;"> 
                        <div id="selected-file" style="font-family: 'Montserrat', sans-serif; color: #EE002F; font-size: 10px;  margin-left: 4.5%; "></div>
                        <img id="delete-file" src="./img/close.svg" style="height: 15px; width: 15px; margin-left: 7px; cursor: pointer;">
                    </div>
                </div>
                <input id="file-input" type="file" accept="image/*" style="display: none;">
                <img id="file-button" src="./img/paperclip.svg" style="height: 20px; width: 25px;  margin-left: 10px; margin-right: 10px; padding-top:7px">
            </div>
            
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
        const fileInput = document.getElementById('file-input');
        const fileButton = document.getElementById('file-button');
        const selectedFile = document.getElementById("selected-file");
        const selectedDiv = document.getElementById("selected-container");
        let messageList = [];
        let fileData = null;
        const route = "../img/noticias/"

        addMessageToUI("¡Hola! Soy tu asistente virtual y estoy para ayudarte. \n¿Querías agregar o eliminar una noticia?", false);

        function addMessageToUI(message, fromUser) {
            const userMessageContainer = document.createElement('div');
            userMessageContainer.style.display = 'flex'; // Establece el contenedor como flexbox
            userMessageContainer.style.justifyContent = fromUser ? 'flex-end' : 'flex-start'; // Alinea los elementos al final del contenedor
            messagesContainer.appendChild(userMessageContainer);
            const messageDiv = document.createElement('div');
            if (message instanceof HTMLImageElement) {
                messageDiv.appendChild(message);
                messageDiv.style.padding = "15px"
            } else {
                messageDiv.textContent = message;
                messageDiv.style.padding = '10px';
            }
            messageDiv.style.textAlign = fromUser ? 'right' : 'left';
            messageDiv.style.backgroundColor = fromUser ? '#EE002F' : '#FFF';
            messageDiv.style.color = fromUser ? '#fff' : '#000';
            messageDiv.style.fontFamily = 'Montserrat, sans-serif';
            messageDiv.style.borderRadius = fromUser ? '25px 0px 25px 25px' : '0px 25px 25px 25px';
            messageDiv.style.width = 'fit-content';
            messageDiv.style.maxWidth = '490px';
            messageDiv.style.overflowWrap = 'break-word';
            messageDiv.style.fontSize = '12px';
            messageDiv.style.fontWeight = 'bold';
            messageDiv.style.marginBottom = "10px";
            userMessageContainer.appendChild(messageDiv);
            userMessageContainer.scrollTop = userMessageContainer.scrollHeight;
        }


        userInput.addEventListener('keypress', async function (event) {
            if (event.key === 'Enter') {
                let message = event.target.value;
                if (message.trim() !== '') {
                    addMessageToUI(message, true);
                    event.target.value = '';
                    if (file) {
                        const img = document.createElement('img');
                        img.src = URL.createObjectURL(file);
                        img.style.maxWidth = '100%';
                        addMessageToUI(img, true);
                        message = message + ". Imagen: " + route + file.name;
                        selectedFile.textContent = "";
                        selectedDiv.style.display = "none";
                    }
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

        fileInput.addEventListener('change', async function (event) {
            
            if (event.target.files[0]) {
                file = event.target.files[0];
                fileData = new FormData();
                fileData.append('image', file);
                selectedFile.textContent = file.name;
                selectedDiv.style.display = "flex"
            } else {
                selectedFile.textContent = ""
                selectedDiv.style.display = "none"
            }
            event.target.file = '';
        });


        fileButton.addEventListener('click', function (event) {
            fileInput.click();
        });

        document.getElementById("delete-file").addEventListener("click", function(event){
            file = null;
            fileData = null;
            selectedFile.textContent = "";
            selectedDiv.style.display = "none";
        })

        async function loadMessage() { //carga la conversacion
            const messages = await backend.getConversationMessages(await backend.getIdConversation(userId))
            if (messages.length >= 0) {
                messageList = [...messageList, ...messages]
            } else {
                console.log("No hay mensajes")
                messageList.push(messages)
            }
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
            if (messageResponse.text.startsWith("Noticia guardada correctamente.")) {
                uploadImage();
            }
            file = null;
            fileData = null;
            messageList.push(messageResponse)
            return response;
        }

        function uploadImage() {

            fetch('./php/upload_image.php', {
                method: 'POST',
                body: fileData
            })
                .then(response => console.log(response.text()))
                .catch(error => {
                    console.error('Error:', error);
                });


        }



    }
};