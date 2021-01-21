# Juego de adivina el número
# Darle vidas al usuario (5) -- Ya
# Dar pistas al usuario si el número mayor o menor del ingresado -- Ya
# Opción de volver a jugar generando un número diferente --Ya

import random


print("Bienvenido a adivina el número")
while True:
    print("Elige el nivel de dificultad: ")
    print("1. Facil - 5 intentos y numeros del 1 al 10")
    print("2. Media - 5 intentos y numeros del 1 al 40")
    print("3. Dificil - 3 intentos y numeros del 1 al 40")
    try:
        dificultad = int(input("Ingresa la dificultad: "))
    except ValueError:
        print("Ingresa una opción correcta.")
    if dificultad == 1:
        vidas = 5
        numeroAleatorio = random.randint(1, 10)
    elif dificultad == 2:
        vidas = 5
        numeroAleatorio = random.randint(1, 40)
    elif dificultad == 3:
        vidas = 3
        numeroAleatorio = random.randint(1, 40)
    while vidas > 0:
        print("Tienes "+str(vidas)+" vidas")
        try:
            adivinanza = int(input("Ingresa tu número: "))
        except ValueError:
            print("Ingrese un número valido.")
        else:
            if adivinanza == numeroAleatorio:
                print("Felicidades, ganaste.")
                break
            else:
                print("No has acertado, sigue intentando.")
                if adivinanza > numeroAleatorio:
                    print("El número secreto es menor")
                else:
                    print("El número secreto es mayor")
                vidas -= 1
    again = int(input("Has perdido ¿Quieres volver a jugar? 1. Si - 2. No \n"))
    if again == 2:
        break
    else:
        numeroAleatorio = random.randint(1, 10)
        vidas = 5

print("Gracias por participar")
