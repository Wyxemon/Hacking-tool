# Main code

menu_icon="""

██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝"
"""

# print( las funciones del programa )

import secrets
import string

print(menu_icon)
print("Hello! How can I help you? 😊")

while True:
    user = input("User > ")  # Input para usuarios
    print(user)
    
    if user == "exit":
        exit()  # Salir del programa
    elif user == "help":
        print("""Available commands: help, exit, greet""")  # Help
    else:
        print(f"Unknown command: {user}. Type 'help' for available commands.")

    
# FUNCIONES:
# Aqui crear las funciones necesarias

# def main:

def contraseñas_seguras():
    def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Generar una contraseña segura de 16 caracteres
    contraseña_segura = generar_contraseña()
    print("Contraseña segura generada:", contraseña_segura)
    contraseñas_seguras()
