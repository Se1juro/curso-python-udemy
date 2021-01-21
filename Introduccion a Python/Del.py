vocales = "aeiou"
lista_vocales = list(vocales)
variable_basura = "Hola jeje"

del variable_basura

del lista_vocales[0]
del lista_vocales[-1]
print(lista_vocales)

# del vocales[0] los strings son inmutables, quiere decir que intentas romper una cadena, esta ya no es la misma. No podemos modificar una cadena sin tener que crear una nueva
# La forma sencilla de eliminar algo de una cadena seria volverla una lista, hacerle sus modificaciones y luego volverla una cadena de nuevo
