# banco_problemas.py

banco = [
    {
        "id": 1,
        "metodo": "Interpolación Lineal",
        "problema": "Estimar el Ln de 4 mediante interpolación lineal realizando el cálculo entre Ln 2 y Ln 5.",
        "valores": "a = 2, b = 5",
        "procedimiento": [
            "Ln 2 = 0.69314718",
            "Ln 5 = 1.609437912",
            "f(a) = Ln 2 = 0.69314718",
            "f(b) = Ln 5 = 1.609437912",
            "x = 4",
            "f(x) = Ln 4 = 1.386294361",
            "g(x) = ((1.609437912 - 0.69314718) / (5 - 2)) * (4 - 2) + 0.69314718",
            "g(x) = 1.304007668",
            "\u03B5 = |1.386294361 - 1.304007668|",
            "\u03B5 = 0.082286693"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de f(a)", "pista": "Sustituye 'a' en la función Ln.", "respuesta": "0.69314718"},
            {"pregunta": "Calcula el valor de f(b)", "pista": "Sustituye 'b' en la función Ln.", "respuesta": "1.609437912"},
            {"pregunta": "Calcula el valor final de g(x)", "pista": "Usa la fórmula: ((f(b) - f(a)) / (b - a)) * (x - a) + f(a)", "respuesta": "1.304007668"},
            {"pregunta": "Calcula el Error absoluto \u03B5", "pista": "\u03B5 = |f(x) - g(x)|", "respuesta": "0.082286693"}
        ],
        "respuesta_final": "1.304007668"
    },
    {
        "id": 2,
        "metodo": "Interpolación Lineal",
        "problema": "Estimar el Ln de 4 mediante interpolación lineal con intervalos menores de Ln 3 y Ln 5.",
        "valores": "a = 3, b = 5",
        "procedimiento": [
            "Ln 3 = 1.098612289",
            "Ln 5 = 1.609437912",
            "f(a) = Ln 3 = 1.098612289",
            "f(b) = Ln 5 = 1.609437912",
            "x = 4",
            "f(x) = Ln 4 = 1.386294361",
            "g(x) = ((1.609437912 - 1.098612289) / (5 - 3)) * (4 - 3) + 1.098612289",
            "g(x) = 1.354025101",
            "\u03B5 = |1.386294361 - 1.354025101|",
            "\u03B5 = 0.03226926"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de f(a)", "pista": "Sustituye 'a' en la función Ln.", "respuesta": "1.098612289"},
            {"pregunta": "Calcula el valor de f(b)", "pista": "Sustituye 'b' en la función Ln.", "respuesta": "1.609437912"},
            {"pregunta": "Calcula el valor final de g(x)", "pista": "Usa la fórmula: ((f(b) - f(a)) / (b - a)) * (x - a) + f(a)", "respuesta": "1.354025101"},
            {"pregunta": "Calcula el Error absoluto \u03B5", "pista": "\u03B5 = |f(x) - g(x)|", "respuesta": "0.03226926"}
        ],
        "respuesta_final": "1.354025101"
    },
    {
        "id": 3,
        "metodo": "Newton hacia Adelante",
        "problema": "Obtener g(x) para x = 2.4",
        "valores": "X1=2.2 (y1=2.54), X2=2.5 (y2=2.82), X3=2.8 (y3=3.21)",
        "procedimiento": [
            "h1 = |x2 - x1| = |2.5 - 2.2| = 0.3",
            "h2 = |x3 - x2| = |2.8 - 2.5| = 0.3",
            "\u0394'1 = y2 - y1 = 2.82 - 2.54 = 0.28",
            "\u0394'2 = y3 - y2 = 3.21 - 2.82 = 0.39",
            "\u0394\u00B21 = \u0394'2 - \u0394'1 = 0.39 - 0.28 = 0.11",
            "s = (x - xi) / h = (2.4 - 2.2) / 0.3 = 0.666666666",
            "g(x) = yi[s_0] + \u0394'1[s_1] + \u0394\u00B21[ (s(s-1)) / 2! ]",
            "g(x) = 2.54(1) + (0.28)(0.666666666) + (0.11)[ (0.666666666(0.666666666 - 1)) / 2! ]",
            "g(x) = 2.714444444"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula la 1ra diferencia de primer orden \u0394'1", "pista": "Resta y2 - y1", "respuesta": "0.28"},
            {"pregunta": "Calcula la 2da diferencia de primer orden \u0394'2", "pista": "Resta y3 - y2", "respuesta": "0.39"},
            {"pregunta": "Calcula la 1ra diferencia de segundo orden \u0394\u00b21", "pista": "Resta \u0394'2 - \u0394'1", "respuesta": "0.11"},
            {"pregunta": "Calcula el valor de s", "pista": "s = (x - x1) / h", "respuesta": "0.666666666"},
            {"pregunta": "Calcula la respuesta final de g(x)", "pista": "Aplica el polinomio de Newton hacia adelante.", "respuesta": "2.714444444"}
        ],
        "respuesta_final": "2.714444444"
    },
    {
        "id": 4,
        "metodo": "Newton hacia Atrás",
        "problema": "Obtener g(x) para x = 2.4",
        "valores": "X1=2.2 (y1=2.54), X2=2.5 (y2=2.82), X3=2.8 (y3=3.21)",
        "procedimiento": [
            "\u25BD'2 = y2 - y1 = 2.82 - 2.54 = 0.28",
            "\u25BD'1 = y3 - y2 = 3.21 - 2.82 = 0.39",
            "\u25BD\u00B21 = \u25BD'2 - \u25BD'1 = 0.39 - 0.28 = 0.11",
            "s = (x - xi) / h = (2.4 - 2.8) / 0.3 = -1.33333333333",
            "g(x) = yi[s_0] + \u25BD'f(xi)[s_1] + \u25BD\u00B2f(xi)[ (s(s+1)) / 2! ]",
            "g(x) = 3.21(1) + (0.39)(-1.33333333333) + (0.11)[ (-1.33333333333(-1.33333333333 + 1)) / 2! ]",
            "g(x) = 2.714444444"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula \u25BD'2", "pista": "Resta y2 - y1", "respuesta": "0.28"},
            {"pregunta": "Calcula \u25BD'1", "pista": "Resta y3 - y2", "respuesta": "0.39"},
            {"pregunta": "Calcula \u25BD\u00B21", "pista": "Resta \u25BD'1 - \u25BD'2", "respuesta": "0.11"},
            {"pregunta": "Calcula s", "pista": "s = (x - xi) / h, donde xi es el último valor.", "respuesta": "-1.33333333333"},
            {"pregunta": "Calcula la respuesta final de g(x)", "pista": "Aplica el polinomio de Newton hacia atrás.", "respuesta": "2.714444444"}
        ],
        "respuesta_final": "2.714444444"
    },
    {
        "id": 5,
        "metodo": "Newton con Diferencias Divididas",
        "problema": "Encuentre g(x) para x = 3.5",
        "valores": "Xi: 4.4, 3.7, 3.1 | yi: -0.68, -1.59, -1.82",
        "formula": [
            "g(x) = D\u2070 + D1\u00B9(x - x1) + D1\u00B2(x - x1)(x - x2)",
            "",
            "        y2 - y1",
            "D1\u00B9 = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "        x2 - x1",
            "",
            "        y3 - y2",
            "D2\u00B9 = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "        x3 - x2",
            "",
            "       D2\u00B9 - D1\u00B9",
            "D1\u00B2 = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "        x3 - x1"
        ],
        "procedimiento": [
            "h1 = |x2 - x1| = |3.7 - 4.4| = 0.7",
            "h2 = |x3 - x2| = |3.1 - 3.7| = 0.6",
            "D1\u00B9 = (y2 - y1) / (x2 - x1) = (-1.59 - (-0.68)) / (3.7 - 4.4) = 1.3",
            "D2\u00B9 = (y3 - y2) / (x3 - x2) = (-1.82 - (-1.59)) / (3.1 - 3.7) = 0.38333333",
            "D1\u00B2 = (D2\u00B9 - D1\u00B9) / (x3 - x1) = (0.38333333 - 1.3) / (3.1 - 4.4) = 0.705128205",
            "g(x) = D\u2070 + D1\u00B9(x - x1) + D1\u00B2(x - x1)(x - x2)",
            "g(x) = (-0.68) + (1.3)(3.5 - 4.4) + (0.705128205)(3.5 - 4.4)(3.5 - 3.7)",
            "g(x) = -1.723076923"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula la 1ra diferencia dividida D1\u00B9", "pista": "Usa los primeros dos puntos de la tabla: (4.4, -0.68) y (3.7, -1.59).", "respuesta": "1.3"},
            {"pregunta": "Calcula la 1ra diferencia dividida D2\u00B9", "pista": "Usa los dos últimos puntos de la tabla: (3.7, -1.59) y (3.1, -1.82).", "respuesta": "0.38333333"},
            {"pregunta": "Calcula la 2da diferencia dividida D1\u00B2", "pista": "Usa las diferencias de primer orden calculadas y divídelas entre el cambio total (x3 - x1).", "respuesta": "0.705128205"},
            {"pregunta": "Calcula g(x)", "pista": "Sustituye los valores obtenidos en la fórmula para g(x) con x= 3.5", "respuesta": "-1.723076923"}
        ],
        "respuesta_final": "-1.723076923"
    },
    {
        "id": 6,
        "metodo": "Lagrange",
        "problema": "Obtener g(x) para x = 2.4",
        "valores": "X1=2.2 (y1=2.54), X2=2.5 (y2=2.82), X3=2.8 (y3=3.21)",
        "procedimiento": [
            "g(x) = (2.54) * ((2.4 - 2.5)(2.4 - 2.8)) / ((2.2 - 2.5)(2.2 - 2.8)) = 0.564444444444",
            "+ (2.82) * ((2.4 - 2.2)(2.4 - 2.8)) / ((2.5 - 2.2)(2.5 - 2.8)) = 2.5066667",
            "+ (3.21) * ((2.4 - 2.2)(2.4 - 2.5)) / ((2.8 - 2.2)(2.8 - 2.5)) = -0.356666666",
            "g(x) = 2.714444444"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el primer término de g(x)", "pista": "y1 * g1(x)", "respuesta": "0.564444444444"},
            {"pregunta": "Calcula el segundo término de g(x)", "pista": "y2 * g2(x)", "respuesta": "2.5066667"},
            {"pregunta": "Calcula el tercer término de g(x)", "pista": "y3 * g3(x)", "respuesta": "-0.356666666"},
            {"pregunta": "Calcula la respuesta final de g(x)", "pista": "Suma los tres términos.", "respuesta": "2.714444444"}
        ],
        "respuesta_final": "2.714444444"
    },
    {
        "id": 7,
        "metodo": "Método Gráfico",
        "problema": "y = x\u00B3 - 6.5x + 2",
        "valores": "Sin valores iniciales fijos, se evalúan enteros.",
        "procedimiento": [
            "El punto que representa el valor de f(x)=0 ofrece una aproximación inicial de la raíz observando los cambios de signo en x e y.",
            "X=-3, Y=-5.5",
            "X=-2, Y=7",
            "X=-1, Y=7.5",
            "X=0, Y=2",
            "X=1, Y=-3.5",
            "X=2, Y=-3",
            "X=3, Y=9.5"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de Y cuando X=-3", "pista": "Sustituye X=-3 en la ecuación.", "respuesta": "-5.5"},
            {"pregunta": "Calcula el valor de Y cuando X=-2", "pista": "Sustituye X=-2 en la ecuación.", "respuesta": "7"},
            {"pregunta": "Calcula el valor de Y cuando X=-1", "pista": "Sustituye X=-1 en la ecuación.", "respuesta": "7.5"},
            {"pregunta": "Calcula el valor de Y cuando X=0", "pista": "Sustituye X=0 en la ecuación.", "respuesta": "2"},
            {"pregunta": "Calcula el valor de Y cuando X=1", "pista": "Sustituye X=1 en la ecuación.", "respuesta": "-3.5"},
            {"pregunta": "Calcula el valor de Y cuando X=2", "pista": "Sustituye X=2 en la ecuación.", "respuesta": "-3"},
            {"pregunta": "Calcula el valor de Y cuando X=3", "pista": "Sustituye X=3 en la ecuación.", "respuesta": "9.5"},
            {"pregunta": "¿Cuántas raices tiene la función?", "pista": "Observa los cambios de signo en Y", "respuesta": "3"}
        ],
        "respuesta_final": "3"
    },
    {
        "id": 8,
        "metodo": "Bisectriz",
        "problema": "En la gráfica de la función y = x\u00B3 - 6.5x + 2.",
        "valores": "Iteraciones de búsqueda usando x = (a+b)/2",
        "procedimiento": [
            "a=0, b=1, X=0.5",
            "a=0, b=0.5, X=0.25 (comportamiento +)",
            "a=0.25, b=0.5, X=0.375",
            "a=0.25, b=0.375, X=0.3125 (comportamiento -)",
            "a=0.25, b=0.3175, X=0.28375 (comportamiento +)",
            "a=0.3, b=0.3175, X=0.3087 (comportamiento +)",
            "\u03B5 = |xi+1 - xi| = 0.001"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X en la primera iteración (a=0, b=1)", "pista": "Sustituye los valores en la fórmula de x", "respuesta": "0.5"},
            {"pregunta": "Calcula X en la iteración 2", "pista": "Nuevo intervalo a=0, b=0.5", "respuesta": "0.25"},
            {"pregunta": "Calcula X en la iteración 3", "pista": "Nuevo intervalo a=0.25, b=0.5", "respuesta": "0.375"},
            {"pregunta": "Calcula X en la iteración 4", "pista": "Nuevo intervalo a=0.25, b=0.375", "respuesta": "0.3125"},
            {"pregunta": "Calcula X en la iteración 5", "pista": "Nuevo intervalo a=0.25, b=0.3175", "respuesta": "0.28375"},
            {"pregunta": "Calcula la X final", "pista": "La que cumple \u03B5=0.001", "respuesta": "0.3087"}
        ],
        "respuesta_final": "0.3087" 
    },
    {
        "id": 9,
        "metodo": "Punto Fijo ó Sustituciones Sucesivas",
        "problema": "Localizar la raíz de y = 2x - e^x + 2",
        "valores": "Valor inicial X0 = 0",
        "procedimiento": [
            "Empezar con un valor inicial X0 = 0",
            "Despejar 'x': x = (e^x - 2) / 2",
            "i=0, Xi=0",
            "i=1, (e^0 - 2)/2 = -0.5, \u03B5 = |-0.5 - 0| = 0.5",
            "i=2, (e^-0.5 - 2)/2 = -0.69673467, \u03B5 = 0.19673467",
            "... (Iteraciones continúan de la misma forma hasta i=9)",
            "i=9, (e^-0.768027404 - 2)/2 = -0.768036346, \u03B5 = 0.000008941",
            "El margen de error se encuentra en: \u03B5 = |x9 - x8|",
            "\u03B5 = |-0.768036346 - (-0.768036346)| = 0.000008941"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X1", "pista": "Sustituye X0 en la ecuación despejada.", "respuesta": "-0.5"},
            {"pregunta": "Calcula X2", "pista": "Sustituye X1 en la ecuación despejada.", "respuesta": "-0.69673467"},
            {"pregunta": "Calcula la X final convergente", "pista": "Calcula hasta i=9", "respuesta": "-0.768036346"},
            {"pregunta": "Calcula el error correspondiente a la última iteración", "pista": "Calcula \u03B5 = |x9 - x8| con los últimos valores del procedimiento.", "respuesta": "0.000008941"}
        ],
        "respuesta_final": "0.000008941"
    },
    {
        "id": 10,
        "metodo": "Newton - Raphson",
        "problema": "Encuentre la raíz real de la ecuación f(x) = 0.8x\u00B2 + x - 3",
        "valores": "i=0, xo = 1",
        "formula": [
            "             f(xi)",
            "xi+1 = xi - \u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "            f'(xi)",
            "\u03B5 = |xi+1 - xi|"
        ],
        "procedimiento": [
            "f'(x) = 1.6x + 1",
            "i=0, xo = 1",
            "i=1, x1 = 1 - ( (0.8(1)\u00B2 + (1) - 3) / (1.6(1) + 1) ) = 1.461538462 | \u03B5 = |1.461538462 - 1| = 0.461538462",
            "i=2, x2 = 1.461538462 - ( (0.8(1.461538462)\u00B2 + (1.461538462) - 3) / (1.6(1.461538462) + 1) ) = 1.410492733 | \u03B5 = |1.410492733 - 1.461538462| = 0.051045728",
            "i=3, x3 = 1.410492733 - ( (0.8(1.410492733)\u00B2 + (1.410492733) - 3) / (1.6(1.410492733) + 1) ) = 1.409852675 | \u03B5 = |1.409852675 - 1.410492733| = 0.000640057",
            "i=4, x4 = 1.409852675 - ( (0.8(1.409852675)\u00B2 + (1.409852675) - 3) / (1.6(1.409852675) + 1) ) = 1.409852575 | \u03B5 = |1.409852575 - 1.409852675| = 0.0000001"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X1", "pista": "Sustituye el valor inicial xo = 1 en la fórmula. Evalúa f(1) y f'(1). El error aproximado es de 0.461538462.", "respuesta": "1.461538462"},
            {"pregunta": "Calcula X2", "pista": "Usa x1 para iterar y calcula la diferencia absoluta para verificar el error. El error aproximado es de 0.051045728.", "respuesta": "1.410492733"},
            {"pregunta": "Calcula X3", "pista": "Sigue el proceso con x2. El error aproximado es de 0.00064.", "respuesta": "1.409852675"},
            {"pregunta": "Calcula la raíz final (X4)", "pista": "Realiza la última iteración con x3. El error absoluto final es de 0.0000001.", "respuesta": "1.409852575"}
        ],
        "respuesta_final": "1.409852575"
    },
    {
        "id": 11,
        "metodo": "Falsa Posición ó Regula - Falsi",
        "problema": "Calcule la raíz para f(x) = xe^x - 10",
        "valores": "a=1, b=2",
        "formula": [
            "            f(a) * (b - a)",
            "x = a - \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "            f(b) - f(a)",
            "\u03B5 = |xi+1 - xi|"
        ],
        "procedimiento": [
            "a=1, f(a)=-7.281718172",
            "b=2, f(b)=4.778112190",
            "i=0, b=2, f(b)=4.778112190, a=1, X=1.603799386, f(a)=-7.281718172",
            "i=1, b=2, f(b)=4.778112190, a=1.603799386, X=1.721776248, f(a)=-2.026091162, \u03B5 = 0.117976862",
            "i=2, b=2, f(b)=4.778112190, a=1.721776248, X=1.741651888, f(a)=-0.367597181, \u03B5 = 0.01987564",
            "i=3, b=2, f(b)=4.778112190, a=1.741651888, X=1.744898309, f(a)=-0.060806187, \u03B5 = 0.003246421",
            "i=4, b=2, f(b)=4.778112190, a=1.744898309, X=1.745425782, f(a)=-0.009900159, \u03B5 = 0.000527473",
            "\u03B5 = |xi5 - xi4| = |1.745425782 - 1.744898309|",
            "\u03B5 = 0.000527473"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula f(a) para a=1", "pista": "Evalúa a = 1 en la función ", "respuesta": "-7.281718172"},
            {"pregunta": "Calcula f(b) para b=2", "pista": "Evalúa b = 2 en la función ", "respuesta": "4.778112190"},
            {"pregunta": "Calcula la aproximación X (i=0)", "pista": "Sustituye a = 1, b = 2, f(a) y f(b) en la fórmula de Regula-Falsi.", "respuesta": "1.603799386"},
            {"pregunta": "Calcula la aproximación X (i=1)", "pista": "Como f(1.603799) es negativo, actualiza el límite inferior: a = 1.603799386. Mantén b = 2 y vuelve a aplicar la fórmula.", "respuesta": "1.721776248"},
            {"pregunta": "Calcula la aproximación X (i=2)", "pista": "El nuevo valor de f(a) sigue siendo negativo. Actualiza a = 1.721776248 y mantén b = 2.", "respuesta": "1.741651888"},
            {"pregunta": "Calcula la aproximación X (i=3)", "pista": "Actualiza a = 1.741651888 con b = 2. El error aproximado absoluto ya bajó a 0.0032.", "respuesta": "1.744898309"},
            {"pregunta": "Calcula la raíz final aproximada", "pista": "Sustituye a = 1.744898309 y b = 2. Alcanzarás el error absoluto final de 0.000527473.", "respuesta": "1.745425782"}
        ],
        "respuesta_final": "1.745425782"
    },
    {
        "id": 12,
        "metodo": "Secante",
        "problema": "Calcule la raíz de f(x) = e^(-x) - x.",
        "valores": "x0 = 0, x1 = 1",
        "formula": [
            "               f(xi) * (xi - xi-1)",
            "xi+1 = xi - \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "               f(xi) - f(xi-1)",
            "\u03B5 = |xi+1 - xi|"
        ],
        "procedimiento": [
            "x0 = 0, f(x0) = e^(-0) - 0 = 1",
            "x1 = 1, f(x1) = e^(-1) - 1 = -0.632120558",
            "i=2, x2 = x1 - (f(x1)(x1 - x0)) / (f(x1) - f(x0)) = 1 - {(-0.632120558(1 - 0)) / (-0.632120558 - 1)} = 0.612699836, \u03B5 = |0.612699836 - 1| = 0.387300613",
            "i=3, x3 = x2 - (f(x2)(x2 - x1)) / (f(x2) - f(x1)) = 0.612699836 - {(-0.070813947(0.612699836 - 1)) / (-0.070813947 - (-0.632120558))} = 0.563838389, \u03B5 = |0.563838389 - 0.612699836| = 0.048861447",
            "i=4, x4 = 0.563838423 - {(-0.00004241924099(0.563838389 - 0.612699836)) / (0.005182354419 - (-0.070813946))} = 0.567170358, \u03B5 = |0.567170358 - 0.563838389| = 0.003331969259",
            "i=5, X5 = x4 - (f(x4)(x4 - x3)) / (f(x4) - f(x3)) = 0.567170358 - {(-0.00004241924099(0.567170358 - 0.563838389)) / (-0.00004241924099 - 0.005182354419)} = 0.567143306, \u03B5 = |0.567143306 - 0.567170358| = 0.00002705181386"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula f(x0)", "pista": "Evalúa el primer punto inicial x0 = 0 en f(x) = e^(-x) - x.", "respuesta": "1"},
            {"pregunta": "Calcula f(x1)", "pista": "Evalúa el segundo punto inicial x1 = 1 en f(x) = e^(-x) - x.", "respuesta": "-0.632120558"},
            {"pregunta": "Calcula X2", "pista": "Aplica la fórmula de la secante usando x0 = 0, x1 = 1 y sus respectivas evaluaciones f(x0) y f(x1).", "respuesta": "0.612699836"},
            {"pregunta": "Calcula X3", "pista": "Utiliza los dos valores anteriores: x1 = 1 con f(x1) = -0.632120558, y x2 = 0.6126998 con f(x2) = -0.070813947.", "respuesta": "0.563838389"},
            {"pregunta": "Calcula X4", "pista": "Utiliza x2 = 0.6126998 y x3 = 0.5638383, con sus respectivas evaluaciones en la función.", "respuesta": "0.567170358"},
            {"pregunta": "Calcula la raíz final (X5)", "pista": "Sustituye x3 y x4 en la fórmula. El error absoluto final descenderá hasta 0.000027, logrando la convergencia por debajo de la tolerancia de 0.001.", "respuesta": "0.567143306"}
        ],
        "respuesta_final": "0.567143306"
    },
    {
        "id": 13,
        "metodo": "Montante",
        "problema": "Resolver:\n2a + 5b - 2c = 1\n-a + 2b + 3c = 2\n3a - 3b + 2c = 3",
        "valores": "Matriz inicial 3x4",
        "procedimiento": [
            "Matriz Inicial: [2 5 -2 1], [-1 2 3 2], [3 -3 2 3]",
            "Iteración Pivote = 1 (Elemento 2, Posición 1,1):",
            "Matriz: [2 5 -2 1], [0 9 4 5], [0 -21 10 3]",
            "Iteración Pivote = 2 (Elemento 9, Posición 2,2):",
            "Matriz: [18 0 -38 -16], [0 9 4 5], [0 0 87 66]",
            "Iteración Pivote = 9 (Elemento 87, Posición 3,3):",
            "Matriz: [87 0 0 62], [0 87 0 19], [0 0 87 66]"
        ],
        "pasos_juego": [
            {"pregunta": "Ingresa el valor del pivote 1 (inicial)", "pista": "Elemento 1,1 de la matriz inicial.", "respuesta": "2"},
            {"pregunta": "Ingresa el valor del pivote 2 (segunda iteración)", "pista": "Elemento 2,2 después del primer paso.", "respuesta": "9"},
            {"pregunta": "Ingresa el valor del pivote 3 (tercera iteración)", "pista": "Elemento 3,3 después del segundo paso.", "respuesta": "87"},
            {"pregunta": "Ingresa el valor final de a", "pista": "Divide el término de a por el pivote.", "respuesta": "62/87"},
            {"pregunta": "Ingresa el valor final de b", "pista": "Divide el término de b por el pivote.", "respuesta": "19/87"},
            {"pregunta": "Ingresa el valor final de c", "pista": "Divide el término de c por el pivote.", "respuesta": "66/87"}
        ],
        "respuesta_final": "a = 62/87, b = 19/87, c = 66/87"
    },
    {
        "id": 14,
        "metodo": "Gauss - Jordán",
        "problema": "Resolver:\n3a - 2b + 2c = 1\n4a + 2b + 2c = 2\n3a - 3b + 3c = 3",
        "valores": "Matriz inicial 3x4",
        "procedimiento": [
            "Matriz Inicial: [3 -2 2 | 1], [4 2 2 | 2], [3 -3 3 | 3]",
            "Pivote = 3:",
            "[1 -2/3 2/3 | 1/3], [0 14/3 -2/3 | 2/3], [0 -1 1 | 2]",
            "Pivote = 14/3:",
            "[1 0 4/7 | 3/7], [0 1 -1/7 | 1/7], [0 0 6/7 | 15/7]",
            "Pivote = 6/7:",
            "[1 0 0 | -1], [0 1 0 | 1/2], [0 0 1 | 5/2]"
        ],
        "pasos_juego": [
            {"pregunta": "Valor del primer pivote (Fila 1)", "pista": "Elemento inicial en 1,1.", "respuesta": "3"},
            {"pregunta": "Valor del segundo pivote (Fila 2)", "pista": "Después de reducir la fila 1.", "respuesta": "14/3"},
            {"pregunta": "Valor del tercer pivote (Fila 3)", "pista": "Después de reducir la fila 2.", "respuesta": "6/7"},
            {"pregunta": "Ingresa el valor de a", "pista": "Solución de a.", "respuesta": "-1"},
            {"pregunta": "Ingresa el valor de b", "pista": "Solución de b.", "respuesta": "1/2"},
            {"pregunta": "Ingresa el valor de c", "pista": "Solución de c.", "respuesta": "5/2"}
        ],
        "respuesta_final": "a = -1, b = 1/2, c = 5/2"
    },
    {
        "id": 15,
        "metodo": "Eliminación Gaussiana",
        "problema": "Resolver:\n2x1 + x2 - 3x3 = -1\n-x1 + 3x2 + 2x3 = 12\n3x1 + x2 - 3x3 = 0",
        "valores": "Matriz inicial 3x4",
        "procedimiento": [
            "Procedimiento (matrices sucesivas):",
            "[2 1 -3 -1], [-1 3 2 12], [3 1 -3 0] =>",
            "[2 1 -3 -1], [0 7/2 1/2 23/2], [0 -1/2 3/2 3/2] =>",
            "[2 1 -3 -1], [0 7/2 1/2 23/2], [0 0 11/7 22/7]",
            "Sustitución Hacia Atrás:",
            "11/7 x3 = 22/7 => x3 = (22/7)/(11/7) => x3 = 2",
            "7/2 x2 + 1/2 x3 = 23/2 => x2 = (23/2 - 1/2(2)) / (7/2) => x2 = 3",
            "2x1 + x2 - 3x3 = -1 => 2x1 = -1 - x2 + 3x3 => x1 = (-1 - 3 + 3(2)) / 2 => x1 = 1"
        ],
        "pasos_juego": [
            {"pregunta": "Pivote fila 2 (reducido)", "pista": "Término en 2,2 en la matriz reducida.", "respuesta": "7/2"},
            {"pregunta": "Pivote fila 3 (reducido)", "pista": "Término en 3,3 en la matriz reducida.", "respuesta": "11/7"},
            {"pregunta": "Calcula el valor de x3", "pista": "Sustitución hacia atrás.", "respuesta": "2"},
            {"pregunta": "Calcula el valor de x2", "pista": "Sustitución hacia atrás.", "respuesta": "3"},
            {"pregunta": "Calcula el valor de x1", "pista": "Sustitución hacia atrás.", "respuesta": "1"}
        ],
        "respuesta_final": "x1 = 1, x2 = 3, x3 = 2"
    },
    {
        "id": 16,
        "metodo": "Gauss - Seidel",
        "problema": "Resolver:\nx - 3y + 5z = 5\n8x - y - z = 8\n-2x + 4y + z = 4",
        "valores": "x0 = y0 = z0 = 0\nBuscando un error de 0.001 en las tres variables",
        "procedimiento": [
            "Despejando las variables para la Diagonal Dominante:",
            "x = (8+y+z)/8, y = (4+2x-z)/4, z = (5-x+3y)/5",
            "1era. Iteración: Con y0 = 0 y z0 = 0:",
            "x1 = (8+0+0)/8 = 1",
            "y1 = (4+2(1)-0)/4 = 1.5",
            "z1 = (5-1+3(1.5))/5 = 1.7",
            "2da. Iteración: Con y1 = 1.5 y z1 = 1.7:",
            "x2 = (8+1.5+1.7)/8 = 1.4",
            "y2 = (4+2(1.4)-1.7)/4 = 1.275",
            "z2 = (5-1.4+3(1.275))/5 = 1.485",
            "3era. Iteración: Con y2 = 1.275 y z2 = 1.485:",
            "x3 = (8+1.275+1.485)/8 = 1.345",
            "y3 = (4+2(1.345)-1.485)/4 = 1.30125",
            "z3 = (5-1.345+3(1.30125))/5 = 1.51175",
            "4ta. Iteración: Con y3 = 1.30125 y z3 = 1.51175:",
            "x4 = (8+1.30125+1.51175)/8 = 1.351625",
            "y4 = (4+2(1.351625)-1.51175)/4 = 1.297875",
            "z4 = (5-1.351625+3(1.297875))/5 = 1.5084",
            "5ta. Iteración: Con y4 = 1.297875 y z4 = 1.5084:",
            "x5 = (8+1.297875+1.5084)/8 = 1.350784375",
            "y5 = (4+2(1.350784375)-1.5084)/4 = 1.298292188",
            "z5 = (5-1.350784375+3(1.298292188))/5 = 1.508818438",
            "Errores absolutos en la 5ta. iteración:",
            "\u03B5x = |1.350784375 - 1.351625| = 0.000840625 < 0.001",
            "\u03B5y = |1.298292188 - 1.297875| = 0.000417188 < 0.001",
            "\u03B5z = |1.508818438 - 1.5084| = 0.000418438 < 0.001",
            "Como todos los errores son menores a 0.001, el método converge."
        ],
        "pasos_juego": [
            {"pregunta": "Calcula x1 en la primera iteración", "pista": "Despeja x de la segunda ecuación y sustituye los valores iniciales y0=0, z0=0.", "respuesta": "1"},
            {"pregunta": "Calcula y1 en la primera iteración", "pista": "Despeja y de la tercera ecuación. Recuerda usar el valor de x1 recién calculado (x1 = 1) y z0=0.", "respuesta": "1.5"},
            {"pregunta": "Calcula z1 en la primera iteración", "pista": "Despeja z de la primera ecuación. Recuerda usar los valores más recientes calculados (x1 = 1, y1 = 1.5).", "respuesta": "1.7"},
            {"pregunta": "¿A cuántas iteraciones se llegó a los margenes de error deseados?", "pista": "Revisa el desglose de las iteraciones en el procedimiento. ¿En qué iteración todos los errores absolutos (\u03B5x, \u03B5y, \u03B5z) son menores a 0.001?", "respuesta": "5"},
            {"pregunta": "Calcula el valor final de x (x5)", "pista": "Obtenido en la iteración 5 usando y4 = 1.297875 y z4 = 1.5084.", "respuesta": "1.350784375"},
            {"pregunta": "Calcula el valor final de y (y5)", "pista": "Obtenido en la iteración 5 usando el valor recién calculado de x5 = 1.350784375 y z4 = 1.5084.", "respuesta": "1.298292188"},
            {"pregunta": "Calcula el valor final de z (z5)", "pista": "Obtenido en la iteración 5 usando los valores más recientes x5 = 1.350784375 y y5 = 1.298292188.", "respuesta": "1.508818438"},
            {"pregunta": "Calcula el error absoluto final en x (\u03B5x)", "pista": "Aplica \u03B5x = |x5 - x4|, donde x4 = 1.351625 y x5 = 1.350784375.", "respuesta": "0.000840625"},
            {"pregunta": "Calcula el error absoluto final en y (\u03B5y)", "pista": "Aplica \u03B5y = |y5 - y4|, donde y4 = 1.297875 y y5 = 1.298292188.", "respuesta": "0.000417188"},
            {"pregunta": "Calcula el error absoluto final en z (\u03B5z)", "pista": "Aplica \u03B5z = |z5 - z4|, donde z4 = 1.5084 y z5 = 1.508818438.", "respuesta": "0.000418438"}
        ],
        "respuesta_final": "x5 = 1.350784375, y5 = 1.298292188, z5 = 1.508818438"
    },
    {
        "id": 17,
        "metodo": "Jacobi",
        "problema": "Resolver:\nx - 3y + 5z = 5\n8x - y - z = 8\n-2x + 4y + z = 4",
        "valores": "x0 = y0 = z0 = 1\nBuscando un error de 0.001 en las tres variables",
        "procedimiento": [
            "Despejando las variables para la Diagonal Dominante:",
            "x = (8+y+z)/8, y = (4+2x-z)/4, z = (5-x+3y)/5",
            "1era. Iteración: Con y0 = 1 y z0 = 1:",
            "x1 = (8+1+1)/8 = 1.25",
            "y1 = (4+2(1)-1)/4 = 1.25",
            "z1 = (5-1+3(1))/5 = 1.4",
            "2da. Iteración: Con y1 = 1.25 y z1 = 1.4:",
            "x2 = (8+1.25+1.4)/8 = 1.33125",
            "y2 = (4+2(1.25)-1.4)/4 = 1.275",
            "z2 = (5-1.25+3(1.25))/5 = 1.5",
            "3era. Iteración: Con y2 = 1.275 y z2 = 1.5:",
            "x3 = (8+1.275+1.5)/8 = 1.346875",
            "y3 = (4+2(1.33125)-1.5)/4 = 1.290625",
            "z3 = (5-1.33125+3(1.275))/5 = 1.49875",
            "4ta. Iteración: Con y3 = 1.290625 y z3 = 1.49875:",
            "x4 = (8+1.290625+1.49875)/8 = 1.348671875",
            "y4 = (4+2(1.346875)-1.49875)/4 = 1.29875",
            "z4 = (5-1.346875+3(1.290625))/5 = 1.505",
            "5ta. Iteración: Con y4 = 1.29875 y z4 = 1.505:",
            "x5 = (8+1.29875+1.505)/8 = 1.35046875",
            "y5 = (4+2(1.348671875)-1.505)/4 = 1.298085938",
            "z5 = (5-1.348671875+3(1.29875))/5 = 1.509515625",
            "6ta. Iteración: Con y5 = 1.298085938 y z5 = 1.509515625:",
            "x6 = (8+1.298085938+1.509515625)/8 = 1.350950195",
            "y6 = (4+2(1.35046875)-1.509515625)/4 = 1.297855469",
            "z6 = (5-1.35046875+3(1.298085938))/5 = 1.508757813",
            "Errores absolutos en la 6ta. iteración:",
            "\u03B5x = |1.350950195 - 1.35046875| = 0.000481445 < 0.001",
            "\u03B5y = |1.297855469 - 1.298085938| = 0.000230468 < 0.001",
            "\u03B5z = |1.508757813 - 1.509515625| = 0.000757812 < 0.001",
            "Como todos los errores son menores a 0.001, el método converge."
        ],
        "pasos_juego": [
            {"pregunta": "Calcula x1 en la primera iteración", "pista": "Despeja x de la segunda ecuación utilizando los valores iniciales y0=1, z0=1.", "respuesta": "1.25"},
            {"pregunta": "Calcula y1 en la primera iteración", "pista": "Despeja y de la tercera ecuación. Recuerda usar únicamente los valores de la iteración anterior, x0=1 y z0=1.", "respuesta": "1.25"},
            {"pregunta": "Calcula z1 en la primera iteración", "pista": "Despeja z de la primera ecuación utilizando los valores iniciales, x0=1 y y0=1.", "respuesta": "1.4"},
            {"pregunta": "¿A cuántas iteraciones se llegó a los margenes de error deseados?", "pista": "Revisa el desglose de las iteraciones en el procedimiento. ¿En qué iteración todos los errores absolutos (\u03B5x, \u03B5y, \u03B5z) son menores a 0.001?", "respuesta": "6"},
            {"pregunta": "Calcula el valor final de x (x6)", "pista": "Obtenido en la iteración 6 usando y5 = 1.298085938 y z5 = 1.509515625.", "respuesta": "1.350950195"},
            {"pregunta": "Calcula el valor final de y (y6)", "pista": "Obtenido en la iteración 6 usando los valores de la iteración anterior, x5 = 1.35046875 y z5 = 1.509515625.", "respuesta": "1.297855469"},
            {"pregunta": "Calcula el valor final de z (z6)", "pista": "Obtenido en la iteración 6 usando los valores de la iteración anterior, x5 = 1.35046875 y y5 = 1.298085938.", "respuesta": "1.508757813"},
            {"pregunta": "Calcula el error absoluto final en x (\u03B5x)", "pista": "Aplica \u03B5x = |x6 - x5|, donde x5 = 1.35046875 y x6 = 1.350950195.", "respuesta": "0.000481445"},
            {"pregunta": "Calcula el error absoluto final en y (\u03B5y)", "pista": "Aplica \u03B5y = |y6 - y5|, donde y5 = 1.298085938 y y6 = 1.297855469.", "respuesta": "0.000230468"},
            {"pregunta": "Calcula el error absoluto final en z (\u03B5z)", "pista": "Aplica \u03B5z = |z6 - z5|, donde z5 = 1.509515625 y z6 = 1.508757813.", "respuesta": "0.000757812"}
        ],
        "respuesta_final": "x6 = 1.350950195, y6 = 1.297855469, z6 = 1.508757813"
    },
    {
        "id": 18,
        "metodo": "Mínimos Cuadrados (Línea Recta)",
        "problema": "Ajustar los datos a una línea recta g(x) = a0 + a1x",
        "valores": "x:  1.1  |  1.9  |  2.4  |  4.8  |  5.1  |  10.5\ny:  2.5  |  2.7  |  3.7  |  5.2  |  6.0  |   8.3",
        "formula": [
            "  a0       a1 x      g(x)",
            "\u250C                       \u2510",
            "\u2502  n       \u03A3x  \u2502  \u03A3y  \u2502",
            "\u2502  \u03A3x     \u03A3x\u00B2  \u2502 \u03A3xy  \u2502",
            "\u2514                       \u2518"
        ],
        "procedimiento": [
            "Ecuaciones Normales:",
            "1) 6 a0 + 25.8 a1 = 28.4",
            "2) 25.8 a0 + 169.88 a1 = 159.47",
            "Multiplicar la ec. 1 por -4.3 para eliminar a0:",
            "3) -25.8 a0 - 110.94 a1 = -122.12",
            "Sumar ecuaciones 2 y 3:",
            "0 a0 + 58.94 a1 = 37.35 => a1 = 37.35 / 58.94 = 0.633695283",
            "Sustituir a1 en ec. 1 para hallar a0:",
            "6 a0 + 25.8(0.633695283) = 28.4 => a0 = 2.008443615",
            "Encontrar g(x) con los valores de a0 y a1:",
            "g(x) = 2.008443615 + 0.633695283 x",
            "g(1.1) = 2.705508427 | g(1.9) = 3.212464653 | g(2.4) = 3.529312295",
            "g(4.8) = 5.050180975 | g(5.1) = 5.240289560 | g(10.5) = 8.662244090",
            "Por último se gráfica en el mismo plano con las siguientes coordenadas:",
            "1) [x, y]  y  2) [x, g(x)]",
            "Para analizar el ajuste de la función original con respecto a la de Línea Recta."
        ],
        "pasos_juego": [
            {"pregunta": "Calcula la sumatoria de x (\u03A3x)", "pista": "Suma todos los valores de x de la tabla: (1.1 + 1.9 + 2.4 + 4.8 + 5.1 + 10.5).", "respuesta": "25.8"},
            {"pregunta": "Calcula la sumatoria de y (\u03A3y)", "pista": "Suma todos los valores de y de la tabla: (2.5 + 2.7 + 3.7 + 5.2 + 6.0 + 8.3).", "respuesta": "28.4"},
            {"pregunta": "Calcula la sumatoria de x\u00B2 (\u03A3x\u00B2)", "pista": "Eleva cada valor de x al cuadrado y súmalos: (1.1\u00B2 + 1.9\u00B2 + 2.4\u00B2 + 4.8\u00B2 + 5.1\u00B2 + 10.5\u00B2).", "respuesta": "169.88"},
            {"pregunta": "Calcula la sumatoria de xy (\u03A3xy)", "pista": "Multiplica cada par x*y y suma los resultados: (1.1*2.5 + 1.9*2.7 + 2.4*3.7 + 4.8*5.2 + 5.1*6.0 + 10.5*8.3).", "respuesta": "159.47"},
            {"pregunta": "Calcula el valor de a1", "pista": "Resuelve el sistema. Multiplicando Ec 1 por -4.3, sumas ambas y despejas a1: a1 = 37.35 / 58.94.", "respuesta": "0.633695283"},
            {"pregunta": "Calcula el valor de a0", "pista": "Sustituye a1 en la Ecuación 1: a0 = (28.4 - 25.8 * a1) / 6.", "respuesta": "2.008443615"},
            {"pregunta": "Calcula el valor ajustado de g(10.5)", "pista": "Aplica la función g(x) con x = 10.5.", "respuesta": "8.662244090"}
        ],
        "respuesta_final": "8.662244090"
    },
    {
        "id": 19,
        "metodo": "Regla Trapezoidal",
        "problema": "  3      1\n  \u222B \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 dx\n  2   1 + x\u00B2\ncon n = 4",
        "valores": "a = 2, b = 3, n = 4",
        "formula": [
            "        b - a",
            "  h = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500",
            "          n",
            "",
            "      h   \u250C          n-1                  \u2510",
            "  I = \u2500\u2500\u2500 \u2502 f(a) + 2  \u03A3  f(a + ih) + f(b) \u2502",
            "      2   \u2514          i=1                  \u2518"
        ],
        "procedimiento": [
            "h = (b-a)/n = (3-2)/4 = 1/4 = 0.25",
            "I = (0.25 / 2) * { f(2) + 2[f(9/4) + f(5/2) + f(11/4)] + f(3) }",
            "I = 0.125 * { 1/(1+2\u00B2) + 2[1/(1+(9/4)\u00B2) + 1/(1+(5/2)\u00B2) + 1/(1+(11/4)\u00B2)] + 1/(1+3\u00B2) }",
            "I = 0.125 * (0.2 + 2[0.164948453 + 0.137931034 + 0.116788321] + 0.1)",
            "I = 0.125 * (1.139335619)",
            "I = 0.142416952"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de h", "pista": "Toma en cuenta los valores iniciales en la fórmula de h.", "respuesta": "0.25"},
            {"pregunta": "Calcula la sumatoria interna de los corchetes", "pista": "Evalua los valores obtenidos en la fórmula de I sin multiplicarlo por h/2", "respuesta": "1.139335619"},
            {"pregunta": "Calcula el resultado I final", "pista": "Multiplica la sumatoria obtenida por el factor h/2.", "respuesta": "0.142416952"}
        ],
        "respuesta_final": "0.142416952"
    },
    {
        "id": 20,
        "metodo": "Newton - Cotes (Abiertas)",
        "problema": "  2\n  \u222B (3x\u00B3 - 10) dx\n -2\ncon n = 4",
        "valores": "a = -2, b = 2, n = 4",
        "formula": [
            "          n+2                   b - a",
            "  I = \u03B1 h  \u03A3  w\u1D62 f(a + ih)  ; h = \u2500\u2500\u2500\u2500\u2500",
            "         i=0                    n + 2"
        ],
        "procedimiento": [
            "h = (b-a)/(n+2) = (2 - (-2))/(4+2) = 2/3",
            "\u03B1 = 6/20",
            "I = [6/20][2/3] * { [(0)f(x=-2)] + [(11)f(x=-4/3)] + [(-14)f(x=-2/3)] + [(26)f(x=0)] + [(-14)f(x=2/3)] + [(11)f(x=4/3)] + [(0)f(x=2)] }",
            "I = [1/5] * { (-1694/9) + (1372/9) + 260 + (1148/9) - (289/9) }",
            "I = [1/5][-200]",
            "I = -40"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de h", "pista": "Toma en cuenta los valores iniciales en la fórmula de h.", "respuesta": "2/3"},
            {"pregunta": "Calcula el valor de alfa (\u03B1)", "pista": "Revisa el valor de \u03B1 definido al inicio de la sección de procedimiento.", "respuesta": "6/20"},
            {"pregunta": "Calcula el valor de I", "pista": "Multiplica el factor global \u03B1 * h por el resultado de la sumatoria interna del procedimiento.", "respuesta": "-40"}
        ],
        "respuesta_final": "-40"
    },
    {
        "id": 21,
        "metodo": "Regla de 1/3 Simpson",
        "problema": "  3      1\n  \u222B \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 dx\n  2   1 + x\u00B2\ncon n = 10",
        "valores": "a = 2, b = 3, n = 10",
        "formula": [
            "        h   \u250C             n-1          n-2          \u2510",
            "  I = \u2500\u2500\u2500 \u2502 f(a) + 4  \u03A3  f(x\u1D62) + 2  \u03A3  f(x\u2C7C) + f(b) \u2502",
            "        3   \u2514            i=1,impar    j=2,par       \u2518",
            "  donde h = (b - a) / n (n es siempre par)"
        ],
        "procedimiento": [
            "h = (b-a)/n = (3-2)/10 = 1/10 = 0.1",
            "I = (0.1 / 3) * { f(2) + 4[f(2.1)+f(2.3)+f(2.5)+f(2.7)+f(2.9)] + 2[f(2.2)+f(2.4)+f(2.6)+f(2.8)] + f(3) }",
            "I = 1/30 * (0.2 + 400/541 + 25/73 + 400/629 + 50/169 + 16/29 + 25/97 + 400/829 + 50/221 + 400/941 + 0.1)",
            "I = 1/30 * (4.256914514)",
            "I = 0.14189715"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de h", "pista": "Toma en cuenta los valores iniciales en la sustitución de la fórmula.", "respuesta": "0.1"},
            {"pregunta": "Calcula la sumatoria interna de los corchetes", "pista": "Evalúa f(x) en los puntos de la partición aplicando los coeficientes correspondientes de Simpson 1/3.", "respuesta": "4.256914514"},
            {"pregunta": "Calcula el resultado I final", "pista": "Multiplica la sumatoria obtenida por el factor h/3.", "respuesta": "0.14189715"}
        ],
        "respuesta_final": "0.14189715"
    },
    {
        "id": 22,
        "metodo": "Regla de 3/8 Simpson",
        "problema": "  1\n  \u222B x\u00B3e^x dx\n  0\ncon n = 3",
        "valores": "a = 0, b = 1, n = 3",
        "formula": [
            "       3   \u250C             n-1          \u2510       b - a",
            "  I = \u2500\u2500\u2500 h\u2502 f(a) + 3  \u03A3  f(x\u1D62) + f(b) \u2502 ;h = \u2500\u2500\u2500\u2500\u2500",
            "       8   \u2514            i=1           \u2518         n"
        ],
        "procedimiento": [
            "h = (b-a)/n = (1-0)/3 = 1/3",
            "I = (3/8)[1/3] * { f(0) + 3[f(1/3) + f(2/3)] + f(1) }",
            "I = [1/8] * { [(0)\u00B3e^0] + 3[(1/3)\u00B3e^(1/3) + (2/3)\u00B3e^(2/3)] + [(1)\u00B3e^1] }",
            "I = [1/8] * (0 + 0.155068047 + 1.731319148 + 2.718281828)",
            "I = [1/8] * [4.604669023]",
            "I = 0.575583627"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el coeficiente multiplicador (3h/8)", "pista": "Toma en cuenta los valores iniciales al sustituir en la fórmula de h", "respuesta": "0.125"},
            {"pregunta": "Calcula la sumatoria interna de los corchetes", "pista": "Resuelve las operaciones matematicas dentro de los corchetes", "respuesta": "4.604669023"},
            {"pregunta": "Calcula el resultado I final", "pista": "Multiplica el coeficiente multiplicador por la sumatoria total de los corchetes", "respuesta": "0.575583627"}
        ],
        "respuesta_final": "0.575583627"
    },
    {
        "id": 23,
        "metodo": "Euler Modificado",
        "problema": "2y' + 3yt + y = 0",
        "valores": "y0 = 1.2, h = 0.3, y1 = 1.2, t0 = 0, t1 = 0.3",
        "formula": [
            "y' = f(t, y)",
            "yn+1 = yn + (h/2) * [f(tn, yn) + f(tn+1, yn+1)]"
        ],
        "procedimiento": [
            "Despejar y': y' = (-3yt - y) / 2",
            "y'1 = y0 + (h/2){ [(-3y0t0 - y0)/2] + [(-3y1t1 - y1)/2] }",
            "y'1 = 1.2 + (0.3/2){ ( (-3(1.2)(0) - (1.2))/2 ) + ( (-3(1.2)(0.3) - (1.2))/2 ) }",
            "y'1 = 1.2 + [0.15][-0.6 - 1.14]",
            "y'1 = 0.939"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula f(y0, t0)", "pista": "Usa la fórmula: f(t, y) = (-3yt - y) / 2,", "respuesta": "-0.6"},
            {"pregunta": "Calcula f(y1, t1)", "pista": "Usa la fórmula: f(t, y) = (-3yt - y) / 2,", "respuesta": "-1.14"},
            {"pregunta": "Calcula y'1 final", "pista": "Usa la fórmula completa: y'1 = y0 + (h / 2) * [f(y0, t0) + f(y1, t1)],", "respuesta": "0.939"}
        ],
        "respuesta_final": "0.939"
    },
    {
        "id": 24,
        "metodo": "Runge - Kutta de 2do orden",
        "problema": "y' - 2ty + 1 = 0",
        "valores": "y0 = 1, h = 0.6, t0 = 0",
        "formula": [
            "k1 = h * f(yn, tn)",
            "k2 = h * f(yn + k1, tn + h)",
            "yn+1 = yn + (1/2) * (k1 + k2)"
        ],
        "procedimiento": [
            "Despejar: y' = 2ty - 1",
            "k1 = 0.6( 2(0)(1) - 1 ) = -0.6",
            "k2 = 0.6{ [2(0 + 0.6)[1 + (-0.6)]] - 1 } = 0.6{ [2(0.6)(0.4)] - 1 }",
            "k2 = 0.303265329",
            "y1 = 1 + 1/2(-1 + 0.30326529)",
            "y1 = 0.651632664"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Usa la fórmula de k1, donde f(t, y) = 2ty - 1", "respuesta": "-0.6"},
            {"pregunta": "Calcula k2", "pista": "Usa la fórmula de k2, donde f(t, y) = 2ty - 1", "respuesta": "0.303265329"},
            {"pregunta": "Calcula y1 final", "pista": "Usa la fórmula: yn+1 = yn + 1/2 * (k1 + k2)", "respuesta": "0.651632664"}
        ],
        "respuesta_final": "0.651632664"
    },
    {
        "id": 25,
        "metodo": "Runge - Kutta de 3er Orden",
        "problema": "      2yt + 1\ny' = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n        y\u00B2   ",
        "valores": "y0 = 1, h = 0.25, t0 = 0",
        "formula": [
            "k1 = h * f(yn, tn)",
            "k2 = h * f(yn + (k1/2), tn + (h/2))",
            "k3 = h * f(yn - k1 + 2*k2, tn + h)",
            "yn+1 = yn + (1/6) * (k1 + 4*k2 + k3)"
        ],
        "procedimiento": [
            "k1 = 0.25( (2(1)(0) + 1) / (1)\u00B2 ) = 0.25",
            "k2 = 0.25{ (2(1 + 0.25/2)(0 + 0.25/2) + 1) / (1 + 0.25/2)\u00B2 } = 0.253086419",
            "k3 = 0.25{ (2[1 - 0.25 + 2(0.253086419)][0 + 0.25] + 1) / [1 - 0.25 + 2(0.253086419)]\u00B2 } = 0.257939981",
            "y1 = 1 + 1/6[0.25 + 4(0.253086419) + 0.257993981]",
            "y1 = 1.211723276"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye y0 = 1, t0 = 0 y h = 0.25 en k1 = h * f(yn, tn), donde f(0, 1) = 1.", "respuesta": "0.25"},
            {"pregunta": "Calcula k2", "pista": "Evalúa f en el punto medio: t = 0.125 e y = 1.125. f(0.125, 1.125) \u2248 1.012346. Multiplica por h.", "respuesta": "0.253086419"},
            {"pregunta": "Calcula k3", "pista": "Evalúa f en t = 0.25 e y \u2248 1.256173 (que es y0 - k1 + 2*k2). Multiplica el resultado por h = 0.25.", "respuesta": "0.257939981"},
            {"pregunta": "Calcula y1 final", "pista": "Sustituye en la fórmula final. Nota: Por un error de cálculo común en este procedimiento, la suma de corchetes dio 1.270339656, resultando en 1.211723276.", "respuesta": "1.211723276"}
        ],
        "respuesta_final": "1.211723276"
    },
    {
        "id": 26,
        "metodo": "Runge - Kutta de 4to. Orden por 1/3 de Simpson",
        "problema": "      (y + t)\u00B2\ny' = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n       1 - y  ",
        "valores": "y0 = 0.4, h = 0.2, t0 = 0",
        "formula": [
            "k1 = h * f(yn, tn)",
            "k2 = h * f(yn + (k1/2), tn + (h/2))",
            "k3 = h * f(yn + (k2/2), tn + (h/2))",
            "k4 = h * f(yn + k3, tn + h)",
            "yn+1 = yn + (1/6) * (k1 + 2*k2 + 2*k3 + k4)"
        ],
        "procedimiento": [
            "k1 = (0.2){ [0.4 + 0]\u00B2 / (1 - 0.4) } = (0.2){ (0.4)\u00B2 / 0.6 } = 0.053333333",
            "k2 = (0.2)[ [0.4 + (0.053333333/2) + (0 + (0.2/2))]\u00B2 / (1 - [0.4 + (0.053333333/2)]) ] = 0.096759689",
            "k3 = (0.2)[ [0.4 + (0.096759689/2) + (0 + (0.2/2))]\u00B2 / (1 - [0.4 + (0.096759689/2)]) ] = 0.109031713",
            "k4 = (0.2){ [0.4 + 0.109031713 + (0 + 0.2)]\u00B2 / (1 - (0.4 + 0.109031713)) } = 0.2047895890",
            "y1 = 0.4 + 1/6(0.053333333 + 2(0.096759688) + 2(0.109031713) + 0.204789589)",
            "y1 = 0.511617621"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye y0 = 0.4, t0 = 0 y h = 0.2 en la fórmula.", "respuesta": "0.053333333"},
            {"pregunta": "Calcula k2", "pista": "Evalúa f en el punto medio: t = 0.1 e y \u2248 0.426667. Multiplica por h.", "respuesta": "0.096759689"},
            {"pregunta": "Calcula k3", "pista": "Evalúa f en el punto medio: t = 0.1 e y \u2248 0.448380. Multiplica por h.", "respuesta": "0.109031713"},
            {"pregunta": "Calcula k4", "pista": "Evalúa f al final del intervalo: t = 0.2 e y \u2248 0.509032. Multiplica por h.", "respuesta": "0.2047895890"},
            {"pregunta": "Calcula y1 final", "pista": "Sustituye en la fórmula final usando los coeficientes de Simpson 1/3.", "respuesta": "0.511617621"}
        ],
        "respuesta_final": "0.511617621"
    },
    {
        "id": 27,
        "metodo": "Runge - Kutta de 4to. Orden por 3/8 de Simpson",
        "problema": "        -y   \ny' = \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n      y\u00B2 + t ",
        "valores": "y0 = 1, h = 0.5, t0 = 0",
        "formula": [
            "k1 = h * f(yn, tn)",
            "k2 = h * f(yn + (k1/3), tn + (h/3))",
            "k3 = h * f(yn + (k1/3) + (k2/3), tn + (2*h/3))",
            "k4 = h * f(yn + k1 - k2 - k3, tn + h)",
            "yn+1 = yn + (1/8) * (k1 + 3*k2 + 3*k3 + k4)"
        ],
        "procedimiento": [
            "k1 = 0.5{ -1 / ((1)\u00B2 + 0) } = -0.5",
            "k2 = 0.5{ (-1 + (-0.5/3)) / ([1 + (-0.5/3)]\u00B2 + [0 + (0.5/3)]) } = -0.483870959",
            "k3 = 0.5{ (-1 + (-0.5/3) + (-0.483870959/3)) / ([1 + (-0.5/3) + (-0.483870959/3)]\u00B2 + [0 + 2/3(0.5)]) } = -0.428066426",
            "k4 = 0.5{ (-1 + (-0.5) - (-0.483870959 + (-0.428066428))) / ([1 + (-0.5) - (-0.483870959) + (-0.428066428)]\u00B2 + (0 + 0.5)) } = -0.343547869",
            "y1 = 1 + 1/8[ -0.5 + 3(-0.483870959) + 3(-0.428066426) + (-0.343547869) ]",
            "y1 = 1 + (-0.447420003) = 0.552579997"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye y0 = 1, t0 = 0 y h = 0.5 en la fórmula.", "respuesta": "-0.5"},
            {"pregunta": "Calcula k2", "pista": "Evalúa f en t = 0.166667 e y = 0.833333. Multiplica por h.", "respuesta": "-0.483870959"},
            {"pregunta": "Calcula k3", "pista": "Evalúa f en t \u2248 0.333333 e y \u2248 0.672043. Multiplica por h = 0.5.", "respuesta": "-0.428066426"},
            {"pregunta": "Calcula k4", "pista": "Evalúa f al final del intervalo: t = 0.5 e y \u2248 1.411937. Multiplica por h.", "respuesta": "-0.343547869"},
            {"pregunta": "Calcula y1 final", "pista": "Sustituye en la fórmula final usando los coeficientes de Simpson 3/8.", "respuesta": "0.552579997"}
        ],
        "respuesta_final": "0.552579997"
    },
    {
        "id": 28,
        "metodo": "Runge - Kutta de Orden Superior",
        "problema": "2y'' - 4y't - 2y = 0",
        "valores": "y0 = 1.1, h = 0.2, y'0 = 1.2, t0 = 0",
        "formula": [
            "k1 = h * Vn",
            "m1 = h * [a * Vn * qn - b * Un]",
            "k2 = h * (Vn + m1)",
            "m2 = h * [a * (Vn + m1) * (qn + h) - b * (Un + k1)]",
            "y1 = Un + (1/2) * (k1 + k2)",
            "y'1 = Vn + (1/2) * (m1 + m2)"
        ],
        "procedimiento": [
            "y'' = 2y't - y",
            "a = 2, b = 1, Vn = y'0 = 1.2, Un = y0 = 1.1, qn = t = 0",
            "k1 = h(Vn) = 0.2(1.2) = 0.24",
            "m1 = 0.2{ [2(1.2)(0)] - 1.1 } = -0.22",
            "k2 = 0.2(1.2 + (-0.22)) = 0.2(1.2 - 0.22) = 0.196",
            "m2 = 0.2{ 2[1.2 + (-0.22)(0 + 0.2)] - (1.1 + 0.24) } = -0.1892",
            "y1 = 1.1 + 1/2(0.24 + 0.196) = 1.318",
            "y'1 = 1.2 + 1/2[(-0.22) + (-0.1896)] = 0.9952"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye h = 0.2 y Vn = 1.2 en la fórmula.", "respuesta": "0.24"},
            {"pregunta": "Calcula m1", "pista": "Sustituye a = 2, b = 1, qn = 0 y Un = 1.1 en la fórmula.", "respuesta": "-0.22"},
            {"pregunta": "Calcula k2", "pista": "Sustituye h = 0.2, Vn = 1.2 y m1 = -0.22 en la fórmula.", "respuesta": "0.196"},
            {"pregunta": "Calcula m2", "pista": "Sustituye a = 2, b = 1, qn = 0, h = 0.2 y Un = 1.1 en la fórmula.", "respuesta": "-0.1892"},
            {"pregunta": "Calcula y1", "pista": "Sustituye en la fórmula usando Un = 1.1.", "respuesta": "1.318"},
            {"pregunta": "Calcula y'1", "pista": "Sustituye en la fórmula usando Vn = 1.2.", "respuesta": "0.9952"}
        ],
        "respuesta_final": "y1 = 1.318, y'1 = 0.9952"
    }
]
