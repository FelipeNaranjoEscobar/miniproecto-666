import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import pygame
import interfazusuario
pygame.init()

#pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Entrenador Personal - BodyBuilder')

# Cargar la imagen de Ronnie
try:
    imagen_ronnie = pygame.image.load('ronnie.png')
except Exception as e:
    print(f"Error cargando la imagen: {e}")
    exit()

root = tk.Tk()

# PECHO IMAGENES
try:
    imagen_flexiones = tk.PhotoImage(file='Flexiones.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_pressbanca = tk.PhotoImage(file='Press banca.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_aperturas = tk.PhotoImage(file='APERTURAS.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_fondos = tk.PhotoImage(file='fondos.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_pecdeck = tk.PhotoImage(file='PECK DECK.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

# imagenes pierna "Sentadillas", "Zancadas", "Prensa", "Extensiones", "Curl de piernas"
try:
    imagen_Sentadillas = tk.PhotoImage(file='Sentadillas.png') 
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Zancadas = tk.PhotoImage(file='Zancadas.png') 
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Prensa = tk.PhotoImage(file='Prensa.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Extensiones = tk.PhotoImage(file='Extensiones.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Curlpierna = tk.PhotoImage(file='Curl de pierna.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

# imagenes espalda "Remo con mancuerna", "Dominadas", "Peso muerto", "Jalón al pecho", "Pull-over"

try:
    imagen_Remoconmancuerna = tk.PhotoImage(file='Remom.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Dominadas = tk.PhotoImage(file='Dominadas.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Pesomuerto = tk.PhotoImage(file='Pesomuerto.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Jalónalpecho = tk.PhotoImage(file='jalon.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_Pullover = tk.PhotoImage(file='pullover.png') 
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

# imagenes cardio "Títeres", "Plancha abdominal", "skipping", "Saltar la cuerda", "Burpees"

try:
    imagen_titeres = tk.PhotoImage(file='titeres.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_plancha = tk.PhotoImage(file='plancha.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_skipping = tk.PhotoImage(file='skipping.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_cuerda = tk.PhotoImage(file='cuerda.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

try:
    imagen_burpees = tk.PhotoImage(file='burpees.png')  
except tk.TclError as e:
    print(f"Error cargando la imagen: {e}")
    exit()

# Obtener dimensiones de la imagen
ancho_imagen, alto_imagen = imagen_ronnie.get_size()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Fuentes
pygame.font.init()
fuente = pygame.font.Font(None, 36)

# Contador de créditos
creditos = 0

# Ejercicios por grupo muscular (Aumentados)
ejercicios_pecho = ["Press de banca", "Flexiones", "Fondos", "Aperturas", "Pec Deck"]
ejercicios_pierna = ["Sentadillas", "Zancadas", "Prensa", "Extensiones", "Curl de piernas"]
ejercicios_espalda = ["Remo con mancuerna", "Dominadas", "Peso muerto", "Jalón al pecho", "Pull-over"]
ejercicios_cardio = ["Títeres", "Plancha abdominal", "skipping", "Saltar la cuerda", "Burpees"]
tienda = []

def mostrar_imagen(imagen, x, y):
    """Descripción: Muestra una imagen en la pantalla de Pygame en la posición especificada.
Parámetros:
imagen: La imagen a mostrar.
x: La coordenada x de la posición donde se mostrará la imagen.
y: La coordenada y de la posición donde se mostrará la imagen.
Retorno: No devuelve nada."""
    pantalla.blit(imagen, (x, y))

# Función para mostrar texto en la pantalla de Pygame
def mostrar_texto(texto, x, y, pantalla):
    """Descripción: Muestra un texto en la pantalla de Pygame en la posición especificada.
Parámetros:
texto: El texto a mostrar.
x: La coordenada x de la posición donde se mostrará el texto.
y: La coordenada y de la posición donde se mostrará el texto.
pantalla: La pantalla de Pygame donde se mostrará el texto.
Retorno: No devuelve nada"""
    superficie_texto = fuente.render(texto, True, NEGRO)
    pantalla.blit(superficie_texto, (x, y))
def cerrar_ventanas_abiertas(excepto=None):
    """Descripción: Oculta todas las ventanas top-level de Tkinter excepto la especificada.
    Parámetros:
    excepto: La ventana que no se ocultará (opcional)."""
    for window in root.winfo_children():
        if window != excepto and isinstance(window, tk.Toplevel):
            window.withdraw()  # Oculta la ventana en lugar de cerrarla


def iniciar_ejercicio(ejercicio, rutinas=None):
    """Descripción: Inicia un ejercicio y muestra la ventana correspondiente.
Parámetros:
ejercicio: El ejercicio a iniciar.
rutinas: La lista de rutinas a realizar (opcional).
Retorno: No devuelve nada."""
    global creditos  # Accede a la variable global de créditos

    # Crear una nueva ventana de Tkinter
    ventana_ejercicio = tk.Toplevel(root)  # Asegúrate de crearla como hijo de 'root'
    ventana_ejercicio.title(f"Ejercicio: {ejercicio}")
    ventana_ejercicio.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventanas_abiertas(ventana_ejercicio))
    # Variables globales para series y temporizador
    series_actual = 0
    total_series = 4
    tiempo_descanso = 10
    descanso_activo = True

    # Mostrar información de la serie actual
    label_series = tk.Label(ventana_ejercicio, text=f"Serie: {series_actual}/{total_series}", font=("Arial", 18))
    label_series.pack(pady=10)

    # Contador de descanso
    label_descanso = tk.Label(ventana_ejercicio, text="Presiona 'Siguiente Serie' para comenzar", font=("Arial", 14))
    label_descanso.pack(pady=10)

    # Mostrar imagen correspondiente al ejercicio
    if ejercicio == "Flexiones":
        label_imagen_flexiones = tk.Label(ventana_ejercicio, image=imagen_flexiones)
        label_imagen_flexiones.pack(pady=10)
    elif ejercicio == "Press de banca":
        label_imagen_pressbanca = tk.Label( ventana_ejercicio, image=imagen_pressbanca)
        label_imagen_pressbanca.pack(pady=10)
    elif ejercicio == "Fondos":
        label_imagen_fondos = tk.Label(ventana_ejercicio, image=imagen_fondos)
        label_imagen_fondos.pack(pady=10)
    elif ejercicio == "Aperturas":
        label_imagen_aperturas = tk.Label(ventana_ejercicio, image=imagen_aperturas)
        label_imagen_aperturas.pack(pady=10)
    elif ejercicio == "Pec Deck":
        label_imagen_pecdeck = tk.Label(ventana_ejercicio, image=imagen_pecdeck)
        label_imagen_pecdeck.pack(pady=10)
    elif ejercicio == "Sentadillas":
        label_imagen_Sentadillas = tk.Label(ventana_ejercicio, image=imagen_Sentadillas)
        label_imagen_Sentadillas.pack(pady=10)
    elif ejercicio == "Extensiones":
        label_imagen_Extensiones = tk.Label(ventana_ejercicio, image=imagen_Extensiones)
        label_imagen_Extensiones.pack(pady=10)
    elif ejercicio == "Prensa":
        label_imagen_Prensa = tk.Label(ventana_ejercicio, image=imagen_Prensa)
        label_imagen_Prensa.pack(pady=10)
    elif ejercicio == "Zancadas":
        label_imagen_Zancadas = tk.Label(ventana_ejercicio, image=imagen_Zancadas)
        label_imagen_Zancadas.pack(pady=10)
    elif ejercicio == "Curl de piernas":
        label_imagen_Curlpiernas = tk.Label(ventana_ejercicio, image=imagen_Curlpierna)
        label_imagen_Curlpiernas.pack(pady=10)
    elif ejercicio == "Remo con mancuerna":
        label_imagen_Remoconmancuerna = tk.Label(ventana_ejercicio, image=imagen_Remoconmancuerna)
        label_imagen_Remoconmancuerna.pack(pady=10)
    elif ejercicio == "Dominadas":
        label_imagen_Dominadas = tk.Label(ventana_ejercicio, image=imagen_Dominadas)
        label_imagen_Dominadas.pack(pady=10)
    elif ejercicio == "Peso muerto":
        label_imagen_Pesomuerto = tk.Label(ventana_ejercicio, image=imagen_Pesomuerto)
        label_imagen_Pesomuerto.pack(pady=10)
    elif ejercicio == "Jalón al pecho":
        label_imagen_Jalónalpecho = tk.Label(ventana_ejercicio, image=imagen_Jalónalpecho)
        label_imagen_Jalónalpecho.pack(pady=10)
    elif ejercicio == "Pull-over":
        label_imagen_Pullover = tk.Label(ventana_ejercicio, image=imagen_Pullover)
        label_imagen_Pullover.pack(pady=10)
    elif ejercicio == "Títeres":
        label_imagen_titeres = tk.Label(ventana_ejercicio, image=imagen_titeres)
        label_imagen_titeres.pack(pady=10)
    elif ejercicio == "Plancha abdominal":
        label_imagen_plancha = tk.Label(ventana_ejercicio, image=imagen_plancha)
        label_imagen_plancha.pack(pady=10)
    elif ejercicio == "skipping":
        label_imagen_skipping = tk.Label(ventana_ejercicio, image=imagen_skipping)
        label_imagen_skipping.pack(pady=10)
    elif ejercicio == "Saltar la cuerda":
        label_imagen_cuerda = tk.Label(ventana_ejercicio, image=label_imagen_cuerda)
        label_imagen_cuerda.pack(pady=10)
    elif ejercicio == "Burpees":
        label_imagen_burpees = tk.Label(ventana_ejercicio, image=imagen_burpees)
        label_imagen_burpees.pack(pady=10)

    # Función para manejar el descanso automático y la siguiente serie
    def temporizador_descanso():
        """Descripción: Inicia un temporizador de descanso para el ejercicio actual.
Parámetros: No tiene parámetros.
Retorno: No devuelve nada."""
        nonlocal series_actual
        for i in range(tiempo_descanso, 0, -1):
            label_descanso.config(text=f"Descanso: {i} segundos")
            ventana_ejercicio.update()
            time.sleep(1)
        siguiente_serie()  # Pasar automáticamente a la siguiente serie

    # Función para avanzar a la siguiente serie
    def siguiente_serie():
        """Descripción: Avanza a la siguiente serie del ejercicio actual.
Parámetros: No tiene parámetros.
Retorno: No devuelve nada."""
        nonlocal series_actual, descanso_activo
        descanso_activo = False
        series_actual += 1
        if series_actual <= total_series:
            label_series.config(text=f"Serie: {series_actual}/{total_series}")
            if series_actual < total_series:
                label_descanso.config(text="Presiona 'Siguiente Serie' o espera el descanso")
                boton_siguiente.config(state=tk.NORMAL)  # Habilitar botón nuevamente
                boton_saltar.config(state=tk.NORMAL)
        if series_actual == total_series:
            if rutinas and len(rutinas) > 0:
                siguiente_ejercicio = rutinas.pop(0)
                messagebox.showinfo("Ejercicio Completado", f"¡Has completado las 4 series de {ejercicio}!\nEl siguiente ejercicio es: {siguiente_ejercicio}.")
                iniciar_ejercicio(siguiente_ejercicio, rutinas)
            else:
                # Incrementar créditos al finalizar la rutina
                global creditos
                creditos += 5000  # Sumar 5000 créditos
                messagebox.showinfo("Rutina Completada", "¡Has completado todas las rutinas!")
                # No cerrar la ventana, permitir que el usuario continúe seleccionando ejercicios

    # Función para manejar la siguiente serie con descanso
    def manejar_siguiente_serie():
        """Descripción: Maneja la siguiente serie del ejercicio actual y muestra el temporizador de descanso.
Parámetros: No tiene parámetros.
Retorno: No devuelve nada."""
        nonlocal descanso_activo
        descanso_activo = True
        boton_siguiente.config(state=tk.DISABLED)  # Deshabilitar el botón mientras se cuenta el descanso
        boton_saltar.config(state=tk.DISABLED)
        threading.Thread(target=temporizador_descanso).start()  # Iniciar descanso en un nuevo hilo

    # Botón para avanzar a la siguiente serie
    boton_siguiente = tk.Button(ventana_ejercicio, text="Siguiente Serie", font=("Arial", 14), command=manejar_siguiente_serie)
    boton_siguiente.pack(pady=10)

    # Botón para saltar el descanso
    boton_saltar = tk.Button(ventana_ejercicio, text="Saltar Descanso", font=("Arial", 14), command=siguiente_serie)
    boton_saltar.pack(pady=10)

    # Botón para cambiar de ejercicio
    boton_cambiar = tk.Button(ventana_ejercicio, text="Cambiar Ejercicio", font=("Arial", 14), command=ventana_ejercicio.destroy)
    boton_cambiar.pack(pady=10)

    # Mantener la ventana abierta
    ventana_ejercicio.mainloop()

def abrir_ventana_tkinter(grupo, ejercicios):
    """Descripción: Abre una ventana de Tkinter para seleccionar ejercicios de un grupo muscular.
Parámetros:
grupo: El grupo muscular al que pertenecen los ejercicios.
ejercicios: La lista de ejercicios a mostrar.
Retorno: No devuelve nada."""
    # Crear una ventana de Tkinter
    ventana_tk = tk.Toplevel(root)
    ventana_tk.title(f"Ejercicios de {grupo}")

    # Función para generar rutina aleatoria
    def generar_rutina_aleatoria():
        """Descripción: Genera una rutina aleatoria de ejercicios para el grupo muscular seleccionado.
Parámetros: No tiene parámetros.
Retorno: No devuelve nada."""
        if len(ejercicios) >= 4:  # Verifica si hay al menos 4 ejercicios
            rutinas = random.sample(ejercicios, 4)
            iniciar_ejercicio(rutinas[0], rutinas)
        else:
            messagebox.showerror("Error", "No hay suficientes ejercicios para generar una rutina aleatoria.")

    # Botón para generar rutina aleatoria
    boton_rutina_random = tk.Button(ventana_tk, text="Generar Rutina Random", font=("Arial", 14), command=generar_rutina_aleatoria)
    boton_rutina_random.pack(pady=10)

    # Crear botones para cada ejercicio
    for ejercicio in ejercicios:
        boton = tk.Button(ventana_tk, text=ejercicio, font =("Arial", 14), command=lambda e=ejercicio: iniciar_ejercicio(e))
        boton.pack(pady=5)

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_tk, text="Cerrar", font=("Arial", 14), command=ventana_tk.destroy)
    boton_cerrar.pack(pady=20)

    ventana_tk.mainloop()
    
    

    
def manejar_clic(x, y):
    """Descripción: Maneja el clic del mouse en la pantalla de Pygame y abre la ventana correspondiente.
Parámetros:
x: La coordenada x del clic.
y: La coordenada y del clic.
Retorno: No devuelve nada."""


    if 120< y < 200:  # Pecho
        abrir_ventana_tkinter("Pecho", ejercicios_pecho)
    elif 200 < y < 300:  # Pierna
        abrir_ventana_tkinter("Pierna", ejercicios_pierna)
    elif 300 < y < 400:  # Espalda
        abrir_ventana_tkinter("Espalda", ejercicios_espalda)
    elif 400 < y < 500:  # Full Body (Combinación de todos)
        ejercicios_fullbody = ejercicios_cardio + ejercicios_pecho + ejercicios_pierna + ejercicios_espalda
        abrir_ventana_tkinter("Full Body", ejercicios_fullbody)
    elif 500 < y < 600:  # tienda
        abrir_ventana_tkinter("Tienda")
    elif 50 < y < 90 : 
        interfazusuario # Aquí se llama a la función correctamente

corriendo = True
while corriendo:
    pantalla.fill(BLANCO)

    # menu pygame
    mostrar_texto("ENTRENADOR BODYBUILDER, SELECCIONE PARTE A ENTRENAR:", 5, 15, pantalla)
    mostrar_texto("Usuarios", 50, 90, pantalla)
    mostrar_texto("Pecho", 110, 150, pantalla)
    mostrar_texto("Pierna", 100, 250, pantalla)
    mostrar_texto("Espalda", 100, 350, pantalla)
    mostrar_texto("Full Body", 100, 450, pantalla)
    mostrar_texto("Tienda (proximamente)", 100, 550, pantalla)

    # Mostrar los créditos en la esquina inferior derecha
    mostrar_texto(f"Créditos: {creditos}", ANCHO - 200, ALTO - 50, pantalla)
    #ubicar la imagen
    x_imagen = ANCHO - ancho_imagen - 50  
    y_imagen = (ALTO - alto_imagen) // 2  
    
    mostrar_imagen(imagen_ronnie, x_imagen, y_imagen)


    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Lógica para manejar clics y abrir ventanas
            manejar_clic(evento.pos[0], evento.pos[1])

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()