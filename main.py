import secrets
import string

menu_icon = """
██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░░███║╚██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""

def menu():
    print("\n--- MENÚ ---")
    print("1. Generar contraseña segura")
    print("2. Mostrar este menú nuevamente")
    print("3. Salir")

def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Mostrar el menú al inicio
print(menu_icon)
menu()

while True:
    user = input("\nUser > ").strip().lower()  # Limpia espacios y normaliza entrada

    match user:
        case "exit" | "3":
            print("Saliendo del programa... ¡Hasta luego! 😊")
            break
        
        case "menu" | "2":
            menu()

        case "generar contraseña" | "1":
            contraseña = generar_contraseña()
            print(f"Contraseña segura generada: {contraseña}")

        case _:
            print("Opción no reconocida. Escribe 'menu' para ver las opciones.")
