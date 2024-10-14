import tkinter as tk
from tkinter import messagebox
from userservice import obtener_usuarios, obtener_usuario, crear_usuario, actualizar_usuario

def abrir_gestion_usuarios():
    """Abre la ventana de gestión de usuarios."""
    global usuarios_text  # Definir como global para acceder desde otras funciones

    ventana = tk.Toplevel()  # Abre una nueva ventana en Tkinter
    ventana.title("Gestión de Usuarios")
    ventana.geometry("500x400")

    # Crear los widgets
    label_usuarios = tk.Label(ventana, text="Usuarios:")
    label_usuarios.pack()

    usuarios_text = tk.Text(ventana, height=10)
    usuarios_text.pack()

    # Botón para mostrar todos los usuarios
    btn_mostrar_usuarios = tk.Button(ventana, text="Mostrar todos los usuarios", command=mostrar_usuarios)
    btn_mostrar_usuarios.pack()

    label_user_id = tk.Label(ventana, text="ID del Usuario (ej. 'user1'):")
    label_user_id.pack()

    entrada_user_id = tk.Entry(ventana)
    entrada_user_id.pack()

    # Botón para ver un usuario específico
    btn_ver_usuario = tk.Button(ventana, text="Ver Usuario", command=ver_usuario)
    btn_ver_usuario.pack()

    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack()

    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    label_carrera = tk.Label(ventana, text="Carrera:")
    label_carrera.pack()

    entrada_carrera = tk.Entry(ventana)
    entrada_carrera.pack()

    label_password = tk.Label(ventana, text="Contraseña:")
    label_password.pack()

    entrada_password = tk.Entry(ventana, show="*")
    entrada_password.pack()
    
    #
    label_puntos = tk.Label(ventana, text="puntos:")
    label_puntos.pack()

    entrada_puntos = tk.Entry(ventana, show="*")
    entrada_puntos.pack()


    # Botón para crear un nuevo usuario
    btn_crear_usuario = tk.Button(ventana, text="Crear Usuario", command=crear_nuevo_usuario)
    btn_crear_usuario.pack()

    # Botón para actualizar un usuario
    btn_actualizar_usuario = tk.Button(ventana, text="Actualizar Usuario", command=actualizar_usuario_gui)
    btn_actualizar_usuario.pack()

    # Botón para salir de la ventana
    btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack()

    # Mostrar todos los usuarios al iniciar
    mostrar_usuarios()
def actualizar_usuario_gui():
    user_id = entrada_user_id.get()
    nombre = entrada_nombre.get()
    carrera = entrada_carrera.get()
    password = entrada_password.get()
    puntos = entrada_puntos.get()
    
    if not user_id:
        messagebox.showerror("Error", "Ingrese el ID del usuario")
        return
    
    resultado = actualizar_usuario(user_id, nombre=nombre if nombre else None, carrera=carrera if carrera else None, password=password if password else None,puntos=puntos if puntos else None)
    messagebox.showinfo("Resultado", resultado)
    # Mantener la ventana abierta
    ventana.mainloop()
def crear_nuevo_usuario():
    nombre = entrada_nombre.get()
    carrera = entrada_carrera.get()
    password = entrada_password.get()
    puntos = entrada_puntos.get()
    
    if not nombre or not carrera or not password or not puntos:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    resultado = crear_usuario(nombre, carrera, password,puntos)
    messagebox.showinfo("Éxito", resultado)
    mostrar_usuarios()
# Función para mostrar todos los usuarios en el cuadro de texto
def mostrar_usuarios():
    global usuarios_text  # Necesitas acceder a la variable global
    usuarios_text.delete("1.0", tk.END)
    usuarios = obtener_usuarios()
    for user_id, datos in usuarios.items():
        usuarios_text.insert(tk.END, f"{user_id}: {datos}\n")

# Función para ver un usuario específico
def ver_usuario():
    user_id = entrada_user_id.get()
    if not user_id:
        messagebox.showerror("Error", "Ingrese el ID del usuario")
        return
    
    usuario = obtener_usuario(user_id)
    if isinstance(usuario, str):  # Si es un mensaje de error
        messagebox.showerror("Error", usuario)
    else:
        messagebox.showinfo(f"Usuario {user_id}", f"Nombre: {usuario['nombre']}\nCarrera: {usuario['degree']}\nContraseña: {usuario['password']}\npuntos:: {usuario['puntos']}")
