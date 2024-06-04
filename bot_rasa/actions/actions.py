# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHorarioHockey(Action):

   def name(self) -> Text:
       return "horarios_hockey"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            edad = tracker.get_slot("anios")
            print(edad)

            if int(edad) > 6:
                dispatcher.utter_message("Lunes 18:15, miercoles 18:30 y sabados 11:00")

            elif int(edad) < 5:
                dispatcher.utter_message("es a partir de los 5 años")
            
            elif int(edad) > 18:
                dispatcher.utter_message("es hasta los 18 años")
            else:
                dispatcher.utter_message("sabados 11:00")

            return []
class ActionHorarios(Action):

   def name(self) -> Text:
       return "horarios_todos"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")
            
            if str(actividad) == "hockey" or str(actividad) == "hockeyagain":
                print("hora hockey")
                dispatcher.utter_message("Cuantos años tenes")
            elif str(actividad) == "apoyo" or str(actividad) == "apoyoagain":
                print("hora apoyo")
                dispatcher.utter_message("Martes 17:15")
            elif str(actividad) == "arte":
                print("hora arte")
                dispatcher.utter_message("Martes 18:30")
            elif str(actividad) == "actividades" or str(actividad) == "actividadesagain":
                print("hora actividades")
                dispatcher.utter_message("no hay actividades por el momento")
            elif str(actividad) == "musica":
                print("hora musica")
                dispatcher.utter_message("Viernes 14:30")
            elif str(actividad) == "valores":
                print("hora valores")
                dispatcher.utter_message("Cuantos años tenes")
            return []

class ActionLlevarCosas(Action):

   def name(self) -> Text:
       return "llevar_cosas"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")
            if str(actividad) == "hockey" or str(actividad) == "hockeyagain":
                dispatcher.utter_message("No hay que llevar nada")
            elif str(actividad) == "apoyo" or str(actividad) == "apoyoagain":
                dispatcher.utter_message("La mochila del colegio")
            elif str(actividad) == "arte":
                dispatcher.utter_message("No hay que llevar nada")
            elif str(actividad) == "actividades" or str(actividad) == "actividadesagain":
                dispatcher.utter_message("no hay actividades por el momento")
            elif str(actividad) == "musica":
                dispatcher.utter_message("No hay que llevar nada")
            elif str(actividad) == "valores":
                dispatcher.utter_message("No hay que llevar nada")
            return []

class ActionDuracionTodos(Action):

   def name(self) -> Text:
       return "duracion_todos"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")
       
            if str(actividad) == "hockey" or str(actividad) == "hockeyagain":
                dispatcher.utter_message("Una hora y media, ya que es conjunto con el taller de valores")
            elif str(actividad) == "apoyo" or str(actividad) == "apoyoagain":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "arte":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "musica":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "actividades" or str(actividad) == "actividadesagain":
                dispatcher.utter_message("no hay actividades por el momento")
            elif str(actividad) == "valores":
                dispatcher.utter_message("Una hora y media, ya que es conjunto con hockey")
            return []
        
class ActionInicio(Action):
    
    def name(self) -> Text:        
       return "action_inicio"   

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")

            if str(actividad) == "hockey":
                dispatcher.utter_message("Hola,¿Que te gustaria saber sobre hockey?")
                return []

            elif str(actividad) == "apoyo":
                dispatcher.utter_message("Hola,¿Que te gustaria saber sobre el taller de apoyo escolar?")
                return []

            elif str(actividad) == "generico":
                dispatcher.utter_message("Hola, brindamos talleres de valores, arte y musica ¿sobre cual te gustaria saber?")
                return []
                
            elif str(actividad) == "actividades":
                dispatcher.utter_message("Hola, no hay actividades por el momento")
                return []

            elif str(actividad) == "hockeyagain":
                dispatcher.utter_message("Hola volviste, ¿Que mas gustaria saber sobre hockey?")
                return []
                
            elif str(actividad) == "apoyoagain":
                dispatcher.utter_message("Hola volviste, ¿Que mas gustaria saber sobre el taller de apoyo escolar?")
                return []

            elif str(actividad) == "genericoagain":
                dispatcher.utter_message("Hola volviste, ¿sobre que te gustaria saber mas: musica, arte o valores?")
                return []
                
            elif str(actividad) == "actividadesagain":
                dispatcher.utter_message("Hola volviste, sigue sin haber actividades")
                return []
            return []
        
         
class ActionInformacion(Action):

   def name(self) -> Text:
       return "action_informacion"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")

            if str(actividad) == "musica":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de musica?")
                return []
            
            elif str(actividad) == "arte":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de arte?")
                return []
            
            elif str(actividad) == "valores":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de valores?")
                return []
            return []
    

class Actionfalta(Action):

    def name(self) -> str:
        return "action_falta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        nombre = tracker.get_slot("nombre")
        numero = tracker.get_slot("numero")
        faltante = tracker.get_slot("item")
        print(nombre)
        print(numero)
        print(faltante)
        
        if nombre and faltante:
            file_path = "necesidades.txt"
            with open(file_path, "a") as file:
                file.write(f"Nombre: {nombre}, Telefono: {numero}, Necesita: {faltante}\n")
            dispatcher.utter_message(text="Gracias. He guardado tu información, pronto nos comunicaremos contigo")
        else:
            dispatcher.utter_message(text="Lo siento, no he podido obtener tu información correctamente.")

        return []
    
class ActionGetLastUserMessage(Action):

    def name(self) -> Text:
        return "action_ultimo_mensaje"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_user_message = tracker.latest_message.get('text')
        print(last_user_message)
        
        dispatcher.utter_message(text="Por favor dame tu nombre, apellido y numero de telefono")

        last_intent = tracker.latest_message["intent"]["name"]

        if last_intent == "negacion":
            return [SlotSet("item", last_user_message)]
        return[]