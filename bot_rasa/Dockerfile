# Usa una imagen base de Python
FROM python:3.7-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación Rasa al contenedor
COPY . .

# Instala las dependencias de tu aplicación Rasa
RUN pip install --no-cache-dir rasa

# Exponer el puerto en el que se ejecutará tu servidor de acciones
EXPOSE 5055

# Comando por defecto para ejecutar tu aplicación Rasa Actions
CMD ["rasa", "run", "actions"]
