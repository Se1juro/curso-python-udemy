# Iteración de diccionarios
diccionario_calificaciones = {
    "Daniel": 10,
    "Pablo": 7,
    "Juanito": 5,
    "Kevin": 8
}

print("\nImprimir Llaves\n")
for calificacion in diccionario_calificaciones:
    print(calificacion)

print("\nIterando Valores de las llaves\n")
for calificacion in diccionario_calificaciones:
    print(diccionario_calificaciones[calificacion])

print("\nImprimir Llaves\n")

for keys in diccionario_calificaciones.keys():
    print(keys)

print("\nImprimir Valores\n")

for values in diccionario_calificaciones.values():
    print(values)

print("\nImprimir Items\n")
for item in diccionario_calificaciones.items():
    print(item)
