import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

ANCHO = 1000
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Detective: Casos Numericos")

reloj = pygame.time.Clock()

fondo = pygame.image.load("fondos/fondo1.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

pygame.mixer.music.load("sonidos/intro.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

BLANCO = (255, 255, 255)
AZUL = (50, 120, 255)
GRIS = (60, 60, 60)
NEGRO = (0, 0, 0)

titulo_fuente = pygame.font.SysFont("Arial", 58, bold=True)
menu_fuente = pygame.font.SysFont("Arial", 34)
frase_fuente = pygame.font.SysFont("Arial", 24, italic=True)

btn_iniciar = pygame.Rect(350, 320, 300, 70)
btn_tutorial = pygame.Rect(350, 420, 300, 70)
btn_salir = pygame.Rect(350, 520, 300, 70)

lluvia = []

for i in range(150):
    x = random.randint(0, ANCHO)
    y = random.randint(0, ALTO)
    velocidad = random.randint(4, 10)

    lluvia.append([x, y, velocidad])

def dibujar_texto(texto, fuente, color, x, y):

    sombra = fuente.render(texto, True, NEGRO)
    pantalla.blit(sombra, (x + 2, y + 2))

    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))

while True:

    pantalla.blit(fondo, (0, 0))

    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(90)
    overlay.fill((0, 0, 0))

    pantalla.blit(overlay, (0, 0))

    for gota in lluvia:

        pygame.draw.line(
            pantalla,
            (180, 180, 255),
            (gota[0], gota[1]),
            (gota[0], gota[1] + 12),
            2
        )

        gota[1] += gota[2]

        if gota[1] > ALTO:
            gota[0] = random.randint(0, ANCHO)
            gota[1] = random.randint(-50, -10)

    dibujar_texto(
        "DETECTIVE:",
        titulo_fuente,
        BLANCO,
        300,
        90
    )

    dibujar_texto(
        "CASOS NUMERICOS",
        titulo_fuente,
        AZUL,
        180,
        160
    )

    dibujar_texto(
        '"Los numeros nunca mienten..."',
        frase_fuente,
        BLANCO,
        340,
        240
    )

    mouse = pygame.mouse.get_pos()

    color_iniciar = AZUL if btn_iniciar.collidepoint(mouse) else GRIS
    color_tutorial = AZUL if btn_tutorial.collidepoint(mouse) else GRIS
    color_salir = AZUL if btn_salir.collidepoint(mouse) else GRIS

    pygame.draw.rect(pantalla, color_iniciar, btn_iniciar, border_radius=12)
    pygame.draw.rect(pantalla, color_tutorial, btn_tutorial, border_radius=12)
    pygame.draw.rect(pantalla, color_salir, btn_salir, border_radius=12)

    dibujar_texto(
        "INICIAR JUEGO",
        menu_fuente,
        BLANCO,
        395,
        338
    )

    dibujar_texto(
        "TUTORIALES",
        menu_fuente,
        BLANCO,
        420,
        438
    )

    dibujar_texto(
        "SALIR",
        menu_fuente,
        BLANCO,
        460,
        538
    )

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if btn_iniciar.collidepoint(evento.pos):
                print("Iniciando juego...")

            if btn_tutorial.collidepoint(evento.pos):
                print("Abriendo tutoriales...")

            if btn_salir.collidepoint(evento.pos):
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    reloj.tick(60)