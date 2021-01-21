miLista = ["Maria", 5, True, 25.2]
miLista2 = ["Sandra", "Lucia"]

# Concatenar Listas
miLista3 = miLista+miLista2
print(miLista3)

# Repetir Lista
miLista4 = ["Jose", True, "Daniel", 3] * 3
print(miLista4)

# # Porción de lista
# miLista.append("Sandra")
# miLista.insert(2, "Daniel")

# miLista.extend(["Juan", "Camilo", "Nicole"])

# print(miLista)

# print(miLista.index("Daniel"))

# print("Pepe" in miLista)

# # Eliminacion de elementos

# miLista.remove("Maria")
# print(miLista)

# # Eliminar ultimo elemento de una lista
# miLista.pop()
# print(miLista)

#####################################
# UDEMY
#####################################

list([4, 3, 2, 3])
list("DANIEL")
nuevaLista = "Daniel es programador".split()
print(nuevaLista)

# Split cadena
comidaFavorita = "Pizza,Hamburguesa,Helado"
print(comidaFavorita.split(','))

# Join Cadena
comidaFavorita = ["Pizza", "Perro", "Hamburguesa", "Helado"]
print(", ".join(comidaFavorita))

print("Mi comida favorita es "+", ".join(comidaFavorita))
