from userservice import obtener_usuarios, obtener_usuario, crear_usuario, actualizar_usuario

def mostrar_menu():
    print("\n--- Menú de Usuarios ---")
    print("1. Ver todos los usuarios")
    print("2. Ver usuario")
    print("3. Crear un nuevo usuario")
    print("4. Actualizar un usuario")
    print("5. Salir")

def solicitar_datos_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    carrera = input("Ingrese la carrera: ")
    password = input("Ingrese la contraseña: ")
    puntos= input("puntos")
    return nombre, carrera, password,puntos

def menu():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            print("\n--- Lista de Usuarios ---")
            usuarios = obtener_usuarios()
            for user_id, datos in usuarios.items():
                print(f"{user_id}: {datos}")
            print("\n")

        elif opcion == "2":
            user_id = input("Ingrese el ID del usuario que desea ver (ejemplo: 'user1'): ")
            usuario = obtener_usuario(user_id)
            print(f"\n--- Información del usuario {user_id} ---")
            print(usuario)
            print("\n")

        elif opcion == "3":
            print("\n--- Crear un nuevo usuario ---")
            nombre, carrera, password, puntos= solicitar_datos_usuario()
            resultado = crear_usuario(nombre, carrera, password,puntos)
            print(resultado)

        elif opcion == "4":
            user_id = input("Ingrese el ID del usuario que desea actualizar (ejemplo: 'user1'): ")
            print("\n--- Actualizar información del usuario ---")
            carrera = input("Ingrese la nueva carrera (deje en blanco para no cambiar): ")
            password = input("Ingrese la nueva contraseña (deje en blanco para no cambiar): ")
            puntos =input("Ingrese puntaje): ")
            resultado = actualizar_usuario(user_id, carrera=carrera if carrera else None, password=password if password else None,puntos=puntos if puntos else None)
            print(resultado)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()