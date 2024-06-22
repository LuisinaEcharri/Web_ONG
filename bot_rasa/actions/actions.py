# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from aifc import Error
from typing import Any, Text, Dict, List
import mysql.connector
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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

class ActionProfesoras(Action):

   def name(self) -> Text:
       return "action_profesoras"

   def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            actividad = tracker.get_slot("actividad")
            if str(actividad) == "hockey" or str(actividad) == "hockeyagain":
                dispatcher.utter_message("Agustina Ferreira, Melany Krimer, Sofia Ferreira")
            elif str(actividad) == "apoyo" or str(actividad) == "apoyoagain":
                dispatcher.utter_message("Melany Hernandez con un voluntario llamado Daniel")
            elif str(actividad) == "arte":
                dispatcher.utter_message("Melany Hernandez junto con Melany krimer")
            elif str(actividad) == "actividades" or str(actividad) == "actividadesagain":
                dispatcher.utter_message("no hay actividades por el momento")
            elif str(actividad) == "musica":
                dispatcher.utter_message("Melany hernandez taller de arte junto con Melany krimer")
            elif str(actividad) == "valores":
                dispatcher.utter_message("Agustina Ferreira, Melany Krimer, Sofia Ferreira")
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
        
        ropaTalle = ["pantalon", "remera", "pantalón", "musculosa", "camiseta", "campera", "buzo", "jean", "short", "zapatillas", "medias", "sweater", "sueter", "zapatos", "sandalias", "ojotas", "malla", "cinto", "cinturon"]

        nombre = tracker.get_slot("nombre")
        numero = tracker.get_slot("numero")
        faltante = tracker.get_slot("item")
        ropa = tracker.get_slot("ropa")
        print (ropa)
        if ropa in ropaTalle:
             dispatcher.utter_message(text="Me decis el talle por favor")
        else: 
            if nombre and faltante:
                file_path = "necesidades.txt"
                with open(file_path, "a") as file:
                    file.write(f"Nombre: {nombre}, Telefono: {numero}, Necesita: {faltante}\n")
                try:
                    connection = mysql.connector.connect(
                        host="localhost",  # Cambia esto por tu host
                        user="root",  # Cambia esto por tu usuario
                        password="",  # Cambia esto por tu contraseña
                        database="reinvent_reinventar"  # Cambia esto por tu base de datos
                    )
                    cursor = connection.cursor()
                    sql_insert_query = "INSERT INTO necesidad (necesidad, nombre, telefono) VALUES (%s, %s, %s)"
                    cursor.execute(sql_insert_query, (faltante, nombre, numero))
                    connection.commit()
                    cursor.close()
                    connection.close()
                except Error as error:
                    dispatcher.utter_message(text=f"Error al guardar en la base de datos: {error}")
                dispatcher.utter_message(text="Gracias. He guardado tu información, pronto nos comunicaremos contigo")
            else:
                dispatcher.utter_message(text="Lo siento, no he podido obtener tu información correctamente.")

        return []
    
class ActionTallefalta(Action):

    def name(self) -> str:
        return "action_talle_falta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        nombre = tracker.get_slot("nombre")
        numero = tracker.get_slot("numero")
        faltante = tracker.get_slot("item")
        talle = tracker.get_slot("talle")
        
        if nombre and faltante:
            file_path = "necesidades.txt"
            with open(file_path, "a") as file:
                file.write(f"Nombre: {nombre}, Telefono: {numero}, Necesita: {faltante}, Talle: {talle}\n")
            try:
                connection = mysql.connector.connect(
                    host="localhost",  # Cambia esto por tu host
                    user="root",  # Cambia esto por tu usuario
                    password="",  # Cambia esto por tu contraseña
                    database="reinvent_reinventar"  # Cambia esto por tu base de datos
                )
                cursor = connection.cursor()
                sql_insert_query = "INSERT INTO necesidad (necesidad, nombre, telefono, talle) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_insert_query, (faltante, nombre, numero, talle))
                connection.commit()
                cursor.close()
                connection.close()
                SlotSet("ropa", "")
            except Error as error:
                dispatcher.utter_message(text=f"Error al guardar en la base de datos: {error}")
            dispatcher.utter_message(text="Gracias. He guardado tu información, pronto nos comunicaremos contigo")
        else:
            dispatcher.utter_message(text="Lo siento, no he podido obtener tu información correctamente.")
        return [SlotSet("ropa", "")]
    
    
class ActionGetLastUserMessage(Action):

    def name(self) -> Text:
        return "action_ultimo_mensaje"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_intent = tracker.latest_message["intent"]["name"]

        if last_intent == "negacion":    
            last_user_message = tracker.latest_message.get('text')
            dispatcher.utter_message(text="Por favor dame tu nombre y numero de telefono")
            return [SlotSet("item", last_user_message)]
        
        return[]

class ActionDonar(Action):

    def name(self) -> str:
        return "action_donar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        ropaTalle =  ["pantalon", "remera", "pantalón", "musculosa", "camiseta", "campera", "buzo", "jean", "short", "zapatillas", "medias", "sweater", "sueter", "zapatos", "sandalias", "ojotas", "malla", "cinto", "cinturon"]
        nombre = tracker.get_slot("nombre")
        numero = tracker.get_slot("numero")
        donacion = tracker.get_slot("item2")
        ropa = tracker.get_slot("ropa")
        print (ropa)
        if ropa in ropaTalle:
             dispatcher.utter_message(text="Me decis el talle por favor")
        else: 
            if nombre and donacion:
                file_path = "donaciones.txt"
                with open(file_path, "a") as file:
                    file.write(f"Nombre: {nombre}, Telefono: {numero}, Dona: {donacion}\n")
                try:
                    connection = mysql.connector.connect(
                        host="localhost",  # Cambia esto por tu host
                        user="root",  # Cambia esto por tu usuario
                        password="",  # Cambia esto por tu contraseña
                        database="reinvent_reinventar"  # Cambia esto por tu base de datos
                    )
                    cursor = connection.cursor()
                    sql_insert_query = "INSERT INTO donacion (donacion, nombre, telefono) VALUES (%s, %s, %s)"
                    cursor.execute(sql_insert_query, (donacion, nombre, numero))
                    connection.commit()
                    cursor.close()
                    connection.close()
                except Error as error:
                    dispatcher.utter_message(text=f"Error al guardar en la base de datos: {error}")
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
        
        last_intent = tracker.latest_message["intent"]["name"]

        if last_intent == "negacion":    
            last_user_message = tracker.latest_message.get('text')
            dispatcher.utter_message(text="Por favor dame tu nombre y numero de telefono")
            return [SlotSet("item", last_user_message)]
        
        return[]

class ActionTalleDonar(Action):

    def name(self) -> str:
        return "action_talle_dona"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        nombre = tracker.get_slot("nombre")
        numero = tracker.get_slot("numero")
        donacion = tracker.get_slot("item2")
        talle = tracker.get_slot("talle")
     
        if nombre and donacion:
            file_path = "donaciones.txt"
            with open(file_path, "a") as file:
                file.write(f"Nombre: {nombre}, Telefono: {numero}, Dona: {donacion}, Talle: {talle}\n")
            try:
                connection = mysql.connector.connect(
                    host="localhost",  # Cambia esto por tu host
                    user="root",  # Cambia esto por tu usuario
                    password="",  # Cambia esto por tu contraseña
                    database="reinvent_reinventar"  # Cambia esto por tu base de datos
                )
                cursor = connection.cursor()
                sql_insert_query = "INSERT INTO donacion (donacion, nombre, telefono, talle) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_insert_query, (donacion, nombre, numero, talle))
                connection.commit()
                cursor.close()
                connection.close()
                SlotSet("ropa", "")
            except Error as error:
                dispatcher.utter_message(text=f"Error al guardar en la base de datos: {error}")
            dispatcher.utter_message(text="Gracias. He guardado tu información, pronto nos comunicaremos contigo")
        else:
            dispatcher.utter_message(text="Lo siento, no he podido obtener tu información correctamente.")
        return [SlotSet("ropa", "")]
    
class ActionGetLastUserMessage(Action):

    def name(self) -> Text:
        return "action_ultimo_mensaje_donacion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_intent = tracker.latest_message["intent"]["name"]
        
        if last_intent == "donacion":
            last_user_message = tracker.latest_message.get('text')
            dispatcher.utter_message(text="Por favor dame tu nombre y numero de telefono")
            return [SlotSet("item2", last_user_message)]
        
        return[]

class ActionDocumentacion(Action):
     def name(self):
         return "action_documentacion"

     def run(self, dispatcher, tracker: Tracker, domain):
        actividad = tracker.get_slot("actividad")
         # URL local del PDF
        print(actividad)
        if actividad == "hockey":
            dispatcher.utter_message(text="veni a retirar tu planilla de inscripcion a Velez S 491, Tandil, Buenos Aires")
        else:
            dispatcher.utter_message(text="no hay que presentar nada")
        return []
