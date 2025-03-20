import math

def calcular_angulos(a, b, c):
    """Calcula los ángulos de un triángulo dados sus tres lados usando la Ley de Cosenos."""
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C = 180 - (A + B)  
    return round(A, 2), round(B, 2), round(C, 2)

def caracterizar_triangulo(a, b, c):
    """Clasifica el triángulo según sus lados."""
    if a == b == c:
        return "Equilátero (Tres lados iguales)"
    elif a == b or a == c or b == c:
        return "Isósceles (Dos lados iguales)"
    else:
        return "Escaleno (Todos los lados diferentes)"

def main():
    print("🔺 CARACTERIZADOR DE TRIÁNGULOS 🔺")
    

    a = float(input("Ingrese el lado a: "))
    b = float(input("Ingrese el lado b: "))
    c = float(input("Ingrese el lado c: "))

    
    if a + b > c and a + c > b and b + c > a:
        A, B, C = calcular_angulos(a, b, c)  
        tipo = caracterizar_triangulo(a, b, c)  
        
        print("\n🔹 Resultados:")
        print(f"✔ Lados: a={a}, b={b}, c={c}")
        print(f"✔ Ángulos: A={A}°, B={B}°, C={C}°")
        print(f"✔ Clasificación: {tipo}")
    else:
        print("❌ Los lados ingresados NO forman un triángulo válido.")

if __name__ == "__main__":
    main()
