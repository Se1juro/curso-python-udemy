dias_semana = {
    "Lunes": 9,
    "Martes": 10,
    "Miercoles": 11
}

print(dias_semana)

# Añadir elemento a un diccionario
dias_semana["Jueves"] = 12
print(dias_semana)

# Borrar elemento de un diccionario
del dias_semana['Lunes']
print(dias_semana)

# Actualizar Elemento
dias_semana.update({"Viernes": 13, "Sabado": 14})
print(dias_semana)

dias_semana.update({"Sabado": 15, "Domingo": 16})
print(dias_semana)
