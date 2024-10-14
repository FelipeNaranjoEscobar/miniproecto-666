import pygame
import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla de Pygame
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Entrenador Personal - BodyBuilder')


root = tk.Tk()

    



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
ejercicios_cardio = ["Títeres", "Plancha abdominal", "Correr", "Saltar la cuerda", "Burpees"]
tienda =[]

# Función para mostrar texto en la pantalla de Pygame
def mostrar_texto(texto, x, y, pantalla):
    superficie_texto = fuente.render(texto, True, NEGRO)
    pantalla.blit(superficie_texto, (x, y))

# Función para iniciar la ventana del ejercicio y manejar series y descanso
def iniciar_ejercicio(ejercicio, rutinas=None):
    global creditos  # Accede a la variable global de créditos

    # Crear una nueva ventana de Tkinter
    ventana_ejercicio = tk.Toplevel()
    ventana_ejercicio.title(f"Ejercicio: {ejercicio}")
    
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
    if ejercicio == "Flexiones":
        label_imagen_flexiones = tk.Label(ventana_ejercicio, image=imagen_flexiones)
        label_imagen_flexiones.pack(pady=10)
    # Función para manejar el descanso automático y la siguiente serie
    def temporizador_descanso():
        nonlocal series_actual
        for i in range(tiempo_descanso, 0, -1):
            label_descanso.config(text=f"Descanso: {i} segundos")
            ventana_ejercicio.update()
            time.sleep(1)
        siguiente_serie()  # Pasar automáticamente a la siguiente serie

    # Función para avanzar a la siguiente serie
    def siguiente_serie():
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
                ventana_ejercicio.destroy()
                iniciar_ejercicio(siguiente_ejercicio, rutinas)
            else:
                # Incrementar créditos al finalizar la rutina
                global creditos
                creditos += 5000  # Sumar 5000 créditos
                messagebox.showinfo("Rutina Completada", "¡Has completado todas las rutinas!")
                ventana_ejercicio.destroy()

    # Función para manejar la siguiente serie con descanso
    def manejar_siguiente_serie():
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

    ventana_ejercicio.mainloop()

# Función para abrir ventana de selección de ejercicios y generar botones
def abrir_ventana_tkinter(grupo, ejercicios):
    # Crear una ventana de Tkinter
    ventana_tk = tk.Toplevel()
    ventana_tk.title(f"Ejercicios de {grupo}")

    # Función para generar rutina aleatoria
    def generar_rutina_aleatoria():
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
        boton = tk.Button(ventana_tk, text=ejercicio, font=("Arial", 14), command=lambda e=ejercicio: iniciar_ejercicio(e))
        boton.pack(pady=5)

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_tk, text="Cerrar", font=("Arial", 14), command=ventana_tk.destroy)
    boton_cerrar.pack(pady=20)

    ventana_tk.mainloop()

# Función para manejar eventos de clic y abrir la ventana de Tkinter con el grupo muscular seleccionado
def manejar_clic(x, y):
    if 100 < y < 200:  # Pecho
        abrir_ventana_tkinter("Pecho", ejercicios_pecho)
    elif 200 < y < 300:  # Pierna
        abrir_ventana_tkinter("Pierna", ejercicios_pierna)
    elif 300 < y < 400:  # Espalda
        abrir_ventana_tkinter("Espalda", ejercicios_espalda)
    elif 400 < y < 500:  # Full Body (Combinación de todos)
        ejercicios_fullbody = ejercicios_pecho + ejercicios_pierna + ejercicios_espalda + ejercicios_cardio
        abrir_ventana_tkinter("Full Body", ejercicios_fullbody)
    elif 500 < y < 600:  # tienda     
        abrir_ventana_tkinter("Tienda")

# Bucle principal de Pygame
corriendo = True
while corriendo:
    pantalla.fill(BLANCO)
    
    # Mostrar el menú en Pygame
    mostrar_texto("ENTRENADOR BODYBUILDER, SELECCIONE PARTE A ENTRENAR:", 5, 15, pantalla)
    mostrar_texto("Pecho", 100, 150, pantalla)
    mostrar_texto("Pierna", 100, 250, pantalla)
    mostrar_texto("Espalda", 100, 350, pantalla)
    mostrar_texto("Full Body", 100, 450, pantalla)
    mostrar_texto("Tienda (proximamente)", 100, 550, pantalla)

    # Mostrar los créditos en la esquina inferior derecha
    mostrar_texto(f"Créditos: {creditos}", ANCHO - 200, ALTO - 50, pantalla)

  

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            manejar_clic(x, y)

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()