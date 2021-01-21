continuar = 1
numero_operacion = 0
while continuar == 1:
    print("Bienvenido a la calculadora")
    print("Estas son las operaciones que puedes realizar: ")
    while numero_operacion == 0 and numero_operacion < 5:
        print("1 - Suma \n2 - Resta \n3 - Multiplicación \n4 - División")
        try:
            numero_operacion = int(
                input("Introduce el número de operaciones que quieres realizar: "))
        except ValueError:
            print("Elige una opción correcta")

    try:
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
    except ValueError:
        print("Ingresa un número correcto.")
    else:
        if numero_operacion == 1:
            resultado = numero1+numero2
            print("El resultado es: "+str(resultado))
        elif numero_operacion == 2:
            resultado = numero1-numero2
            print("El resultado es: "+str(resultado))
        elif numero_operacion == 3:
            resultado = numero1*numero2
            print("El resultado es: "+str(resultado))
        elif numero_operacion == 4:
            resultado = numero1/numero2
            print("El resultado es: "+str(resultado))
        else:
            print("Por favor, ingresa una opción que este disponible")
    continuar = int(input("¿Desea continuar? 1. Si - 2. No\n"))
    numero_operacion = 0
    print()
    print()
