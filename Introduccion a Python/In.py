vocales = "aeiou"
lista_vocales = list(vocales)
print("a" in vocales)
print("a" in lista_vocales)

if "a" in vocales:
    print("La A hace parte de las vocales")

if "z" not in vocales:
    print("Z no es una vocal")
