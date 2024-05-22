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
                ## revise si el slot hockey esta activo
                ## cuando va de hockey a apoyo y vuelve a hockey el slot hockey se active de nuevo
                if (self.hock):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola,¿Que te gustaria saber sobre hockey?")
                SlotSet("apoyo",'false')
                SlotSet("musica",'false')
                SlotSet("arte",'false')
                SlotSet("valores",'false')
                SlotSet("generico",'false')
                SlotSet("actividades",'false')
                self.hock = True
                return [SlotSet("hockey",'true')]

            elif str(actividad) == "apoyo":
                if (self.apoy):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola,¿Que te gustaria saber sobre el taller de apoyo escolar?")
                SlotSet("hockey",'false')
                SlotSet("musica",'false')
                SlotSet("arte",'false')
                SlotSet("valores",'false')
                SlotSet("generico",'false')
                SlotSet("actividades",'false')
                self.apoy= True
                return [SlotSet("apoyo",'true')]

            elif str(actividad) == "generico":
                if(self.gen):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola, brindamos talleres de valores, arte y musica ¿sobre cual te gustaria saber?")
                SlotSet("hockey",'false')
                SlotSet("musica",'false')
                SlotSet("arte",'false')
                SlotSet("valores",'false')
                SlotSet("apoyo",'false')
                SlotSet("actividades",'false')
                self.gen = True
                return [SlotSet("generico",'true')]
            
            elif str(actividad) == "actividades":
                if (self.act):
                    dispatcher.utter_message("Hola, volviste, que necesitas saber")
                else:
                    dispatcher.utter_message("Hola, por el momento no hay actividades")
                SlotSet("hockey",'false')
                SlotSet("musica",'false')
                SlotSet("arte",'false')
                SlotSet("valores",'false')
                SlotSet("apoyo",'false')
                SlotSet("generico",'false')
                self.act = True
                return [SlotSet("actividades",'true')]
            return []
        
         
class ActionInicioGenerico(Action):

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
    
    
