import subprocess
import os
import platform
import threading

packages = [
    "rasa",
    "mysql-connector-python",
    "streamlit",
    "google-generativeai",
    "python-dotenv",
    "pyinstaller"
]


def run_command_in_new_console(command, cwd=None, listener=None, console=None):
    if platform.system() == 'Windows':
        process = subprocess.Popen(command, cwd=cwd, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    elif platform.system() == 'Linux':
        command_with_nohup = f'nohup {command} &'
        process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
    
    def read_output():
        for line in iter(process.stdout.readline, ''):
            if listener:
                listener(line.rstrip(), console=console)
    
    output_thread = threading.Thread(target=read_output)
    output_thread.start()
    
    return process

def install(package):
    subprocess.check_call(["pip", "install", package])


def instalar_dependencias():
    try:
        for package in packages:
            install(package)
        return True
    except Exception as e:
        print(f'Error al instalar dependencias: {e}')
        return False

def main():
    commandForBotPublicActions = 'rasa run actions'
    commandForPublicBotModel = 'rasa run -m models --enable-api --cors "*"'
    commandForPrivateActions = 'rasa run actions --port 5056'
    commandForPrivateBotModel = 'rasa run -m models --port 5006 --enable-api --cors "*"'
    commandForMp = 'node index.js'
    
    Directory = os.getcwd()
    DirectoryBotPublic = os.path.join(Directory, 'bot_rasa')
    DirectoryBotPrivate = os.path.join(Directory, 'bot_noticias')
    DirectoryMp = os.path.join(Directory, 'mp')
    
    dependencias = instalar_dependencias()
    if dependencias:
        listadeprocesos = []
        
        def listener(line, console=None):
            line = line.strip()  # Eliminar espacios en blanco adicionales al inicio y final de la línea
            if "Rasa server is up and running" in line:
                print("Modelo de Rasa corriendo " + console )
            elif "Action endpoint is up and running" in line:
                print("Acción de Rasa corriendo " + console )
            elif "Server running " in line:
                print("Mercado Pago corriendo" + console)
        listadeprocesos.append(run_command_in_new_console(commandForMp, cwd=DirectoryMp, listener=listener, console="Mercado Pago"))
        listadeprocesos.append(run_command_in_new_console(commandForBotPublicActions, cwd=DirectoryBotPublic, listener=listener, console="Bot actions Actividades"))
        listadeprocesos.append(run_command_in_new_console(commandForPublicBotModel, cwd=DirectoryBotPublic, listener=listener, console="Bot modelo Actividades"))
        listadeprocesos.append(run_command_in_new_console(commandForPrivateActions, cwd=DirectoryBotPrivate, listener=listener, console="Bot actions Noticias"))
        listadeprocesos.append(run_command_in_new_console(commandForPrivateBotModel, cwd=DirectoryBotPrivate, listener=listener, console="Bot modelo Noticias"))
    
    print()
    input("Presiona Enter para cerrar los procesos...\n")
    print()
    for proceso in listadeprocesos:
        proceso.kill()

if __name__ == "__main__":
    main()
