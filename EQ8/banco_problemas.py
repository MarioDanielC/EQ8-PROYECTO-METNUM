# banco_problemas.py
# Este archivo contiene el banco de problemas extraídos exactamente del libro de la maestra.
# Se respeta estrictamente la nomenclatura, símbolos y procedimientos originales.
# Cada problema cuenta ahora con "pasos_juego", un arreglo dinamico con los pasos que mejor representan su metodo.

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
            "E = |1.386294361 - 1.304007668|",
            "E = 0.082286693"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de f(a)", "pista": "Sustituye 'a' en la función Ln.", "respuesta": "0.69314718"},
            {"pregunta": "Calcula el valor de f(b)", "pista": "Sustituye 'b' en la función Ln.", "respuesta": "1.609437912"},
            {"pregunta": "Calcula el valor final de g(x)", "pista": "Usa la fórmula: ((f(b) - f(a)) / (b - a)) * (x - a) + f(a)", "respuesta": "1.304007668"},
            {"pregunta": "Calcula el Error absoluto E", "pista": "E = |f(x) - g(x)|", "respuesta": "0.082286693"}
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
            "E = |1.386294361 - 1.354025101|",
            "E = 0.03226926"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de f(a)", "pista": "Sustituye 'a' en la función Ln.", "respuesta": "1.098612289"},
            {"pregunta": "Calcula el valor de f(b)", "pista": "Sustituye 'b' en la función Ln.", "respuesta": "1.609437912"},
            {"pregunta": "Calcula el valor final de g(x)", "pista": "Usa la fórmula: ((f(b) - f(a)) / (b - a)) * (x - a) + f(a)", "respuesta": "1.354025101"},
            {"pregunta": "Calcula el Error absoluto E", "pista": "E = |f(x) - g(x)|", "respuesta": "0.03226926"}
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
            "Δ'1 = y2 - y1 = 2.82 - 2.54 = 0.28",
            "Δ'2 = y3 - y2 = 3.21 - 2.82 = 0.39",
            "Δ²1 = Δ'2 - Δ'1 = 0.39 - 0.28 = 0.11",
            "s = (x - xi) / h = (2.4 - 2.2) / 0.3 = 0.666666666",
            "g(x) = yi[s_0] + Δ'1[s_1] + Δ²1[ (s(s-1)) / 2! ]",
            "g(x) = 2.54(1) + (0.28)(0.666666666) + (0.11)[ (0.666666666(0.666666666 - 1)) / 2! ]",
            "g(x) = 2.714444444"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula la 1ra diferencia finita \u0394'1", "pista": "Resta y2 - y1", "respuesta": "0.28"},
            {"pregunta": "Calcula la 2da diferencia finita \u0394\u00b21", "pista": "Resta \u0394'2 - \u0394'1", "respuesta": "0.11"},
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
            "∇'2 = y2 - y1 = 2.82 - 2.54 = 0.28",
            "∇'1 = y3 - y2 = 3.21 - 2.82 = 0.39",
            "∇²1 = ∇'2 - ∇'1 = 0.39 - 0.28 = 0.11",
            "s = (x - xi) / h = (2.4 - 2.8) / 0.3 = -1.33333333333",
            "g(x) = yi[s_0] + ∇'f(xi)[s_1] + ∇²f(xi)[ (s(s+1)) / 2! ]",
            "g(x) = 3.21(1) + (0.39)(-1.33333333333) + (0.11)[ (-1.33333333333(-1.33333333333 + 1)) / 2! ]",
            "g(x) = 2.714444444"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula ∇'2", "pista": "Resta y2 - y1", "respuesta": "0.28"},
            {"pregunta": "Calcula ∇'1", "pista": "Resta y3 - y2", "respuesta": "0.39"},
            {"pregunta": "Calcula ∇²1", "pista": "Resta ∇'1 - ∇'2", "respuesta": "0.11"},
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
        "procedimiento": [
            "h1 = |x2 - x1| = |3.7 - 4.4| = 0.7",
            "h2 = |x3 - x2| = |3.1 - 3.7| = 0.6",
            "D1¹ = (y2 - y1) / (x2 - x1) = (-1.59 - (-0.68)) / (3.7 - 4.4) = 1.3",
            "D2¹ = (y3 - y2) / (x3 - x2) = (-1.82 - (-1.59)) / (3.1 - 3.7) = 0.38333333",
            "D1² = (D2¹ - D1¹) / (x3 - x1) = (0.38333333 - 1.3) / (3.1 - 4.4) = 0.705128205",
            "g(x) = D⁰ + D1¹(x - x1) + D1²(x - x1)(x - x2)",
            "g(x) = (-0.68) + (1.3)(3.5 - 4.4) + (0.705128205)(3.5 - 4.4)(3.5 - 3.7)",
            "g(x) = -1.723076923"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula la 1ra diferencia dividida D1¹", "pista": "D1¹ = (y2 - y1) / (x2 - x1)", "respuesta": "1.3"},
            {"pregunta": "Calcula la 1ra diferencia dividida D2¹", "pista": "D2¹ = (y3 - y2) / (x3 - x2)", "respuesta": "0.38333333"},
            {"pregunta": "Calcula la 2da diferencia dividida D1²", "pista": "D1² = (D2¹ - D1¹) / (x3 - x1)", "respuesta": "0.705128205"},
            {"pregunta": "Calcula la respuesta final de g(x)", "pista": "Aplica el polinomio con D⁰, D1¹ y D1²", "respuesta": "-1.723076923"}
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
        "problema": "y = x³ - 6.5x + 2",
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
            {"pregunta": "¿Entre qué intervalos de X hay cambios de signo?", "pista": "Escribe solamente los incisos con el formato [X, Y], [X, Y], [X, Y]", "respuesta": "[-3, -2], [0, 1], [2, 3]"}
        ],
        "respuesta_final": "[-3, -2], [0, 1], [2, 3]"
    },
    {
        "id": 8,
        "metodo": "Bisectriz",
        "problema": "En la gráfica de la función y = x³ - 6.5x + 2.",
        "valores": "Iteraciones de búsqueda usando x = (a+b)/2",
        "procedimiento": [
            "a=0, b=1, X=0.5",
            "a=0, b=0.5, X=0.25 (comportamiento +)",
            "a=0.25, b=0.5, X=0.375",
            "a=0.25, b=0.375, X=0.3125 (comportamiento -)",
            "a=0.25, b=0.3175, X=0.28375 (comportamiento +)",
            "a=0.3, b=0.3175, X=0.3087 (comportamiento +)",
            "E = |xi+1 - xi| = 0.001"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X en la primera iteración (a=0, b=1)", "pista": "X = (a+b)/2", "respuesta": "0.5"},
            {"pregunta": "Calcula X en la iteración 2", "pista": "Nuevo intervalo a=0, b=0.5", "respuesta": "0.25"},
            {"pregunta": "Calcula X en la iteración 3", "pista": "Nuevo intervalo a=0.25, b=0.5", "respuesta": "0.375"},
            {"pregunta": "Calcula X en la iteración 4", "pista": "Nuevo intervalo a=0.25, b=0.375", "respuesta": "0.3125"},
            {"pregunta": "Calcula la X final", "pista": "La que cumple E=0.001", "respuesta": "0.3087"}
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
            "i=1, (e^0 - 2)/2 = -0.5, E = |-0.5 - 0| = 0.5",
            "i=2, (e^-0.5 - 2)/2 = -0.69673467, E = 0.19673467",
            "... (Iteraciones continúan de la misma forma hasta i=9)",
            "i=9, (e^-0.768027404 - 2)/2 = -0.768036346, E = 0.000008941",
            "El margen de error se encuentra en: E = |x9 - x8|",
            "E = |-0.768036346 - (-0.768036346)| = 0.000008941"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X1", "pista": "Sustituye X0 en la ecuación despejada.", "respuesta": "-0.5"},
            {"pregunta": "Calcula X2", "pista": "Sustituye X1 en la ecuación despejada.", "respuesta": "-0.69673467"},
            {"pregunta": "Calcula la X final convergente", "pista": "Calcula hasta i=9", "respuesta": "-0.768036346"}
        ],
        "respuesta_final": "-0.768036346"
    },
    {
        "id": 10,
        "metodo": "Newton - Raphson",
        "problema": "Encuentre la raíz real de la ecuación f(x) = 0.8x² + x - 3",
        "valores": "i=0, xo = 1",
        "procedimiento": [
            "f'(x) = 1.6x + 1",
            "i=0, xo = 1",
            "i=1, x1 = 1 - ( (0.8(1)² + (1) - 3) / (1.6(1) + 1) ) = 1.461538462 | E = |1.461538462 - 1| = 0.461538462",
            "i=2, x2 = 1.461538462 - ( (0.8(1.461538462)² + (1.461538462) - 3) / (1.6(1.461538462) + 1) ) = 1.410492733 | E = |1.410492733 - 1.461538462| = 0.051045728",
            "i=3, x3 = 1.410492733 - ( (0.8(1.410492733)² + (1.410492733) - 3) / (1.6(1.410492733) + 1) ) = 1.409852675 | E = |1.409852675 - 1.410492733| = 0.000640057",
            "i=4, x4 = 1.409852675 - ( (0.8(1.409852675)² + (1.409852675) - 3) / (1.6(1.409852675) + 1) ) = 1.409852575 | E = |1.409852575 - 1.409852675| = 0.0000001"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula X1", "pista": "xi - f(xi)/f'(xi) para i=0", "respuesta": "1.461538462"},
            {"pregunta": "Calcula X2", "pista": "xi - f(xi)/f'(xi) para i=1", "respuesta": "1.410492733"},
            {"pregunta": "Calcula la raíz final (X4)", "pista": "Donde el error es casi cero.", "respuesta": "1.409852575"}
        ],
        "respuesta_final": "1.409852575"
    },
    {
        "id": 11,
        "metodo": "Falsa Posición ó Regula - Falsi",
        "problema": "Calcule la raíz para f(x) = xe^x - 10",
        "valores": "a=1, b=2",
        "procedimiento": [
            "a=1, f(a)=-7.281718172",
            "b=2, f(b)=4.778112190",
            "i=0, b=2, f(b)=4.778112190, a=1, X=1.603799386, f(a)=-7.281718172",
            "i=1, b=2, f(b)=4.778112190, a=1.603799386, X=1.721776248, f(a)=-2.026091162, E = 0.117976862",
            "i=2, b=2, f(b)=4.778112190, a=1.721776248, X=1.741651888, f(a)=-0.367597181, E = 0.01987564",
            "i=3, b=2, f(b)=4.778112190, a=1.741651888, X=1.744898309, f(a)=-0.060806187, E = 0.003246421",
            "i=4, b=2, f(b)=4.778112190, a=1.744898309, X=1.745425782, f(a)=-0.009900159, E = 0.000527473",
            "E = |xi5 - xi4| = |1.745425782 - 1.744898309|",
            "E = 0.000527473"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula f(a) para a=1", "pista": "Evalúa 1 en la función.", "respuesta": "-7.281718172"},
            {"pregunta": "Calcula f(b) para b=2", "pista": "Evalúa 2 en la función.", "respuesta": "4.778112190"},
            {"pregunta": "Calcula la aproximación X (i=0)", "pista": "Aplica la fórmula de Regula Falsi en la i=0.", "respuesta": "1.603799386"},
            {"pregunta": "Calcula la aproximación X (i=1)", "pista": "Aplica la fórmula en la i=1.", "respuesta": "1.721776248"},
            {"pregunta": "Calcula la aproximación X (i=2)", "pista": "Aplica la fórmula en la i=2.", "respuesta": "1.741651888"},
            {"pregunta": "Calcula la raíz final aproximada", "pista": "La iteración donde E = 0.000527473", "respuesta": "1.745425782"}
        ],
        "respuesta_final": "1.745425782"
    },
    {
        "id": 12,
        "metodo": "Secante",
        "problema": "Calcule la raíz de f(x) = e^(-x) - x.",
        "valores": "x0 = 0, x1 = 1",
        "procedimiento": [
            "x0 = 0, f(x0) = e^(-0) - 0 = 1",
            "x1 = 1, f(x1) = e^(-1) - 1 = -0.632120558",
            "i=2, x2 = x1 - (f(x1)(x1 - x0)) / (f(x1) - f(x0)) = 1 - {(-0.632120558(1 - 0)) / (-0.632120558 - 1)} = 0.612699836, E = |0.612699836 - 1| = 0.387300613",
            "i=3, x3 = x2 - (f(x2)(x2 - x1)) / (f(x2) - f(x1)) = 0.612699836 - {(-0.070813947(0.612699836 - 1)) / (-0.070813947 - (-0.632120558))} = 0.563838389, E = |0.563838389 - 0.612699836| = 0.048861447",
            "i=4, x4 = 0.563838423 - {(-0.00004241924099(0.5638389 - 0.612699836)) / (0.005182354419 - (-0.070813946))} = 0.567170358, E = |0.567170358 - 0.563838389| = 0.003331969259",
            "i=5, X5 = x4 - (f(x4)(x4 - x3)) / (f(x4) - f(x3)) = 0.567170358 - {(-0.00004241924099(0.567170358 - 0.563838389)) / (-0.00004241924099 - 0.005182354419)} = 0.567143306, E = |0.567143306 - 0.567170358| = 0.00002705181386"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula f(x0)", "pista": "Evalúa x0 en la función.", "respuesta": "1"},
            {"pregunta": "Calcula f(x1)", "pista": "Evalúa x1 en la función.", "respuesta": "-0.632120558"},
            {"pregunta": "Calcula X2", "pista": "Aplica la fórmula de la Secante para i=2.", "respuesta": "0.612699836"},
            {"pregunta": "Calcula X3", "pista": "Aplica la fórmula de la Secante para i=3.", "respuesta": "0.563838389"},
            {"pregunta": "Calcula X4", "pista": "Aplica la fórmula de la Secante para i=4.", "respuesta": "0.567170358"},
            {"pregunta": "Calcula la raíz final (X5)", "pista": "Iteración final.", "respuesta": "0.567143306"}
        ],
        "respuesta_final": "0.567143306"
    },
    {
        "id": 13,
        "metodo": "Montante",
        "problema": "Resolver: 2a + 5b - 2c = 1 | -a + 2b + 3c = 2 | 3a - 3b + 2c = 3",
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
        "problema": "Resolver: 3a - 2b + 2c = 1 | 4a + 2b + 2c = 2 | 3a - 3b + 3c = 3",
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
        "problema": "Resolver: 2x1 + x2 - 3x3 = -1 | -x1 + 3x2 + 2x3 = 12 | 3x1 + x2 - 3x3 = 0",
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
            {"pregunta": "Pivote fila 2 (reducido)", "pista": "Término en 2,2 después de ceros.", "respuesta": "7/2"},
            {"pregunta": "Pivote fila 3 (reducido)", "pista": "Término en 3,3 después de ceros.", "respuesta": "11/7"},
            {"pregunta": "Calcula el valor de x3", "pista": "Sustitución hacia atrás.", "respuesta": "2"},
            {"pregunta": "Calcula el valor de x2", "pista": "Sustitución hacia atrás.", "respuesta": "3"},
            {"pregunta": "Calcula el valor de x1", "pista": "Sustitución hacia atrás.", "respuesta": "1"}
        ],
        "respuesta_final": "x1 = 1, x2 = 3, x3 = 2"
    },
    {
        "id": 16,
        "metodo": "Gauss - Seidel",
        "problema": "x - 3y + 5z = 5 | 8x - y - z = 8 | -2x + 4y + z = 4",
        "valores": "x0 = y0 = z0 = 0",
        "procedimiento": [
            "Despejando las variables para la Diagonal Dominante:",
            "x = (8+y+z)/8, y = (4+2x-z)/4, z = (5-x+3y)/5",
            "1era. Iteración:",
            "x1 = (8+0+0)/8 = 1 | y1 = (4+2(1)-0)/4 = 1.5 | z1 = (5-1+3(1.5))/5 = 1.7",
            "2da. Iteración:",
            "x2 = (8+1.5+1.7)/8 = 1.4 | y2 = (4+2(1.4)-1.7)/4 = 1.275 | z2 = (5-1.4+3(1.275))/5 = 1.485",
            "(Las iteraciones continúan hasta cumplir E = 0.001 en la iteración 5)"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula x1 en la primera iteración", "pista": "x = (8+y+z)/8", "respuesta": "1"},
            {"pregunta": "Calcula y1 en la primera iteración", "pista": "y = (4+2x-z)/4", "respuesta": "1.5"},
            {"pregunta": "Escribe el texto exacto de conclusión", "pista": "Iteración 5...", "respuesta": "Iteración 5 converge a la respuesta"}
        ],
        "respuesta_final": "Iteración 5 converge a la respuesta"
    },
    {
        "id": 17,
        "metodo": "Jacobi",
        "problema": "x - 3y + 5z = 5 | 8x - y - z = 8 | -2x + 4y + z = 4",
        "valores": "x0 = y0 = z0 = 1",
        "procedimiento": [
            "Despejando:",
            "x = (8+y+z)/8, y = (4+2x-z)/4, z = (5-x+3y)/5",
            "1era. Iteración:",
            "x1 = (8+1+1)/8 = 1.25 | y1 = (4+2(1)-1)/4 = 1.25 | z1 = (5-1+3(1))/5 = 1.4",
            "2da. Iteración:",
            "x2 = (8+1.25+1.4)/8 = 1.33125 | y2 = (4+2(1.25)-1.4)/4 = 1.275 | z2 = (5-1.25+3(1.25))/5 = 1.5",
            "(El proceso se repite en paralelo hasta converger)"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula x1 en la primera iteración", "pista": "Usar valores en t=0.", "respuesta": "1.25"},
            {"pregunta": "Calcula x2 en la segunda iteración", "pista": "Usar valores en t=1.", "respuesta": "1.33125"},
            {"pregunta": "Escribe el texto exacto de conclusión", "pista": "Proceso iterativo...", "respuesta": "Proceso iterativo converge"}
        ],
        "respuesta_final": "Proceso iterativo converge"
    },
    {
        "id": 18,
        "metodo": "Mínimos Cuadrados (Línea Recta)",
        "problema": "Ajustar los datos a una línea recta g(x) = a0 + a1x",
        "valores": "Σx=25.8, Σx²=169.88, Σy=28.4, Σxy=159.47",
        "procedimiento": [
            "Ecuaciones Normales:",
            "1) 6 a0 + 25.8 a1 = 28.4",
            "2) 25.8 a0 + 169.88 a1 = 159.47",
            "Multiplicar la ecuación 1 por 4.3:",
            "3) -25.8 a0 - 110.94 a1 = -122.12",
            "Sumar ecuaciones 2 y 3:",
            "0 a0 + 58.94 a1 = 37.35 => a1 = 37.35 / 58.94 = 0.633695283",
            "Sustituir a1 en ec. 1:",
            "6 a0 + 25.8(0.633695283) = 28.4 => 6 a0 = 12.05066169 => a0 = 2.008443615"
        ],
        "pasos_juego": [
            {"pregunta": "Resuelve la suma: 0 a0 + 58.94 a1 = ?", "pista": "Resta 159.47 - 122.12", "respuesta": "37.35"},
            {"pregunta": "Calcula a1", "pista": "Despeja a1 de la suma.", "respuesta": "0.633695283"},
            {"pregunta": "Ingresa la respuesta final", "pista": "Formato: a0 = X, a1 = Y", "respuesta": "a0 = 2.008443615, a1 = 0.633695283"}
        ],
        "respuesta_final": "a0 = 2.008443615, a1 = 0.633695283"
    },
    {
        "id": 19,
        "metodo": "Regla Trapezoidal",
        "problema": "Integral de 2 a 3 de (1 / (1+x²)) dx con n = 4",
        "valores": "a = 2, b = 3, n = 4",
        "procedimiento": [
            "h = (b-a)/n = (3-2)/4 = 1/4",
            "I = (1/4 / 2) * { f(x=2) + 2{f(x=9/4) + f(x=5/2) + f(x=11/4)} + f(x=3) }",
            "I = (1/4 / 2) * { 1/(1+(2)²) + 2( 1/(1+(9/4)²) + 1/(1+(5/2)²) + 1/(1+(11/4)²) ) + 1/(1+(3)²) }",
            "I = (1/4 / 2) * (0.2 + (32/97) + (8/29) + (32/137) + 0.1)",
            "I = 1/8 (1.139335619)",
            "I = 0.142416952"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el valor de h", "pista": "h = (b-a)/n", "respuesta": "0.25"},
            {"pregunta": "Calcula la sumatoria interna", "pista": "La suma total de corchetes, multiplicado por h/2.", "respuesta": "1.139335619"},
            {"pregunta": "Calcula el resultado I final", "pista": "Aplica la Regla Trapezoidal.", "respuesta": "0.142416952"}
        ],
        "respuesta_final": "0.142416952"
    },
    {
        "id": 20,
        "metodo": "Newton - Cotes (Abiertas)",
        "problema": "Integral de -2 a 2 de (3x³ - 10) dx con n = 4",
        "valores": "a = -2, b = 2, n = 4",
        "procedimiento": [
            "h = (b-a)/(n+2) = (2 - (-2))/(4+2) = 2/3",
            "α = 6/20",
            "I = [6/20][2/3] * { [(0)f(x=-2)] + [(11)f(x=-4/3)] + [(-14)f(x=-2/3)] + [(26)f(x=0)] + [(-14)f(x=2/3)] + [(11)f(x=4/3)] + [(0)f(x=2)] }",
            "I = [1/5] * { (-1694/9) + (1372/9) + 260 + (1148/9) - (289/9) }",
            "I = [1/5][-200]",
            "I = -40"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el sumando principal interior", "pista": "Es un número entero negativo.", "respuesta": "-200"},
            {"pregunta": "Calcula el factor multiplicador \u03b1*h", "pista": "Es una fracción simple [6/20][2/3]. En decimal o fracción.", "respuesta": "0.2"},
            {"pregunta": "Calcula I", "pista": "Multiplica ambos factores.", "respuesta": "-40"}
        ],
        "respuesta_final": "-40"
    },
    {
        "id": 21,
        "metodo": "Regla de 1/3 Simpson",
        "problema": "Integral de 2 a 3 de (1 / (1+x²)) dx con n = 10",
        "valores": "a = 2, b = 3, n = 10",
        "procedimiento": [
            "h = (b-a)/n = (3-2)/10 = 1/10",
            "I = (1/10 / 3) * { f(x=2) + 4f(x=21/10) + 2f(x=11/5) + 4f(x=23/10) + 2f(x=12/5) + 4f(x=5/2) + 2f(x=13/5) + 4f(x=27/10) + 2f(x=14/5) + 4f(x=29/10) + f(x=3) }",
            "I = 1/30 * (0.2 + 400/541 + 25/73 + 400/629 + 50 + 169 + 16/29 + 25/97 + 400/829 + 50/221 + 400/941 + 0.1)",
            "I = 1/30 * (4.256914514)",
            "I = 0.14189715"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula h", "pista": "h = (b-a)/n", "respuesta": "0.1"},
            {"pregunta": "Calcula la suma interna (corchetes)", "pista": "Suma total dentro de los corchetes.", "respuesta": "4.256914514"},
            {"pregunta": "Calcula I final", "pista": "Multiplica la suma por h/3.", "respuesta": "0.14189715"}
        ],
        "respuesta_final": "0.14189715"
    },
    {
        "id": 22,
        "metodo": "Regla de 3/8 Simpson",
        "problema": "Integral de 0 a 1 de x³e^x dx con n = 3",
        "valores": "a = 0, b = 1, n = 3",
        "procedimiento": [
            "h = (b-a)/n = (1-0)/3 = 1/3",
            "I = (3/8)[1/3] * { f(x=0) + 3(f(x=1/3) + f(x=2/3)) + f(x=1) }",
            "I = [3/8][1/3] * { [(0)³e^0] + 3[ (1/3)³e^(1/3) + (2/3)³e^(2/3) ] + [(1)³e^1] }",
            "I = [1/8] * (0 + 0.155068047 + 1.731319148 + 2.718281828)",
            "I = [1/8] * [4.604669023]",
            "I = 0.575583627"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el coeficiente multiplicador (3h/8)", "pista": "Sustituye h en (3/8)*h.", "respuesta": "0.125"},
            {"pregunta": "Calcula la suma interna", "pista": "Suma dentro de los corchetes.", "respuesta": "4.604669023"},
            {"pregunta": "Calcula I final", "pista": "Aplica la regla de 3/8 de Simpson.", "respuesta": "0.575583627"}
        ],
        "respuesta_final": "0.575583627"
    },
    {
        "id": 23,
        "metodo": "Euler hacia Adelante",
        "problema": "3y' - 5yt + 1 = 0",
        "valores": "y0 = 2, h = 0.2, t0 = 0",
        "procedimiento": [
            "y' = (5yt - 1) / 3",
            "y1 = y0 + h{(5y0t0 - 1)/3} = 2 + (0.2){(5(2)(0) - 1)/3}",
            "y1 = 1.933333333",
            "t1 = t0 + h = 0 + 0.2 = 0.2",
            "y2 = y1 + h{(5y1t1 - 1)/3} = 1.933333333 + (0.2){(5(1.933333333)(0.2) - 1)/3}",
            "y2 = 1.995555556"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula y1", "pista": "Aplica la fórmula de Euler para la primera iteración.", "respuesta": "1.933333333"},
            {"pregunta": "Calcula t1", "pista": "t1 = t0 + h", "respuesta": "0.2"},
            {"pregunta": "Calcula y2 final", "pista": "Aplica la fórmula de Euler con y1, t1.", "respuesta": "1.995555556"}
        ],
        "respuesta_final": "1.995555556"
    },
    {
        "id": 24,
        "metodo": "Euler Modificado",
        "problema": "2y' + 3yt + y = 0",
        "valores": "y0 = 1.2, h = 0.3, y1 = 1.2, t0 = 0, t1 = 0.3",
        "procedimiento": [
            "Despejar y': y' = (-3yt - y) / 2",
            "y'1 = y0 + (h/2){ [(-3y0t0 - y0)/2] + [(-3y1t1 - y1)/2] }",
            "y'1 = 1.2 + (0.3/2){ ( (-3(1.2)(0) - (1.2))/2 ) + ( (-3(1.2)(0.3) - (1.2))/2 ) }",
            "y'1 = 1.2 + [0.15][-0.6 - 1.14]",
            "y'1 = 0.939"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula el primer término de f(t,y)", "pista": "(-3y0t0 - y0)/2", "respuesta": "-0.6"},
            {"pregunta": "Calcula el segundo término de f(t,y)", "pista": "(-3y1t1 - y1)/2", "respuesta": "-1.14"},
            {"pregunta": "Calcula y'1", "pista": "Aplica Euler modificado.", "respuesta": "0.939"}
        ],
        "respuesta_final": "0.939"
    },
    {
        "id": 25,
        "metodo": "Runge - Kutta de 2do orden",
        "problema": "y' - 2ty + 1 = 0",
        "valores": "y0 = 1, h = 0.6, t0 = 0",
        "procedimiento": [
            "Despejar: y' = 2ty - 1",
            "k1 = 0.6( 2(0)(1) - 1 ) = -0.6",
            "k2 = 0.6{ [2(0 + 0.6)[1 + (-0.6)]] - 1 } = 0.6{ [2(0.6)(0.4)] - 1 }",
            "k2 = 0.303265329",
            "y1 = 1 + 1/2(-1 + 0.30326529)",
            "y1 = 0.651632664"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye en la ecuación de k1.", "respuesta": "-0.6"},
            {"pregunta": "Calcula k2", "pista": "Sustituye en la ecuación de k2.", "respuesta": "0.303265329"},
            {"pregunta": "Calcula y1 final", "pista": "Aplica Runge-Kutta 2do Orden.", "respuesta": "0.651632664"}
        ],
        "respuesta_final": "0.651632664"
    },
    {
        "id": 26,
        "metodo": "Runge - Kutta de 3er Orden",
        "problema": "y' = (2yt + 1) / y²",
        "valores": "y0 = 1, h = 0.25, t0 = 0",
        "procedimiento": [
            "k1 = 0.25( (2(1)(0) + 1) / (1)² ) = 0.25",
            "k2 = 0.25{ (2(1 + 0.25/2)(0 + 0.25/2) + 1) / (1 + 0.25/2)² } = 0.253086419",
            "k3 = 0.25{ (2[1 - 0.25 + 2(0.253086419)][0 + 0.25] + 1) / [1 - 0.25 + 2(0.253086419)]² } = 0.257939981",
            "y1 = 1 + 1/6[0.25 + 4(0.253086419) + 0.257993981]",
            "y1 = 1.211723276"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Sustituye en la fórmula de k1.", "respuesta": "0.25"},
            {"pregunta": "Calcula k2", "pista": "Sustituye en la fórmula de k2.", "respuesta": "0.253086419"},
            {"pregunta": "Calcula k3", "pista": "Sustituye en la fórmula de k3.", "respuesta": "0.257939981"},
            {"pregunta": "Calcula y1 final", "pista": "Aplica Runge-Kutta 3er Orden.", "respuesta": "1.211723276"}
        ],
        "respuesta_final": "1.211723276"
    },
    {
        "id": 27,
        "metodo": "Runge - Kutta de 4to. Orden por 1/3 de Simpson",
        "problema": "y' = (y + t)² / (1 - y)",
        "valores": "y0 = 0.4, h = 0.2, t0 = 0",
        "procedimiento": [
            "k1 = (0.2){ [0.4 + 0]² / (1 - 0.4) } = (0.2){ (0.4)² / 0.6 } = 0.053333333",
            "k2 = (0.2)[ [0.4 + (0.053333333/2) + (0 + (0.2/2))]² / (1 - [0.4 + (0.053333333/2)]) ] = 0.096759689",
            "k3 = (0.2)[ [0.4 + (0.096759689/2) + (0 + (0.2/2))]² / (1 - [0.4 + (0.096759689/2)]) ] = 0.109031713",
            "k4 = (0.2){ [0.4 + 0.109031713 + (0 + 0.2)]² / (1 - (0.4 + 0.109031713)) } = 0.2047895890",
            "y1 = 0.4 + 1/6(0.053333333 + 2(0.096759688) + 2(0.109031713) + 0.204789589)",
            "y1 = 0.511617621"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Evalúa la función con valores iniciales.", "respuesta": "0.053333333"},
            {"pregunta": "Calcula k2", "pista": "Aplica la fórmula de k2.", "respuesta": "0.096759689"},
            {"pregunta": "Calcula k3", "pista": "Aplica la fórmula de k3 con k2.", "respuesta": "0.109031713"},
            {"pregunta": "Calcula k4", "pista": "Aplica la fórmula de k4.", "respuesta": "0.2047895890"},
            {"pregunta": "Calcula y1 final", "pista": "Aplica Simpson 1/3.", "respuesta": "0.511617621"}
        ],
        "respuesta_final": "0.511617621"
    },
    {
        "id": 28,
        "metodo": "Runge - Kutta de 4to. Orden por 3/8 de Simpson",
        "problema": "y' = -y / (y² + t)",
        "valores": "y0 = 1, h = 0.5, t0 = 0",
        "procedimiento": [
            "k1 = 0.5{ -1 / ((1)² + 0) } = -0.5",
            "k2 = 0.5{ (-1 + (-0.5/3)) / ([1 + (-0.5/3)]² + [0 + (0.5/3)]) } = -0.483870959",
            "k3 = 0.5{ (-1 + (-0.5/3) + (-0.483870959/3)) / ([1 + (-0.5/3) + (-0.483870959/3)]² + [0 + 2/3(0.5)]) } = -0.428066426",
            "k4 = 0.5{ (-1 + (-0.5) - (-0.483870959 + (-0.428066428))) / ([1 + (-0.5) - (-0.483870959) + (-0.428066428)]² + (0 + 0.5)) } = -0.343547869",
            "y1 = 1 + 1/8[ -0.5 + 3(-0.483870959) + 3(-0.428066426) + (-0.343547869) ]",
            "y1 = 1 + (-0.447420003) = 0.552579997"
        ],
        "pasos_juego": [
            {"pregunta": "Calcula k1", "pista": "Calcula el primer incremento.", "respuesta": "-0.5"},
            {"pregunta": "Calcula k2", "pista": "Calcula el segundo incremento.", "respuesta": "-0.483870959"},
            {"pregunta": "Calcula k3", "pista": "Calcula el tercer incremento.", "respuesta": "-0.428066426"},
            {"pregunta": "Calcula k4", "pista": "Calcula el último incremento de Runge Kutta.", "respuesta": "-0.343547869"},
            {"pregunta": "Calcula y1 final", "pista": "Aplica Simpson 3/8.", "respuesta": "0.552579997"}
        ],
        "respuesta_final": "0.552579997"
    },
    {
        "id": 29,
        "metodo": "Runge - Kutta de Orden Superior",
        "problema": "2y'' - 4y't - 2y = 0",
        "valores": "y0 = 1.1, h = 0.2, y'0 = 1.2, t0 = 0",
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
            {"pregunta": "Calcula k1", "pista": "h * Vn", "respuesta": "0.24"},
            {"pregunta": "Calcula m1", "pista": "Calcula la función con valores iniciales.", "respuesta": "-0.22"},
            {"pregunta": "Calcula k2", "pista": "Calcula el segundo incremento k2.", "respuesta": "0.196"},
            {"pregunta": "Calcula m2", "pista": "Calcula el segundo incremento m2.", "respuesta": "-0.1892"},
            {"pregunta": "Calcula y1", "pista": "Aplica la fórmula para y1.", "respuesta": "1.318"},
            {"pregunta": "Calcula y'1", "pista": "Aplica la fórmula para y'1.", "respuesta": "0.9952"}
        ],
        "respuesta_final": "y1 = 1.318, y'1 = 0.9952"
    }
]
