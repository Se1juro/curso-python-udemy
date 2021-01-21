try:
    numero1 = int(input("Ingrese un número: "))
    numero2 = int(input("Ingrese el segundo número: "))
except ValueError:
    print("Por favor, ingresa dos números enteros")
else:
    resultado = numero1 + numero2
    print("La suma es "+str(resultado))
