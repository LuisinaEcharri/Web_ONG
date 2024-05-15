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

class ActionHorario(Action):

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
   
class ActionInicioHockey(Action):

   def name(self) -> Text:
       return "inicio_actividad_hockey"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            print("entro hockey")
            #dispatcher.utter_message("Hola, ¿que te gustaria saber sobre hockey?")
            SlotSet("apoyo",'false')
            SlotSet("musica",'false')
            SlotSet("arte",'false')
            SlotSet("valores",'false')
            SlotSet("generico",'false')
            SlotSet("actividades",'false')
            return [SlotSet("hockey",'true')]
 
class ActionInicioApoyo(Action):

   def name(self) -> Text:
       return "inicio_actividad_apoyo"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            #dispatcher.utter_message("Hola, ¿que te gustaria saber sobre hockey?")
            print("entro apoyo")
            SlotSet("hockey",'false')
            SlotSet("musica",'false')
            SlotSet("arte",'false')
            SlotSet("valores",'false')
            SlotSet("generico",'false')
            SlotSet("actividades",'false')
            return [SlotSet("apoyo",'true')]
         
class ActionInicioMusica(Action):

    def name(self) -> Text:
        return "inicio_actividad_musica"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            #dispatcher.utter_message("Hola, ¿que te gustaria saber sobre hockey?")
            SlotSet("hockey",'false')
            SlotSet("apoyo",'false')
            SlotSet("arte",'false')
            SlotSet("valores",'false')
            SlotSet("generico",'false')
            SlotSet("actividades",'false')
            return [SlotSet("musica",'true')]

class ActionInicioGenerico(Action):

    def name(self) -> Text:
        return "inicio_actividad_generico"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            #dispatcher.utter_message("Hola, ¿que te gustaria saber sobre hockey?")
            SlotSet("hockey",'false')
            SlotSet("apoyo",'false')
            SlotSet("arte",'false')
            SlotSet("valores",'false')
            SlotSet("musica",'false')
            SlotSet("actividades",'false')
            return [SlotSet("generico",'true')]

class ActionInicioActividades(Action):

    def name(self) -> Text:
        return "inicio_actividad_actividades"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message("Hola, por el momento no hay actividades")
            SlotSet("hockey",'false')
            SlotSet("apoyo",'false')
            SlotSet("arte",'false')
            SlotSet("valores",'false')
            SlotSet("generico",'false')
            SlotSet("musica",'false')
            return [SlotSet("actividades",'true')]
         
class ActionInicio(Action):

   def name(self) -> Text:
       return "action_informacion"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")

            if str(actividad) == "musica":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de musica?")
                SlotSet("arte",'false')
                SlotSet("apoyo",'false')
                SlotSet("hockey",'false')
                SlotSet("valores",'false')
                SlotSet("generico",'false')
                SlotSet("actividades",'false')
                return [SlotSet("musica",'true')]
            
            elif str(actividad) == "arte":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de arte?")
                SlotSet("apoyo",'false')
                SlotSet("musica",'false')
                SlotSet("hockey",'false')
                SlotSet("valores",'false')
                SlotSet("generico",'false')
                SlotSet("actividades",'false')
                return [SlotSet("arte",'true')]
            
            elif str(actividad) == "valores":
                dispatcher.utter_message("¿Que te gustaria saber sobre el taller de valores?")
                SlotSet("apoyo",'false')
                SlotSet("musica",'false')
                SlotSet("hockey",'false')
                SlotSet("arte",'false')
                SlotSet("generico",'false')
                SlotSet("actividades",'false')
                return [SlotSet("valores",'true')]
            return []
    
    
