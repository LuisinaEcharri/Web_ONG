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
            
            if str(actividad) == "hockey":
                print("hora hockey")
                dispatcher.utter_message("Cuantos años tenes")
            elif str(actividad) == "apoyo":
                print("hora apoyo")
                dispatcher.utter_message("Martes 17:15")
            elif str(actividad) == "arte":
                print("hora arte")
                dispatcher.utter_message("Martes 18:30")
            elif str(actividad) == "actividades":
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
            if str(actividad) == "hockey":
                dispatcher.utter_message("No hay que llevar nada")
            elif str(actividad) == "apoyo":
                dispatcher.utter_message("La mochila del colegio")
            elif str(actividad) == "arte":
                dispatcher.utter_message("No hay que llevar nada")
            elif str(actividad) == "actividades":
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
       
            if str(actividad) == "hockey":
                dispatcher.utter_message("Una hora y media, ya que es conjunto con el taller de valores")
            elif str(actividad) == "apoyo":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "arte":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "musica":
                dispatcher.utter_message("Una hora")
            elif str(actividad) == "actividades":
                dispatcher.utter_message("no hay actividades por el momento")
            elif str(actividad) == "valores":
                dispatcher.utter_message("Una hora y media, ya que es conjunto con hockey")
            return []
        
class ActionInicio(Action):

    hock = False 
    apoy= False
    gen = False
    act = False
    
    def name(self) -> Text:        
       return "action_inicio"   

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")

            if str(actividad) == "hockey":
                print("entro hockey")
                ## revise si el slot hockey esta activo
                ## cuando va de hockey a apoyo y vuelve a hockey el slot hockey se active de nuevo
                if (self.hock):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola,¿Que te gustaria saber sobre hockey?")
                self.hock = True
                return []

            elif str(actividad) == "apoyo":
                print("entro apoyo")
                if (self.apoy):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola,¿Que te gustaria saber sobre el taller de apoyo escolar?")
                self.apoy= True
                return []

            elif str(actividad) == "generico":
                print("entro generico")
                if(self.gen):
                    dispatcher.utter_message("Hola, volviste, ¿ sobre cual necesitas saber: musica, arte o valores?")
                else:
                    dispatcher.utter_message("Hola, brindamos talleres de valores, arte y musica ¿sobre cual te gustaria saber?")
                self.gen = True
                return []
            
            elif str(actividad) == "actividades":
                print("entro actividades")
                if (self.act):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola, por el momento no hay actividades")
                self.act = True
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
    
    
