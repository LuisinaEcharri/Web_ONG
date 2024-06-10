
import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import ActionExecutor
import streamlit as st
import os
import google.generativeai as genai
import json
import requests
from dotenv import load_dotenv


load_dotenv()


# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


class TalkAction(Action):

    def name(self) -> Text:
        return "talk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print(os.getenv("GOOGLE_API_KEY"))
        # Obtener el texto de la noticia del usuario
        text = tracker.latest_message.get("text")
        # Utilizar Gemini para generar la noticia
        response = model.generate_content(text).candidates[0].content.parts[0].text
        
        #print(response)
        # Acceder a la lista de candidatos dentro del atributo result
        # candidates = response.candidates

        # # Verificar si hay candidatos
        # if candidates:
        # # Acceder al primer candidato
        #     first_candidate = candidates[0]

        # # Acceder al texto dentro del atributo content del primer candidato
        #     response_text = first_candidate.content.parts[0].text
    
        dispatcher.utter_message(text=str(response))

        return []


class GenerateNewAction(Action):

    def name(self) -> Text:
        return "generate_new"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        # Obtener el texto de la noticia del usuario
        news_text = tracker.latest_message.get("text")

        text = "Quisiera que me formatees el siguiente texto que te voy a pasar. Es una noticia y necesito que quede para ponerlo directamente en un archivo con la siguiente estructura {\"Titulo\": \"....\", \"Epigrafe\": \"...\", \"Cuerpo\": \"...\", \"Imagen\": \"...\"}, donde las claves sean Titulo, Epigrafe y Cuerpo con sus correspondientes valores. Si te especifican un titulo necesito que lo dejes como esta, pero sino inventale uno. Si te especifican un epigrafe dejalo como esta, sino creale uno simple. Siempre incluí un cuerpo por favor. Para la imagen ponele el link/enlace que te pasen, sin importar si es un link de internet o una ruta de un archivo, dejalo como esta. Si no te pasan nada no le agregues nada, ni siquiera le agregues la parte de \"Imagen:\", no agregues nada."
        text = str(text + news_text)
        # Utilizar Gemini para generar la noticia
        response = model.generate_content(text).candidates[0].content.parts[0].text
        print(response)
        news_data = json.loads(response)
        # Validar y formatear la respuesta
        news_data = self.format_response(response)
        if not news_data:
            dispatcher.utter_message(text="Hubo un error al procesar la noticia generada.")
            return []
        
        # Enviar la información a través de una petición POST
        url = "http://localhost/Web_ONG/bot_noticias/actions/save_new.php"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(news_data))
        if response.status_code == 200:
            dispatcher.utter_message(text="Noticia guardada correctamente. \n La noticia que se publicó es:\n" + str(news_data))
        else:
            dispatcher.utter_message(text="Hubo un error al guardar la noticia.")
        #dispatcher.utter_message(text=str("Genial. Se guardó la siguiente noticia: ") + str(news_data))


        return [SlotSet("texto", None)]
    
    def format_response(self, response_text: str) -> Dict[Text, Any]:
        # Expresiones regulares para extraer las partes del texto
        title_pattern = re.compile(r'"?Titulo"?:\s?"(.*?)"[,}]', re.IGNORECASE)
        epigrafe_pattern = re.compile(r'"?Epigrafe"?:\s?"(.*?)"[,}]', re.IGNORECASE)
        cuerpo_pattern = re.compile(r'"?Cuerpo"?:\s?"(.*?)"[,}]', re.IGNORECASE)
        imagen_pattern = re.compile(r'"?Imagen"?:\s?"(.*?)"[,}]', re.IGNORECASE)

        title_match = title_pattern.search(response_text)
        epigrafe_match = epigrafe_pattern.search(response_text)
        cuerpo_match = cuerpo_pattern.search(response_text)
        imagen_match = imagen_pattern.search(response_text)

        # Extraer y validar las partes
        title = title_match.group(1) if title_match else "Título generado automáticamente"
        epigrafe = epigrafe_match.group(1) if epigrafe_match else "Epígrafe generado automáticamente"
        cuerpo = cuerpo_match.group(1) if cuerpo_match else response_text  # Si no se encuentra, usar todo el texto
        imagen = imagen_match.group(1) if imagen_match else "../welcome.jpeg"

        # Crear el diccionario con los datos formateados
        news_data = {
            "Titulo": title,
            "Epigrafe": epigrafe,
            "Cuerpo": cuerpo,
            "Imagen": imagen
        }

        return news_data
    

# ------------------------flujo eliminar noticia
class ValidateEliminarNoticiaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_eliminar_noticia_form"

    def validate_texto(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        
        new_title = tracker.latest_message.get("text")
        print(new_title)
        # Preparar la URL del script PHP
        url = "http://localhost/Web_ONG/bot_noticias/actions/get_new.php"
        headers = {'Content-Type': 'application/json'}
        
        # Crear el payload con el título de la noticia
        payload = {
            "Titulo": new_title
        }

        # Enviar la solicitud POST al script PHP
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()

        # Manejar la respuesta
        if response_data['status'] == 'success':
            news = response_data['data']
            message = ("\n\n"
                       f"Título: {news['titulo']}\n"
                       f"Epígrafe: {news['epigrafe']}\n"
                       f"Cuerpo: {news['cuerpo']}")
            dispatcher.utter_message(text=message)
            return {"texto": new_title}
        else:
            dispatcher.utter_message(text=response_data['message'])
            return {"texto": None}

    def validate_confirm_delete(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        confirm_delete = tracker.get_slot("confirm_delete")
        new_title = tracker.get_slot("texto")

        if confirm_delete:
            # Preparar la URL del script PHP
            url = "http://localhost/Web_ONG/bot_noticias/actions/delete_new.php"
            headers = {'Content-Type': 'application/json'}
            
            # Crear el payload con el título de la noticia
            payload = {
                "Titulo": new_title
            }

            # Enviar la solicitud POST al script PHP
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response_data = response.json()

            # Manejar la respuesta
            dispatcher.utter_message(text=response_data['message'])
        else:
            dispatcher.utter_message(text="Operación cancelada. La noticia no ha sido eliminada.")


# class GetNewAction(Action):

#     def name(self) -> Text:
#         return "get_new"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Obtener el texto de la noticia del usuario
#         new_title = tracker.latest_message.get("text")
#         print(new_title)
#         # Preparar la URL del script PHP
#         url = "http://localhost/Web_ONG/bot_noticias/actions/get_new.php"
#         headers = {'Content-Type': 'application/json'}
        
#         # Crear el payload con el título de la noticia
#         payload = {
#             "Titulo": new_title
#         }

#         # Enviar la solicitud POST al script PHP
#         response = requests.post(url, headers=headers, data=json.dumps(payload))
#         response_data = response.json()

#         # Manejar la respuesta
#         if response_data['status'] == 'success':
#             news = response_data['data']
#             message = (f"¿Estás seguro de que deseas eliminar la siguiente noticia?\n\n"
#                        f"**Título**: {news['titulo']}\n"
#                        f"**Epígrafe**: {news['epigrafe']}\n"
#                        f"**Cuerpo**: {news['cuerpo']}")
#             dispatcher.utter_message(text=message)
#         else:
#             dispatcher.utter_message(text=response_data['message'])
#             return []
        
class DeleteNewForm(Action):

    def name(self) -> Text:
        return "delete_new"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [SlotSet("confirm_delete", None), SlotSet("texto", None)]