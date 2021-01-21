# Nos permiten obtener trozos de una lista o cadena

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

print(numeros[1])

# Slices
# El punto de partida es inclusivo, pero el punto de llegada es exclusivo, por lo tanto no nos imprimiria el número en el indice 6
print(numeros[0:6])
print(numeros[0:1])
# Si ponemos que llegue hasta un numero mas grande que el tamaño de nuestra lista, nos devolvera la lista completa
print(numeros[0:999])
print(numeros[2:])  # Nos devolvera la lista completa
print(numeros[:5])  # Va a contar desde el indice 0
print(numeros[:])  # Lo imprime todo

# Indices negativos en Slices
print(numeros[-6:-3])
print(numeros[-6])
