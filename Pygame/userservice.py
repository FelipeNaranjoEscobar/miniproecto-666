from users import users

def obtener_usuarios():
    return users


def obtener_usuario(user_id):
    return users.get(user_id, f"Usuario con ID {user_id} no encontrado.")


def crear_usuario(nombre, carrera, password,puntos):

    nuevo_id_num = len(users) + 1
    nuevo_id = f"user{nuevo_id_num}"
    
    users[nuevo_id] = {"degree": carrera, "password": password, "nombre": nombre, "puntos":puntos}
    return f"Usuario con ID {nuevo_id} creado."

def actualizar_usuario(user_id, nombre=None, carrera=None, password=None, puntos=None):
    if user_id in users:
        if nombre:
            users[user_id]["name"] = nombre
        if carrera:
            users[user_id]["degree"] = carrera
        if password:
            users[user_id]["password"] = password
        if puntos:
            users[user_id]["puntos"] = puntos
        return f"Usuario con ID {user_id} actualizado."
    else:
        return f"Usuario con ID {user_id} no encontrado."

