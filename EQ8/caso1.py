import pygame
import sys
import random
import os
import math

def centrar_x(texto_render, ancho_pantalla):
    return (ancho_pantalla - texto_render.get_width()) // 2

def ejecutar_caso1(pantalla, reloj, ancho, alto, dificultad="facil"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Fuentes
    titulo_fuente = pygame.font.SysFont("Arial", 48, bold=True)
    texto_fuente = pygame.font.SysFont("Arial", 28)
    input_fuente = pygame.font.SysFont("Arial", 36, bold=True)
    
    # Colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    AZUL = (50, 120, 255)
    ROJO = (255, 50, 50)
    VERDE = (50, 200, 50)
    GRIS = (60, 60, 60)
    AMARILLO = (255, 200, 50)
    
    # Tipo de problema aleatorio según dificultad
    if dificultad == "facil":
        metodos_disponibles = ["newton_adelante", "lagrange", "diferencias_divididas"]
    elif dificultad == "intermedio":
        # TODO: Implementar métodos intermedios reales (Ej: Bisección, Newton-Raphson)
        # Por ahora usaremos lagrange como placeholder temporal para probar la UI
        metodos_disponibles = ["lagrange"]
    elif dificultad == "dificil":
        # TODO: Implementar métodos difíciles (Ej: Euler, Runge-Kutta)
        # Por ahora usaremos diferencias_divididas como placeholder temporal
        metodos_disponibles = ["diferencias_divididas"]
    else:
        metodos_disponibles = ["newton_adelante"]
        
    tipo_metodo = random.choice(metodos_disponibles)

    # Generar problema
    h = random.randint(1, 3)
    x0 = random.randint(0, 5)
    x1 = x0 + h
    
    if tipo_metodo == "newton_adelante":
        x2 = x1 + h
    else:
        # En Lagrange o Dif. Divididas no es obligatorio estar equiespaciado
        x2 = x1 + random.randint(1, 3)
    
    # Generar "función" oculta para tener datos enteros bonitos
    a, b, c = random.randint(-2, 2), random.randint(-5, 5), random.randint(1, 10)
    if a == 0: a = 1
    
    y0 = a*(x0**2) + b*x0 + c
    y1 = a*(x1**2) + b*x1 + c
    y2 = a*(x2**2) + b*x2 + c
    
    x_eval = x0 + (x2 - x0) / 2.0

    if tipo_metodo == "newton_adelante":
        dy0 = y1 - y0
        dy1 = y2 - y1
        d2y0 = dy1 - dy0
        p = (x_eval - x0) / h
        resultado_final = y0 + p * dy0 + (p * (p - 1) / 2.0) * d2y0
        
        respuestas_correctas = [str(dy0), str(d2y0), f"{resultado_final:.4f}".rstrip('0').rstrip('.')]
        mensajes_paso = [
            "1. Calcula la 1ra diferencia finita \u0394y0 (y1 - y0)",
            "2. Calcula la 2da diferencia finita \u0394\u00b2y0 (\u0394y1 - \u0394y0)",
            f"3. Calcula f({x_eval}) usando Newton hacia adelante"
        ]
        texto_instruccion = f"Resuelve con Interpolaci\u00f3n de Newton para hallar f({x_eval})."
        
    elif tipo_metodo == "lagrange":
        l0 = ((x_eval - x1)*(x_eval - x2)) / ((x0 - x1)*(x0 - x2))
        l1 = ((x_eval - x0)*(x_eval - x2)) / ((x1 - x0)*(x1 - x2))
        l2 = ((x_eval - x0)*(x_eval - x1)) / ((x2 - x0)*(x2 - x1))
        resultado_final = y0*l0 + y1*l1 + y2*l2
        
        respuestas_correctas = [f"{l0:.4f}".rstrip('0').rstrip('.'), f"{l1:.4f}".rstrip('0').rstrip('.'), f"{l2:.4f}".rstrip('0').rstrip('.'), f"{resultado_final:.4f}".rstrip('0').rstrip('.')]
        mensajes_paso = [
            f"1. Calcula el valor de L0({x_eval})",
            f"2. Calcula el valor de L1({x_eval})",
            f"3. Calcula el valor de L2({x_eval})",
            f"4. Calcula f({x_eval}) (Suma de L_i * y_i)"
        ]
        texto_instruccion = f"Resuelve con Interpolaci\u00f3n de Lagrange para hallar f({x_eval})."

    elif tipo_metodo == "diferencias_divididas":
        f_x0_x1 = (y1 - y0) / (x1 - x0)
        f_x1_x2 = (y2 - y1) / (x2 - x1)
        f_x0_x1_x2 = (f_x1_x2 - f_x0_x1) / (x2 - x0)
        resultado_final = y0 + f_x0_x1*(x_eval - x0) + f_x0_x1_x2*(x_eval - x0)*(x_eval - x1)
        
        respuestas_correctas = [f"{f_x0_x1:.4f}".rstrip('0').rstrip('.'), f"{f_x1_x2:.4f}".rstrip('0').rstrip('.'), f"{f_x0_x1_x2:.4f}".rstrip('0').rstrip('.'), f"{resultado_final:.4f}".rstrip('0').rstrip('.')]
        mensajes_paso = [
            "1. Calcula la primera dif. dividida f[x0, x1]",
            "2. Calcula la primera dif. dividida f[x1, x2]",
            "3. Calcula la segunda dif. dividida f[x0, x1, x2]",
            f"4. Calcula f({x_eval}) con el polinomio de Newton"
        ]
        texto_instruccion = f"Usa Diferencias Divididas de Newton para hallar f({x_eval})."
    
    mensajes_error = ""
    texto_usuario = ""
    paso_actual = 0
    
    estado = "INTRO"
    
    # Tiempos
    tiempo_limite_seg = 300 # 5 min
    penalizacion_pista = 0
    tiempo_inicio = pygame.time.get_ticks()
    
    # Botones
    btn_continuar = pygame.Rect(ancho//2 - 150, alto - 100, 300, 60)
    btn_pista = pygame.Rect(20, 20, 150, 40)
    btn_enviar = pygame.Rect(ancho//2 - 100, alto - 150, 200, 50)
    btn_volver = pygame.Rect(ancho//2 - 150, alto - 100, 300, 60)
    
    pistas_dadas = []
    if tipo_metodo == "newton_adelante":
        lista_pistas = [
            "Pista 1: Para \u0394y0 resta el valor de y1 menos y0",
            "Pista 2: Para \u0394\u00b2y0 resta \u0394y1 menos \u0394y0",
            "Pista 3: f(x) = y0 + p*\u0394y0 + [p(p-1)/2]*\u0394\u00b2y0",
            "Pista 4: p = (x - x0) / h"
        ]
    elif tipo_metodo == "lagrange":
        lista_pistas = [
            "Pista 1: L0(x) = [(x-x1)(x-x2)] / [(x0-x1)(x0-x2)]",
            "Pista 2: L1(x) = [(x-x0)(x-x2)] / [(x1-x0)(x1-x2)]",
            "Pista 3: L2(x) = [(x-x0)(x-x1)] / [(x2-x0)(x2-x1)]",
            "Pista 4: Multiplica cada L por su 'y' y sumalos"
        ]
    elif tipo_metodo == "diferencias_divididas":
        lista_pistas = [
            "Pista 1: f[x0, x1] = (y1 - y0) / (x1 - x0)",
            "Pista 2: f[x1, x2] = (y2 - y1) / (x2 - x1)",
            "Pista 3: f[x0, x1, x2] = (f[x1, x2] - f[x0, x1]) / (x2 - x0)",
            "Pista 4: f(x) = y0 + f[x0, x1](x-x0) + f[x0, x1, x2](x-x0)(x-x1)"
        ]
    indice_pista = 0

    try:
        fondo_caja = pygame.image.load(os.path.join(BASE_DIR, "fondos", "cajafuerte.jpeg"))
        fondo_caja = pygame.transform.scale(fondo_caja, (ancho, alto))
    except FileNotFoundError:
        try:
            fondo_caja = pygame.image.load(os.path.join(BASE_DIR, "fondos", "cajafuerte.jpg"))
            fondo_caja = pygame.transform.scale(fondo_caja, (ancho, alto))
        except FileNotFoundError:
            try:
                fondo_caja = pygame.image.load(os.path.join(BASE_DIR, "fondos", "cajafuerte.png"))
                fondo_caja = pygame.transform.scale(fondo_caja, (ancho, alto))
            except FileNotFoundError:
                fondo_caja = pygame.Surface((ancho, alto))
                fondo_caja.fill((30, 40, 50)) # Color oscuro de fondo
    
    corriendo = True
    resultado_salida = "menu"
    
    while corriendo:
        
        pantalla.blit(fondo_caja, (0, 0))
        
        # Oscurecer un poco la imagen de fondo para no perder la legibilidad del texto
        overlay = pygame.Surface((ancho, alto))
        overlay.set_alpha(170)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        
        # Calcular tiempo en estado JUGANDO
        tiempo_restante = 0
        if estado == "INTRO":
            tiempo_inicio = pygame.time.get_ticks() # Mantiene el inicio hasta salir de intro
        elif estado == "JUGANDO":
            tiempo_actual = pygame.time.get_ticks()
            segundos_transcurridos = (tiempo_actual - tiempo_inicio) // 1000
            tiempo_restante = tiempo_limite_seg - segundos_transcurridos - penalizacion_pista
            
            if tiempo_restante <= 0:
                tiempo_restante = 0
                estado = "PISTA_NO_ENCONTRADA"
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == "INTRO" and btn_continuar.collidepoint(evento.pos):
                    estado = "JUGANDO"
                    tiempo_inicio = pygame.time.get_ticks() # Comienza el tiempo
                    
                elif estado == "JUGANDO":
                    if btn_enviar.collidepoint(evento.pos):
                        # Validar respuesta
                        try:
                            # Permitimos pequeño error decimal
                            usr_val = float(texto_usuario)
                            correct_val = float(respuestas_correctas[paso_actual])
                            if abs(usr_val - correct_val) < 0.05:
                                paso_actual += 1
                                texto_usuario = ""
                                mensajes_error = ""
                                if paso_actual >= len(respuestas_correctas):
                                    estado = "PISTA_ENCONTRADA"
                            else:
                                mensajes_error = "Respuesta incorrecta. Intenta de nuevo."
                        except ValueError:
                            mensajes_error = "Formato inv\u00e1lido. Ingresa un n\u00famero."
                    
                    elif btn_pista.collidepoint(evento.pos):
                        if indice_pista < len(lista_pistas):
                            pistas_dadas.append(lista_pistas[indice_pista])
                            indice_pista += 1
                            penalizacion_pista += 5
                            
                elif estado in ["PISTA_ENCONTRADA", "PISTA_NO_ENCONTRADA"]:
                    if btn_volver.collidepoint(evento.pos):
                        corriendo = False
                        if estado == "PISTA_ENCONTRADA":
                            resultado_salida = "siguiente_escenario"
                        else:
                            resultado_salida = "menu"
                            
            if evento.type == pygame.KEYDOWN and estado == "JUGANDO":
                if evento.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    # Simular click en enviar
                    try:
                        usr_val = float(texto_usuario)
                        correct_val = float(respuestas_correctas[paso_actual])
                        if abs(usr_val - correct_val) < 0.05:
                            paso_actual += 1
                            texto_usuario = ""
                            mensajes_error = ""
                            if paso_actual >= len(respuestas_correctas):
                                estado = "PISTA_ENCONTRADA"
                        else:
                            mensajes_error = "Respuesta incorrecta. Intenta de nuevo."
                    except ValueError:
                        mensajes_error = "Formato inv\u00e1lido. Ingresa un n\u00famero."
                else:
                    if evento.unicode.isprintable(): # Solo admitimos caracteres escribibles
                        texto_usuario += evento.unicode
                        
        # ---------------- DRAW ----------------
        if estado == "INTRO":
            tit = titulo_fuente.render("CASO 01: La Caja Fuerte", True, BLANCO)
            pantalla.blit(tit, (centrar_x(tit, ancho), 100))
            
            lineas = [
                "En una caja fuerte se encuentra evidencia vital para el caso.",
                "Pero la combinación est\u00e1 fragmentada en problemas de",
                "m\u00e9todos num\u00e9ricos. Alguien protegi\u00f3 esto con matem\u00e1ticas.",
                "",
                texto_instruccion
            ]
            
            for idx, linea in enumerate(lineas):
                txt = texto_fuente.render(linea, True, BLANCO)
                pantalla.blit(txt, (centrar_x(txt, ancho), 200 + idx*40))
                
            pygame.draw.rect(pantalla, AZUL, btn_continuar, border_radius=10)
            txt_btn = texto_fuente.render("Continuar", True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_continuar.y + 15))
            
        elif estado == "JUGANDO":
            # Tiempo
            mins = tiempo_restante // 60
            secs = tiempo_restante % 60
            color_tiempo = BLANCO if tiempo_restante > 60 else ROJO
            txt_tiempo = titulo_fuente.render(f"{mins:02d}:{secs:02d}", True, color_tiempo)
            pantalla.blit(txt_tiempo, (ancho - 150, 20))
            
            # Boton Pista
            pygame.draw.rect(pantalla, AMARILLO, btn_pista, border_radius=5)
            txt_pista = texto_fuente.render("Pista (-5s)", True, NEGRO)
            pantalla.blit(txt_pista, (btn_pista.x + 10, btn_pista.y + 5))
            
            # Datos de la tabla
            tit_datos = titulo_fuente.render("Datos del problema:", True, AZUL)
            pantalla.blit(tit_datos, (centrar_x(tit_datos, ancho), 50))
            
            tabla_txt = f"x0 = {x0}, y0 = {y0}  |  x1 = {x1}, y1 = {y1}  |  x2 = {x2}, y2 = {y2}"
            txt_tb = texto_fuente.render(tabla_txt, True, BLANCO)
            pantalla.blit(txt_tb, (centrar_x(txt_tb, ancho), 120))
            
            # Pasos e instrucciones
            inst_txt = titulo_fuente.render(mensajes_paso[paso_actual], True, VERDE)
            pantalla.blit(inst_txt, (centrar_x(inst_txt, ancho), 220))
            
            # Area de Input
            pygame.draw.rect(pantalla, GRIS, (ancho//2 - 200, 320, 400, 60), border_radius=8)
            txt_inp = input_fuente.render(texto_usuario, True, BLANCO)
            pantalla.blit(txt_inp, (ancho//2 - 180, 330))
            
            # Cursor
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                pygame.draw.line(pantalla, BLANCO, (ancho//2 - 180 + txt_inp.get_width() + 5, 335),
                                 (ancho//2 - 180 + txt_inp.get_width() + 5, 365), 2)
                                 
            # Mensaje de error
            if mensajes_error:
                err = texto_fuente.render(mensajes_error, True, ROJO)
                pantalla.blit(err, (centrar_x(err, ancho), 400))
                
            # Boton enviar
            pygame.draw.rect(pantalla, AZUL, btn_enviar, border_radius=10)
            btn_env_txt = texto_fuente.render("Enviar (ENTER)", True, BLANCO)
            pantalla.blit(btn_env_txt, (centrar_x(btn_env_txt, ancho), btn_enviar.y + 10))
            
            # Pistas mostradas
            for idx, p in enumerate(pistas_dadas):
                p_txt = texto_fuente.render(p, True, AMARILLO)
                pantalla.blit(p_txt, (50, 480 + idx*30))
                
        elif estado == "PISTA_ENCONTRADA":
            tit = titulo_fuente.render("\u00a1Pista Encontrada!", True, VERDE)
            pantalla.blit(tit, (centrar_x(tit, ancho), 150))
            
            msg = texto_fuente.render("La caja fuerte se ha abierto.", True, BLANCO)
            pantalla.blit(msg, (centrar_x(msg, ancho), 250))
            
            pista = titulo_fuente.render('"El culpable trabaja en la comisar\u00eda"', True, AZUL)
            pantalla.blit(pista, (centrar_x(pista, ancho), 350))
            
            pygame.draw.rect(pantalla, AZUL, btn_volver, border_radius=10)
            txt_btn = texto_fuente.render("Avanzar", True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_volver.y + 15))
            
        elif estado == "PISTA_NO_ENCONTRADA":
            tit = titulo_fuente.render("Pista no encontrada", True, ROJO)
            pantalla.blit(tit, (centrar_x(tit, ancho), 150))
            
            msg = texto_fuente.render("No pudiste resolver el caso a tiempo.", True, BLANCO)
            pantalla.blit(msg, (centrar_x(msg, ancho), 250))
            
            pygame.draw.rect(pantalla, AZUL, btn_volver, border_radius=10)
            txt_btn = texto_fuente.render("Volver al Men\u00fa Principal", True, BLANCO)
            pantalla.blit(txt_btn, (centrar_x(txt_btn, ancho), btn_volver.y + 15))

        pygame.display.flip()
        reloj.tick(60)

    return resultado_salida
