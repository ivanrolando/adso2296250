import math

def caracterizar_triangulo(lado_a, lado_b, lado_c):

    if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
        return "Los lados ingresados no forman un triángulo válido."


    if lado_a == lado_b == lado_c:
        tipo_lados = "Equilátero"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"


    angulo_A = math.acos((lado_b**2 + lado_c**2 - lado_a**2) / (2 * lado_b * lado_c)) * (180 / math.pi)
    angulo_B = math.acos((lado_a**2 + lado_c**2 - lado_b**2) / (2 * lado_a * lado_c)) * (180 / math.pi)
    angulo_C = 180 - angulo_A - angulo_B 


    if angulo_A == 90 or angulo_B == 90 or angulo_C == 90:
        tipo_angulos = "Rectángulo"
    elif angulo_A < 90 and angulo_B < 90 and angulo_C < 90:
        tipo_angulos = "Acutángulo"
    else:
        tipo_angulos = "Obtusángulo"


    return {
        "Tipo de lados": tipo_lados,
        "Ángulo A": angulo_A,
        "Ángulo B": angulo_B,
        "Ángulo C": angulo_C,
        "Tipo de ángulos": tipo_angulos,
    }


lado_a = float(input("Ingrese el lado A del triángulo: "))
lado_b = float(input("Ingrese el lado B del triángulo: "))
lado_c = float(input("Ingrese el lado C del triángulo: "))


resultado = caracterizar_triangulo(lado_a, lado_b, lado_c)


print("\nResultados:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")