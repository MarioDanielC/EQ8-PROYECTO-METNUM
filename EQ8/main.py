import os
import pygame
import sys
import random
import caso1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

ANCHO = 1000
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Detective: Casos Numericos")

reloj = pygame.time.Clock()

fondo = pygame.image.load(os.path.join(BASE_DIR, "fondos", "fondo1.jpg"))
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

pygame.mixer.music.load(os.path.join(BASE_DIR, "sonidos", "intro.wav"))
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

# Botones menú selección de caso
btn_caso1 = pygame.Rect(250, 230, 500, 60)
btn_caso2 = pygame.Rect(250, 310, 500, 60)
btn_caso3 = pygame.Rect(250, 390, 500, 60)
btn_caso4 = pygame.Rect(250, 470, 500, 60)
btn_volver = pygame.Rect(350, 560, 300, 60)

# Botones de dificultad
btn_facil = pygame.Rect(350, 250, 300, 60)
btn_intermedio = pygame.Rect(350, 330, 300, 60)
btn_dificil = pygame.Rect(350, 410, 300, 60)

estado_menu = "principal"
caso_seleccionado = 0

lluvia = []

for i in range(150):
    x = random.randint(0, ANCHO)
    y = random.randint(0, ALTO)
    velocidad = random.randint(4, 10)

    lluvia.append([x, y, velocidad])

def dibujar_texto(texto, fuente, color, x, y):

    render = fuente.render(texto, True, color)
    if x == "centro":
        x = (ANCHO - render.get_width()) // 2

    sombra = fuente.render(texto, True, NEGRO)
    pantalla.blit(sombra, (x + 2, y + 2))

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

    mouse = pygame.mouse.get_pos()

    if estado_menu == "principal":
        dibujar_texto(
            "DETECTIVE:",
            titulo_fuente,
            BLANCO,
            "centro",
            90
        )

        dibujar_texto(
            "CASOS NUMERICOS",
            titulo_fuente,
            AZUL,
            "centro",
            160
        )

        dibujar_texto(
            '"Los numeros nunca mienten..."',
            frase_fuente,
            BLANCO,
            "centro",
            240
        )

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
            "centro",
            338
        )

        dibujar_texto(
            "TUTORIALES",
            menu_fuente,
            BLANCO,
            "centro",
            438
        )

        dibujar_texto(
            "SALIR",
            menu_fuente,
            BLANCO,
            "centro",
            538
        )

    elif estado_menu == "seleccion_caso":
        dibujar_texto(
            "SELECCIONAR EL CASO",
            titulo_fuente,
            BLANCO,
            "centro",
            90
        )

        color_caso1 = AZUL if btn_caso1.collidepoint(mouse) else GRIS
        color_caso2 = AZUL if btn_caso2.collidepoint(mouse) else GRIS
        color_caso3 = AZUL if btn_caso3.collidepoint(mouse) else GRIS
        color_caso4 = AZUL if btn_caso4.collidepoint(mouse) else GRIS
        color_volver = AZUL if btn_volver.collidepoint(mouse) else GRIS

        pygame.draw.rect(pantalla, color_caso1, btn_caso1, border_radius=12)
        pygame.draw.rect(pantalla, color_caso2, btn_caso2, border_radius=12)
        pygame.draw.rect(pantalla, color_caso3, btn_caso3, border_radius=12)
        pygame.draw.rect(pantalla, color_caso4, btn_caso4, border_radius=12)
        pygame.draw.rect(pantalla, color_volver, btn_volver, border_radius=12)

        dibujar_texto("Caso 01 - La Caja Fuerte", menu_fuente, BLANCO, "centro", 240)
        dibujar_texto("Caso 02", menu_fuente, BLANCO, "centro", 320)
        dibujar_texto("Caso 03", menu_fuente, BLANCO, "centro", 400)
        dibujar_texto("Caso 04", menu_fuente, BLANCO, "centro", 480)
        dibujar_texto("Volver", menu_fuente, BLANCO, "centro", 570)

    elif estado_menu == "seleccion_dificultad":
        dibujar_texto("SELECCIONA LA DIFICULTAD", titulo_fuente, BLANCO, "centro", 100)
        
        color_facil = AZUL if btn_facil.collidepoint(mouse) else GRIS
        color_intermedio = AZUL if btn_intermedio.collidepoint(mouse) else GRIS
        color_dificil = AZUL if btn_dificil.collidepoint(mouse) else GRIS
        color_volver = AZUL if btn_volver.collidepoint(mouse) else GRIS
        
        pygame.draw.rect(pantalla, color_facil, btn_facil, border_radius=12)
        pygame.draw.rect(pantalla, color_intermedio, btn_intermedio, border_radius=12)
        pygame.draw.rect(pantalla, color_dificil, btn_dificil, border_radius=12)
        pygame.draw.rect(pantalla, color_volver, btn_volver, border_radius=12)
        
        dibujar_texto("F\u00e1cil", menu_fuente, BLANCO, "centro", 260)
        dibujar_texto("Intermedio", menu_fuente, BLANCO, "centro", 340)
        dibujar_texto("Dif\u00edcil", menu_fuente, BLANCO, "centro", 420)
        dibujar_texto("Volver", menu_fuente, BLANCO, "centro", 570)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if estado_menu == "principal":
                if btn_iniciar.collidepoint(evento.pos):
                    estado_menu = "seleccion_caso"

                if btn_tutorial.collidepoint(evento.pos):
                    print("Abriendo tutoriales...")

                if btn_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

            elif estado_menu == "seleccion_caso":
                if btn_caso1.collidepoint(evento.pos):
                    caso_seleccionado = 1
                    estado_menu = "seleccion_dificultad"

                if btn_caso2.collidepoint(evento.pos):
                    print("Iniciando Caso 02...")
                if btn_caso3.collidepoint(evento.pos):
                    print("Iniciando Caso 03...")
                if btn_caso4.collidepoint(evento.pos):
                    print("Iniciando Caso 04...")
                if btn_volver.collidepoint(evento.pos):
                    estado_menu = "principal"
                    
            elif estado_menu == "seleccion_dificultad":
                dificultad_elegida = None
                if btn_facil.collidepoint(evento.pos):
                    dificultad_elegida = "facil"
                elif btn_intermedio.collidepoint(evento.pos):
                    dificultad_elegida = "intermedio"
                elif btn_dificil.collidepoint(evento.pos):
                    dificultad_elegida = "dificil"
                elif btn_volver.collidepoint(evento.pos):
                    estado_menu = "seleccion_caso"
                    
                if dificultad_elegida is not None:
                    if caso_seleccionado == 1:
                        resultado = caso1.ejecutar_caso1(pantalla, reloj, ANCHO, ALTO, dificultad_elegida)
                        if resultado == "menu":
                            estado_menu = "principal"
                    # Aquí se agregarían los demás casos (ej: elif caso_seleccionado == 2)

    pygame.display.flip()
    reloj.tick(60)