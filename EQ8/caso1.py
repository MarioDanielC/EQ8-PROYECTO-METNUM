import pygame
import sys
import random
import os
import math
from banco_problemas import banco

def centrar_x(texto_render, ancho_pantalla):
    return (ancho_pantalla - texto_render.get_width()) // 2

def ejecutar_caso1(pantalla, reloj, ancho, alto, dificultad="facil"):
    res = ejecutar_fase(pantalla, reloj, ancho, alto, dificultad, 1)
    if res == "siguiente_escenario":
        res = ejecutar_fase(pantalla, reloj, ancho, alto, dificultad, 2)
        if res == "siguiente_escenario":
            res = ejecutar_fase(pantalla, reloj, ancho, alto, dificultad, 3)
            if res == "siguiente_escenario":
                return "menu"
    return res

def ejecutar_fase(pantalla, reloj, ancho, alto, dificultad, fase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Fuentes
    titulo_fuente = pygame.font.SysFont("Arial", 36, bold=True)
    texto_fuente = pygame.font.SysFont("Arial", 22)
    texto_pista_fuente = pygame.font.SysFont("Arial", 18)
    input_fuente = pygame.font.SysFont("Arial", 28, bold=True)
    
    # Colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    AZUL = (50, 120, 255)
    ROJO = (255, 50, 50)
    VERDE = (50, 200, 50)
    GRIS = (60, 60, 60)
    AMARILLO = (255, 200, 50)
    
    # Selección aleatoria del problema
    problema = random.choice(banco)
    
    # Configurar tiempos según dificultad
    if dificultad == "facil":
        tiempo_limite_seg = 30 * 60
    elif dificultad == "intermedio":
        tiempo_limite_seg = 20 * 60
    elif dificultad == "dificil":
        tiempo_limite_seg = 15 * 60
    else:
        tiempo_limite_seg = 30 * 60
        
    penalizacion_pista_seg = 4 * 60
    
    mensajes_error = ""
    texto_usuario = ""
    
    estado = "INTRO"
    estado_anterior = None
    tiempo_entrada_pausa = 0
    tiempo_inicio = pygame.time.get_ticks()
    penalizacion_total = 0
    
    # Leer directamente los pasos estructurados del banco de problemas
    pasos_finales = problema["pasos_juego"]
    
    paso_actual = 0
    pista_revelada = False
    
    # Botones
    btn_continuar = pygame.Rect(ancho//2 - 150, alto - 100, 300, 60)
    btn_pista = pygame.Rect(20, 20, 180, 40)
    btn_enviar = pygame.Rect(ancho//2 - 100, alto - 80, 200, 50)
    btn_volver = pygame.Rect(ancho//2 - 150, alto - 100, 300, 60)
    btn_comisaria = pygame.Rect(ancho//2 - 150, alto - 100, 300, 60)
    
    try:
        icono_home = pygame.image.load(os.path.join(BASE_DIR, "fondos", "home.png")).convert_alpha()
        icono_home = pygame.transform.scale(icono_home, (40, 40))
        btn_menu_principal = pygame.Rect(20, alto - 60, 40, 40)
    except FileNotFoundError:
        icono_home = None
        btn_menu_principal = pygame.Rect(20, alto - 60, 160, 40)
    
    btn_conf_si = pygame.Rect(ancho//2 - 160, alto//2 + 50, 140, 50)
    btn_conf_no = pygame.Rect(ancho//2 + 20, alto//2 + 50, 140, 50)
    
    try:
        if fase == 1:
            fondo = pygame.image.load(os.path.join(BASE_DIR, "fondos", "cajafuerte.jpeg")).convert()
        elif fase == 2:
            fondo = pygame.image.load(os.path.join(BASE_DIR, "fondos", "comisaria.png")).convert()
        elif fase == 3:
            fondo = pygame.image.load(os.path.join(BASE_DIR, "fondos", "interrogatorio.png")).convert()
        else:
            fondo = pygame.image.load(os.path.join(BASE_DIR, "fondos", "cajafuerte.jpeg")).convert()
        fondo = pygame.transform.scale(fondo, (ancho, alto))
    except FileNotFoundError:
        fondo = pygame.Surface((ancho, alto))
        fondo.fill((30, 40, 50))
    
    corriendo = True
    resultado_salida = "menu"
    
    while corriendo:
        
        pantalla.blit(fondo, (0, 0))
        
        overlay = pygame.Surface((ancho, alto))
        overlay.set_alpha(190)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        
        tiempo_restante = 0
        if estado == "INTRO":
            tiempo_inicio = pygame.time.get_ticks() 
        elif estado == "JUGANDO":
            tiempo_actual = pygame.time.get_ticks()
            segundos_transcurridos = (tiempo_actual - tiempo_inicio) // 1000
            tiempo_restante = tiempo_limite_seg - segundos_transcurridos - penalizacion_total
            
            if tiempo_restante <= 0:
                tiempo_restante = 0
                estado = "PISTA_NO_ENCONTRADA"
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == "CONFIRMAR_SALIDA":
                    if btn_conf_si.collidepoint(evento.pos):
                        corriendo = False
                        resultado_salida = "menu"
                    elif btn_conf_no.collidepoint(evento.pos):
                        estado = estado_anterior
                        if estado == "JUGANDO":
                            tiempo_pausado = pygame.time.get_ticks() - tiempo_entrada_pausa
                            tiempo_inicio += tiempo_pausado
                else:
                    if btn_menu_principal.collidepoint(evento.pos):
                        estado_anterior = estado
                        estado = "CONFIRMAR_SALIDA"
                        tiempo_entrada_pausa = pygame.time.get_ticks()
                        continue
                        
                if estado == "INTRO" and btn_continuar.collidepoint(evento.pos):
                    estado = "JUGANDO"
                    tiempo_inicio = pygame.time.get_ticks()
                    
                elif estado == "JUGANDO":
                    if btn_enviar.collidepoint(evento.pos):
                        resp_correcta = str(pasos_finales[paso_actual]["respuesta"]).replace(" ", "").lower()
                        usr_val = texto_usuario.replace(" ", "").lower()
                        
                        es_correcta = False
                        if usr_val == resp_correcta:
                            es_correcta = True
                        else:
                            try:
                                if abs(float(usr_val) - float(resp_correcta)) < 0.05:
                                    es_correcta = True
                            except ValueError:
                                pass
                                
                        if es_correcta:
                            paso_actual += 1
                            texto_usuario = ""
                            mensajes_error = ""
                            pista_revelada = False
                            if paso_actual >= len(pasos_finales):
                                estado = "PISTA_ENCONTRADA"
                        else:
                            mensajes_error = "Respuesta incorrecta. Intenta de nuevo."
                    
                    elif btn_pista.collidepoint(evento.pos):
                        if not pista_revelada:
                            pista_revelada = True
                            penalizacion_total += penalizacion_pista_seg
                            
                elif estado == "PISTA_ENCONTRADA":
                    if btn_comisaria.collidepoint(evento.pos):
                        corriendo = False
                        resultado_salida = "siguiente_escenario" # Para ir a la comisaría
                        
                elif estado == "PISTA_NO_ENCONTRADA":
                    if btn_volver.collidepoint(evento.pos):
                        corriendo = False
                        resultado_salida = "menu"
                            
            if evento.type == pygame.KEYDOWN and estado == "JUGANDO":
                if evento.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    resp_correcta = str(pasos_finales[paso_actual]["respuesta"]).replace(" ", "").lower()
                    usr_val = texto_usuario.replace(" ", "").lower()
                    
                    es_correcta = False
                    if usr_val == resp_correcta:
                        es_correcta = True
                    else:
                        try:
                            if abs(float(usr_val) - float(resp_correcta)) < 0.05:
                                es_correcta = True
                        except ValueError:
                            pass
                            
                    if es_correcta:
                        paso_actual += 1
                        texto_usuario = ""
                        mensajes_error = ""
                        pista_revelada = False
                        if paso_actual >= len(pasos_finales):
                            estado = "PISTA_ENCONTRADA"
                    else:
                        mensajes_error = "Respuesta incorrecta. Intenta de nuevo."
                else:
                    if evento.unicode.isprintable():
                        texto_usuario += evento.unicode
                        
        # ---------------- DRAW ----------------
        if estado == "INTRO":
            if fase == 1:
                tit = titulo_fuente.render("CASO 01: La Caja Fuerte", True, BLANCO)
                lineas = [
                    "Has encontrado una caja fuerte con un candado digital.",
                    "Para abrirla, debes resolver el siguiente problema de",
                    f"M\u00e9todo Num\u00e9rico: {problema['metodo']}",
                    "",
                    "Se te pedir\u00e1n pasos intermedios antes de la respuesta final.",
                    "Las pistas cuestan 4 minutos y te dar\u00e1n el procedimiento."
                ]
            elif fase == 2:
                tit = titulo_fuente.render("CASO 01: La Comisar\u00eda", True, BLANCO)
                lineas = [
                    "Al llegar a la comisar\u00eda, encuentras un sobre con",
                    "el nombre de dos sospechosos. Para descifrarlo,",
                    "tendr\u00e1s que resolver el siguiente problema de",
                    f"M\u00e9todo Num\u00e9rico: {problema['metodo']}",
                    "",
                    "Las pistas cuestan 4 minutos de tu tiempo."
                ]
            else:
                tit = titulo_fuente.render("CASO 01: El Interrogatorio", True, BLANCO)
                lineas = [
                    "Est\u00e1s en la sala de interrogatorio con los sospechosos.",
                    "Para saber qui\u00e9n es el culpable, eval\u00faa la evidencia",
                    "resolviendo el siguiente problema de",
                    f"M\u00e9todo Num\u00e9rico: {problema['metodo']}",
                    "",
                    "¡Es tu \u00faltima prueba, detective!"
                ]
                
            pantalla.blit(tit, (centrar_x(tit, ancho), 100))
            
            for idx, linea in enumerate(lineas):
                txt = texto_fuente.render(linea, True, BLANCO)
                pantalla.blit(txt, (centrar_x(txt, ancho), 200 + idx*40))
                
            pygame.draw.rect(pantalla, AZUL, btn_continuar, border_radius=10)
            txt_btn = texto_fuente.render("Empezar a resolver", True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_continuar.y + 15))
            
        elif estado == "JUGANDO":
            mins = tiempo_restante // 60
            secs = tiempo_restante % 60
            color_tiempo = BLANCO if tiempo_restante > 60 else ROJO
            txt_tiempo = titulo_fuente.render(f"{mins:02d}:{secs:02d}", True, color_tiempo)
            pantalla.blit(txt_tiempo, (ancho - 150, 20))
            
            pygame.draw.rect(pantalla, AMARILLO, btn_pista, border_radius=5)
            txt_pista = texto_fuente.render("Pista (-4 min)", True, NEGRO)
            pantalla.blit(txt_pista, (btn_pista.x + 20, btn_pista.y + 5))
            
            tit_datos = titulo_fuente.render(f"M\u00e9todo: {problema['metodo']}", True, AZUL)
            pantalla.blit(tit_datos, (centrar_x(tit_datos, ancho), 30))
            
            txt_prob = texto_fuente.render(problema["problema"], True, BLANCO)
            pantalla.blit(txt_prob, (centrar_x(txt_prob, ancho), 80))
            
            txt_val = texto_fuente.render(problema["valores"], True, VERDE)
            pantalla.blit(txt_val, (centrar_x(txt_val, ancho), 110))
            
            inst_txt = texto_fuente.render(f"Paso {paso_actual+1}/{len(pasos_finales)} - {pasos_finales[paso_actual]['pregunta']}", True, AMARILLO)
            pantalla.blit(inst_txt, (centrar_x(inst_txt, ancho), 460))
            
            pygame.draw.rect(pantalla, GRIS, (ancho//2 - 250, 500, 500, 50), border_radius=8)
            
            txt_inp = input_fuente.render(texto_usuario, True, BLANCO)
            if txt_inp.get_width() > 480:
                offsetX = txt_inp.get_width() - 480
                superficie_recorte = pygame.Surface((480, 50), pygame.SRCALPHA)
                superficie_recorte.blit(txt_inp, (-offsetX, 10))
                pantalla.blit(superficie_recorte, (ancho//2 - 240, 500))
            else:
                pantalla.blit(txt_inp, (ancho//2 - 240, 510))
            
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                cursor_x = ancho//2 - 240 + min(txt_inp.get_width(), 480) + 2
                pygame.draw.line(pantalla, BLANCO, (cursor_x, 515), (cursor_x, 535), 2)
                                 
            if mensajes_error:
                err = texto_fuente.render(mensajes_error, True, ROJO)
                pantalla.blit(err, (centrar_x(err, ancho), 560))
                
            pygame.draw.rect(pantalla, AZUL, btn_enviar, border_radius=10)
            btn_env_txt = texto_fuente.render("Comprobar", True, BLANCO)
            pantalla.blit(btn_env_txt, (centrar_x(btn_env_txt, ancho), btn_enviar.y + 10))
            
            if pista_revelada:
                p_txt = texto_pista_fuente.render("Pista: " + pasos_finales[paso_actual]["pista"], True, AMARILLO)
                pantalla.blit(p_txt, (centrar_x(p_txt, ancho), 160))
                
        elif estado == "PISTA_ENCONTRADA":
            if fase == 1:
                tit_victoria = "\u00a1Caja Fuerte Abierta!"
                pista_txt = '"\u00a1El culpable est\u00e1 en la comisar\u00eda!"'
                txt_btn_avanzar = "Ir a la Comisar\u00eda"
            elif fase == 2:
                tit_victoria = "\u00a1Sobre Descifrado!"
                pista_txt = '"Los sospechosos apuntan al interrogatorio..."'
                txt_btn_avanzar = "Ir al Interrogatorio"
            else:
                tit_victoria = "\u00a1CASO RESUELTO!"
                pista_txt = '"¡El culpable ha sido encontrado, felicidades!"'
                txt_btn_avanzar = "Volver al Men\u00fa Principal"
                
            tit = titulo_fuente.render(tit_victoria, True, VERDE)
            pantalla.blit(tit, (centrar_x(tit, ancho), 150))
            
            msg = texto_fuente.render("Has resuelto todos los pasos del m\u00e9todo num\u00e9rico.", True, BLANCO)
            pantalla.blit(msg, (centrar_x(msg, ancho), 250))
            
            pista = titulo_fuente.render(pista_txt, True, AZUL)
            pantalla.blit(pista, (centrar_x(pista, ancho), 350))
            
            pygame.draw.rect(pantalla, AZUL, btn_comisaria, border_radius=10)
            txt_btn = texto_fuente.render(txt_btn_avanzar, True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_comisaria.y + 15))
            
        elif estado == "PISTA_NO_ENCONTRADA":
            tit = titulo_fuente.render("Tiempo Agotado", True, ROJO)
            pantalla.blit(tit, (centrar_x(tit, ancho), 150))
            
            msg = texto_fuente.render("No pudiste abrir la caja fuerte a tiempo.", True, BLANCO)
            pantalla.blit(msg, (centrar_x(msg, ancho), 250))
            
            pygame.draw.rect(pantalla, AZUL, btn_volver, border_radius=10)
            txt_btn = texto_fuente.render("Volver al Men\u00fa Principal", True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_volver.y + 15))
            
        elif estado == "CONFIRMAR_SALIDA":
            # Fondo semi-transparente para el pop-up
            oscuro = pygame.Surface((ancho, alto))
            oscuro.set_alpha(200)
            oscuro.fill(NEGRO)
            pantalla.blit(oscuro, (0, 0))
            
            # Caja de confirmacion
            caja_rect = pygame.Rect(ancho//2 - 250, alto//2 - 100, 500, 200)
            pygame.draw.rect(pantalla, GRIS, caja_rect, border_radius=15)
            pygame.draw.rect(pantalla, BLANCO, caja_rect, width=3, border_radius=15)
            
            msg = titulo_fuente.render("\u00bfSeguro que deseas salir?", True, BLANCO)
            pantalla.blit(msg, (centrar_x(msg, ancho), alto//2 - 60))
            
            pygame.draw.rect(pantalla, ROJO, btn_conf_si, border_radius=10)
            txt_si = texto_fuente.render("S\u00ed", True, BLANCO)
            pantalla.blit(txt_si, (btn_conf_si.x + (140 - txt_si.get_width())//2, btn_conf_si.y + 10))
            
            pygame.draw.rect(pantalla, AZUL, btn_conf_no, border_radius=10)
            txt_no = texto_fuente.render("No", True, BLANCO)
            pantalla.blit(txt_no, (btn_conf_no.x + (140 - txt_no.get_width())//2, btn_conf_no.y + 10))

        if estado != "CONFIRMAR_SALIDA":
            if icono_home:
                pygame.draw.rect(pantalla, ROJO, btn_menu_principal, border_radius=8)
                pantalla.blit(icono_home, (btn_menu_principal.x, btn_menu_principal.y))
            else:
                pygame.draw.rect(pantalla, ROJO, btn_menu_principal, border_radius=8)
                txt_menu = texto_pista_fuente.render("Men\u00fa Principal", True, BLANCO)
                pantalla.blit(txt_menu, (btn_menu_principal.x + 10, btn_menu_principal.y + 10))

        pygame.display.flip()
        reloj.tick(60)

    return resultado_salida
