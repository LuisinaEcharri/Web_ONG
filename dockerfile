# Usa una imagen base de Nginx ligera
FROM nginx:alpine

# Copia tu código de la página web al directorio de trabajo de Nginx
COPY . /usr/share/nginx/html
