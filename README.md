# Reinventar
Instalar:
- [Python](https://www.python.org/)
- [Node](https://nodejs.org/en)
- [Rasa](https://www.youtube.com/watch?v=RVoFqxmG8p0) ➜ `pip install rasa`
- [Anaconda](https://www.anaconda.com/) (opcional)
- Conector MYSQL para Python ➜ `python -m pip install mysql-connector-python`
## Bot actividades
- posicionarse en la carpeta bot_rasa
- rasa run actions
- rasa run -m models --enable-api --cors "*"
## Bot noticias
- posicionarse en la carpeta bot_noticias
- `pip install python-dotenv` para poder obtener del archivo .env la key que permitirá conectar el bot con la API de Gemini.
- rasa run actions --port 5056
- rasa run -m models --port  5006 --enable-api --cors "*"
## Mercado Pago
- posicionarse en la carpeta mp
- node index.js
## Xampp
correr el proyecto en Xampp:
- http://localhost/Web_ONG/
- http://localhost/Web_ONG/login.html
### Importar/Sobrescribir BDD local
- http://localhost/Web_ONG/initial.php
