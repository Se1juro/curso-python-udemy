# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer función de union
# Debemos hacer función de intersección
# Debemos hacer función de diferencia
# Debemos hacer función de diferencia simetrica
def verInstrucciones():
    print("Operaciones que puedes realizar: ")
    print("1. Union")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Diferencia Simetrica")
    print("5. Ver instrucciones")
    print("6. Cambiar Conjuntos")
    print("7. Salir")


def union_conjuntos(conjuntoA, conjuntoB):
    print("\nLa union de A y B es: {}\n".format(conjuntoA.union(conjuntoB)))


def interseccion_conjuntos(conjuntoA, conjuntoB):
    print("\nLa intersección de A y B es: {}\n".format(
        conjuntoA.intersection(conjuntoB)))


def diferencia_simetrica_conjuntos(conjuntoA, conjuntoB):
    print("\nLa diferencia simetrica de A y B es: {}\n".format(
        conjuntoA.symmetric_difference(conjuntoB)))


def diferencia_conjuntos(conjuntoA, conjuntoB):
    print("Elige la diferencia que quieres realizar")
    print("1. A - B")
    print("2. B - A")
    try:
        operacion = int(input(": "))
    except ValueError:
        print("\nElige 1 o 2.\n")
        diferencia_conjuntos(conjuntoA, conjuntoB)
    else:
        if operacion == 1:
            print("\nLa diferencia de A - B: {}\n".format(
                conjuntoA.difference(conjuntoB)))
        elif operacion == 2:
            print("\nLa diferencia de B - A: {}\n".format(
                conjuntoB.difference(conjuntoA)))
        else:
            print("Operación desconocida, intenta de nuevo.\n")
            diferencia_conjuntos(conjuntoA, conjuntoB)


def calculadora_conjuntos():
    print("Bienvenido a los conjuntos")
    print("Introduce los elementos de los conjuntos separados por espacios")
    print("Ejemplo: 1 3 5 8 0 2")

    conjuntoA = set(input("Ingrese los elementos del conjunto A: ").split())
    conjuntoB = set(input("Ingrese los elementos del conjunto B: ").split())

    verInstrucciones()

    while True:
        try:
            operacion = int(input(": "))
        except ValueError:
            print("Introduce un número del 1 al 6.")
        else:
            if operacion == 1:
                union_conjuntos(conjuntoA, conjuntoB)
            elif operacion == 2:
                interseccion_conjuntos(conjuntoA, conjuntoB)
            elif operacion == 3:
                diferencia_conjuntos(conjuntoA, conjuntoB)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjuntoA, conjuntoB)
            elif operacion == 5:
                verInstrucciones()
            elif operacion == 6:
                conjuntoA = set(
                    input("Ingrese los elementos del conjunto A: ").split())
                conjuntoB = set(
                    input("Ingrese los elementos del conjunto B: ").split())
            elif operacion == 7:
                print("\nGracias por usar nuestra aplicación.\n")
                break
            else:
                print("Operación desconocida")


calculadora_conjuntos()
