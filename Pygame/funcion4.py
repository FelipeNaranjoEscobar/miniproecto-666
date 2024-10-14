import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import pygame
creditos=0
pygame.init()

#pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Entrenador Personal - BodyBuilder')

# Cargar la imagen de Ronnie


root = tk.Tk()



# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ejercicios_pecho = ["Press de banca", "Flexiones", "Fondos", "Aperturas", "Pec Deck"]
ejercicios_pierna = ["Sentadillas", "Zancadas", "Prensa", "Extensiones", "Curl de piernas"]
ejercicios_espalda = ["Remo con mancuerna", "Dominadas", "Peso muerto", "Jalón al pecho", "Pull-over"]
ejercicios_cardio = ["Títeres", "Plancha abdominal", "skipping", "Saltar la cuerda", "Burpees"]
tienda = []
# Fuentes
pygame.font.init()
fuente = pygame.font.Font(None, 36)
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
def abrir_ventana_tkinter(grupo, ejercicios):
    """Descripción: Abre una ventana de Tkinter para seleccionar ejercicios de un grupo muscular.
Parámetros:
grupo: El grupo muscular al que pertenecen los ejercicios.
ejercicios: La lista de ejercicios a mostrar.
Retorno: No devuelve nada."""
    # Crear una ventana de Tkinter
    ventana_tk = tk.Toplevel(root)
    ventana_tk.title(f"Ejercicios de {grupo}")

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