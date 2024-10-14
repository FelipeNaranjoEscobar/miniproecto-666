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
def cerrar_ventanas_abiertas(excepto=None):
    """Descripción: Oculta todas las ventanas top-level de Tkinter excepto la especificada.
    Parámetros:
    excepto: La ventana que no se ocultará (opcional)."""
    for window in root.winfo_children():
        if window != excepto and isinstance(window, tk.Toplevel):
            window.withdraw()  # Oculta la ventana en lugar de cerrarla
corriendo = True
while corriendo:
    pantalla.fill(BLANCO)
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