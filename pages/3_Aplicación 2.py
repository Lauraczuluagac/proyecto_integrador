import streamlit as st

import pygame
import random

# Inicializa Pygame
pygame.init()

# Configura la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Caza de Patos")

# Define los colores
white = (255, 255, 255)

class Duck:
    def __init__(self):
        self.image = pygame.image.load("pato.webp")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, width - 50)
        self.rect.y = random.randint(50, height - 50)
        self.speed = 1

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Carga la imagen del pato
duck = Duck()

# Inicializa el reloj
clock = pygame.time.Clock()

# Variables de juego
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        duck.rect.x -= duck.speed
    if keys[pygame.K_RIGHT]:
        duck.rect.x += duck.speed
    if keys[pygame.K_UP]:
        duck.rect.y -= duck.speed
    if keys[pygame.K_DOWN]:
        duck.rect.y += duck.speed

    # Mueve el pato hacia abajo
    duck.move()

    # Dibuja la pantalla y el pato
    screen.fill(white)
    duck.draw()

    # Actualiza la pantalla
    pygame.display.update()

    # Limita la velocidad del juego
    clock.tick(60)

# Cierra Pygame
pygame.quit()

st.header("Aplicacón 2")