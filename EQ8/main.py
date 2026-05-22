# -*- coding: utf-8 -*-
import os
import pygame
import sys
import random
from casos import Caso1
from casos import Caso2
from casos import Caso3
        
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

ANCHO = 1000
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Detective: Casos Numéricos")

reloj = pygame.time.Clock()

fondo = pygame.image.load(os.path.join(BASE_DIR, "assets", "menu", "fondo1.jpg"))
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

pygame.mixer.music.load(os.path.join(BASE_DIR, "sonidos", "intro.wav"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

BLANCO = (255, 255, 255)
AZUL = (50, 120, 255)
GRIS = (60, 60, 60)
NEGRO = (0, 0, 0)
AMARILLO = (255, 200, 50)
VERDE = (50, 200, 50)

titulo_fuente = pygame.font.SysFont("Arial", 58, bold=True)
menu_fuente = pygame.font.SysFont("Arial", 34)
frase_fuente = pygame.font.SysFont("Arial", 24, italic=True)

btn_iniciar = pygame.Rect(350, 320, 300, 70)
btn_marcador = pygame.Rect(350, 420, 300, 70)
btn_salir = pygame.Rect(350, 520, 300, 70)

# Botones menú selección de caso
btn_caso1 = pygame.Rect(250, 230, 500, 60)
btn_caso2 = pygame.Rect(250, 310, 500, 60)
btn_caso3 = pygame.Rect(250, 390, 500, 60)
btn_volver = pygame.Rect(350, 560, 300, 60)

# Botones de dificultad
btn_facil = pygame.Rect(350, 250, 300, 60)
btn_intermedio = pygame.Rect(350, 330, 300, 60)
btn_dificil = pygame.Rect(350, 410, 300, 60)

estado_menu = "principal"
caso_seleccionado = 0
estado_progreso = {"casos_desbloqueados": 1, "puntaje": 0, "puntajes_casos": {1: 0, 2: 0, 3: 0}}

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
            "CASOS NUMÉRICOS",
            titulo_fuente,
            AZUL,
            "centro",
            160
        )

        dibujar_texto(
            '"Los números nunca mienten..."',
            frase_fuente,
            BLANCO,
            "centro",
            240
        )

        color_iniciar = AZUL if btn_iniciar.collidepoint(mouse) else GRIS
        color_marcador = AZUL if btn_marcador.collidepoint(mouse) else GRIS
        color_salir = AZUL if btn_salir.collidepoint(mouse) else GRIS

        pygame.draw.rect(pantalla, color_iniciar, btn_iniciar, border_radius=12)
        pygame.draw.rect(pantalla, color_marcador, btn_marcador, border_radius=12)
        pygame.draw.rect(pantalla, color_salir, btn_salir, border_radius=12)

        dibujar_texto(
            "INICIAR JUEGO",
            menu_fuente,
            BLANCO,
            "centro",
            338
        )

        dibujar_texto(
            "MARCADOR",
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
        color_caso2 = (AZUL if btn_caso2.collidepoint(mouse) else GRIS) if estado_progreso["casos_desbloqueados"] >= 2 else (100, 30, 30)
        color_caso3 = (AZUL if btn_caso3.collidepoint(mouse) else GRIS) if estado_progreso["casos_desbloqueados"] >= 3 else (100, 30, 30)
        color_volver = AZUL if btn_volver.collidepoint(mouse) else GRIS

        pygame.draw.rect(pantalla, color_caso1, btn_caso1, border_radius=12)
        pygame.draw.rect(pantalla, color_caso2, btn_caso2, border_radius=12)
        pygame.draw.rect(pantalla, color_caso3, btn_caso3, border_radius=12)
        pygame.draw.rect(pantalla, color_volver, btn_volver, border_radius=12)

        dibujar_texto("Caso 01 - La Caja Fuerte", menu_fuente, BLANCO, "centro", 240)
        
        txt_c2 = "Caso 02 - Descubriendo la Verdad" if estado_progreso["casos_desbloqueados"] >= 2 else "Caso 02 (Bloqueado)"
        color_txt2 = BLANCO if estado_progreso["casos_desbloqueados"] >= 2 else (150, 150, 150)
        dibujar_texto(txt_c2, menu_fuente, color_txt2, "centro", 320)
        
        txt_c3 = "Caso 03 - La Confrontación" if estado_progreso["casos_desbloqueados"] >= 3 else "Caso 03 (Bloqueado)"
        color_txt3 = BLANCO if estado_progreso["casos_desbloqueados"] >= 3 else (150, 150, 150)
        dibujar_texto(txt_c3, menu_fuente, color_txt3, "centro", 400)
        
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
        
        dibujar_texto("Fácil", menu_fuente, BLANCO, "centro", 260)
        dibujar_texto("Intermedio", menu_fuente, BLANCO, "centro", 340)
        dibujar_texto("Difícil", menu_fuente, BLANCO, "centro", 420)
        dibujar_texto("Volver", menu_fuente, BLANCO, "centro", 570)

    elif estado_menu == "marcador":
        dibujar_texto("MARCADOR", titulo_fuente, AMARILLO, "centro", 90)
        
        puntaje_total = sum(estado_progreso["puntajes_casos"].values())
        dibujar_texto(f"Puntaje Total: {puntaje_total} pts", titulo_fuente, VERDE, "centro", 160)
        
        dibujar_texto(f"Caso 01 - La Caja Fuerte: {estado_progreso['puntajes_casos'][1]} pts", menu_fuente, BLANCO, "centro", 260)
        
        txt_c2 = f"Caso 02 - Descubriendo la Verdad: {estado_progreso['puntajes_casos'][2]} pts" if estado_progreso["casos_desbloqueados"] >= 2 else "Caso 02: ---"
        dibujar_texto(txt_c2, menu_fuente, BLANCO if estado_progreso["casos_desbloqueados"] >= 2 else GRIS, "centro", 340)
        
        txt_c3 = f"Caso 03 - La Confrontación: {estado_progreso['puntajes_casos'][3]} pts" if estado_progreso["casos_desbloqueados"] >= 3 else "Caso 03: ---"
        dibujar_texto(txt_c3, menu_fuente, BLANCO if estado_progreso["casos_desbloqueados"] >= 3 else GRIS, "centro", 420)
        
        color_volver = AZUL if btn_volver.collidepoint(mouse) else GRIS
        pygame.draw.rect(pantalla, color_volver, btn_volver, border_radius=12)
        dibujar_texto("Volver", menu_fuente, BLANCO, "centro", 570)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if estado_menu == "principal":
                if btn_iniciar.collidepoint(evento.pos):
                    estado_menu = "seleccion_caso"

                if btn_marcador.collidepoint(evento.pos):
                    estado_menu = "marcador"

                if btn_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

            elif estado_menu == "seleccion_caso":
                if btn_caso1.collidepoint(evento.pos):
                    caso_seleccionado = 1
                    estado_menu = "seleccion_dificultad"

                if btn_caso2.collidepoint(evento.pos) and estado_progreso["casos_desbloqueados"] >= 2:
                    caso_seleccionado = 2
                    estado_menu = "seleccion_dificultad"
                    
                if btn_caso3.collidepoint(evento.pos) and estado_progreso["casos_desbloqueados"] >= 3:
                    caso_seleccionado = 3
                    estado_menu = "seleccion_dificultad"
                if btn_volver.collidepoint(evento.pos):
                    estado_menu = "principal"
                    
            elif estado_menu == "marcador":
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
                        resultado = Caso1.ejecutar_caso1(pantalla, reloj, ANCHO, ALTO, dificultad_elegida, estado_progreso)
                        if resultado == "caso_completado":
                            estado_progreso["casos_desbloqueados"] = max(estado_progreso["casos_desbloqueados"], 2)
                            mejor_puntaje = max(estado_progreso["puntajes_casos"][1], estado_progreso.get("ultimo_puntaje", 0))
                            estado_progreso["puntajes_casos"][1] = mejor_puntaje
                        estado_menu = "principal"
                    elif caso_seleccionado == 2:
                        resultado = Caso2.ejecutar_caso2(pantalla, reloj, ANCHO, ALTO, dificultad_elegida, estado_progreso)
                        if resultado == "caso_completado":
                            estado_progreso["casos_desbloqueados"] = max(estado_progreso["casos_desbloqueados"], 3)
                            mejor_puntaje = max(estado_progreso["puntajes_casos"][2], estado_progreso.get("ultimo_puntaje", 0))
                            estado_progreso["puntajes_casos"][2] = mejor_puntaje
                        estado_menu = "principal"
                    elif caso_seleccionado == 3:
                        resultado = Caso3.ejecutar_caso3(pantalla, reloj, ANCHO, ALTO, dificultad_elegida, estado_progreso)
                        if resultado == "caso_completado":
                            estado_progreso["casos_desbloqueados"] = max(estado_progreso["casos_desbloqueados"], 4)
                            mejor_puntaje = max(estado_progreso["puntajes_casos"][3], estado_progreso.get("ultimo_puntaje", 0))
                            estado_progreso["puntajes_casos"][3] = mejor_puntaje
                        estado_menu = "principal"

    pygame.display.flip()
    reloj.tick(60)