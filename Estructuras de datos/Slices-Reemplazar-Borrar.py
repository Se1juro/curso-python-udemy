numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del numeros[0]
print(numeros)

del numeros[0:5]
print(numeros)

numeros[1:2] = [6, 7, 8]
print(numeros)

numeros[4:6] = [80, 80]
print(numeros)
