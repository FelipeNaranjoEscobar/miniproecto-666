import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import pygame

pygame.init()

#pantalla
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
ejercicios_cardio = ["Títeres", "Plancha abdominal", "skipping", "Saltar la cuerda", "Burpees"]
tienda = []



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
    if 100 < y < 200:  # Pecho
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

corriendo = True
while corriendo:
    pantalla.fill(BLANCO)

    # menu pygame
    mostrar_texto("ENTRENADOR BODYBUILDER, SELECCIONE PARTE A ENTRENAR:", 5, 15, pantalla)
    mostrar_texto("Pecho", 100, 150, pantalla)
    mostrar_texto("Pierna", 100, 250, pantalla)
    mostrar_texto("Espalda", 100, 350, pantalla)
    mostrar_texto("Full Body", 100, 450, pantalla)
    mostrar_texto("Tienda (proximamente)", 100, 550, pantalla)

    # Mostrar los créditos en la esquina inferior derecha
    mostrar_texto(f"Créditos: {creditos}", ANCHO - 200, ALTO - 50, pantalla)
    #ubicar la imagen
    

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