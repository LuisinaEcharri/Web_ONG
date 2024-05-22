class backRasa {
    constructor(urlPuerto) {
        this.RasaApi = urlPuerto; //puerto para conectarse a la api de rasa
        this.AgenteBase = "data"; //nombre del agente base, posible error por que aca es donde nosotros debemos el nombre de la carpeta que contiene nuestro bot
        //o al menos eso entendi
    }

    //es el mensaje enviado por el usuario y el id del usuario y el id del agente
    async sendMessageToAgent(message, userId) {
        // const url = `${this.urlBaseApiCharlatan}/webhooks/rest/webhook/?receiver=${agentId}` //lo de reciver agentID me hace ruido por que no deberiamos tener un id si solo tenemos uno
        const url = `${this.RasaApi}/webhooks/rest/webhook` //esto deberia ser el nombre de la carpeta que contiene el bot
        const response = await fetch(url, { method: 'POST', body: JSON.stringify({ message, sender: userId }) }) //envia el mensaje al agente, espera una respuesta y la guarda en response
        if (response.ok) {
            const jsonResponse = await response.json();
            console.log(jsonResponse)
            return jsonResponse.map(backendMessage => ({
                sender: this.AgenteBase, //el nombre del que lo envia para que aparezca en el chat 
                receiver: backendMessage.recipient_id, //el nombre del que lo recibe para que aparezca en el chat
                text: backendMessage.text,
                image: backendMessage.image,
                timestamp: Date.now() / 1000
                    //guardar en una estructura el mensaje de la actividad 
            })); //????????????
        } else {
            throw new Error(`Error getting response from ReInventar rasa bot.`)
        }
    }

    // participante1 es el id del usuario, y el participante2 es el agente con el que uno quiere hablar
    // una variable mas para diferencias entre cards
    async getIdConversation(participant1) { //participante dos es el agente pero en nuestro caso deberia ser la card.
        //imprimir todos las conversiones posibles
        const response = await fetch(`${this.RasaApi}/conversations/${participant1}/tracker`)
        if (response.ok) {
            const jsonIdConversation = await response.json(); //obtiene la conversacion en formato json
            return jsonIdConversation.sender_id //devuelve la conversacion
        } else {
            throw new Error('Error getting id conversation.');
        }
    }


    async getConversationMessages(idConversation) {
        const response = await fetch(`${this.RasaApi}/conversations/${idConversation}/tracker`)
            //const response = await fetch(`${this.RasaApi}/conversations/${idConversation}/messages/${latestMessageTimestamp ? `?timestamp=${latestMessageTimestamp}` : "" }`)
            //obtiene el ultimo mensaje de la conversacion con esto logramos que solo recupere el mensaje que necesitamos para mostrar
        if (response.ok) {
            const jsonConversation = await response.json();
            const messages = jsonConversation.latest_message
            let messageUser = {
                sender: idConversation,
                receiver: messages.receiver,
                text: messages.text,
                image: messages.image,
                timestamp: Date.now() / 1000
            };
            return messageUser
        } else {
            throw new Error('Error getting conversation.');
        }
    }
}