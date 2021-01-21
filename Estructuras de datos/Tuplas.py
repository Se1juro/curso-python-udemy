# Todas las estructuras de datos en python son mutables, es decir que pueden modificarse a nuestro antojo.
# Excepto las tuplas, son una estructura de datos inmutables, parecidas a las listas.
# Lo que destaca a las tuplas son las comas, no son necesarios los parentesis, pero se usan para identificar una tupla
tupla_1 = (1, 2, 3, 4)
print(tupla_1)

tupla_2 = 1, 2, 3, 4
print(tupla_2)

# Esto no es posible, ya que tomaria tupla 3 como un entero
tupla_3 = (1)
print(tupla_3)

tupla_3 = 1,
print(tupla_3)

# del tupla_1[0] No podemos eliminar un elemento de una tupla

tupla_4 = (1, "Esto es una cadena", [0, 1, 2])
print(tupla_4)

# tupla_4[0] = 2 Tampoco podemos alterar el valor de un elemento de una tupla

# Modificar la lista dentro de la tupla si es posible
tupla_4[2][2] = 3
print(tupla_4)
