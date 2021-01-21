# Los diccionarios no tienen orden

diccionario_calificaciones = {
    "Daniel": {
        "Calificacion": 9,
        "Apellido": "Morales",
        "Grado": 9
    },
    "Pablo": 7,
    "Juanito": 5,
    "Kevin": 8
}

print(diccionario_calificaciones)
print(diccionario_calificaciones['Daniel'])

diccionario_calificaciones['Pablo'] = "Ochenta"
print(diccionario_calificaciones)

# Es un metodo verboso que puede ocasionar errores, así que no es muy usado
diccionario_raro = dict(
    [["Pepe", "El pepe"], ["Juanito", "Culo"], ["María", 4]])
print(diccionario_raro)
