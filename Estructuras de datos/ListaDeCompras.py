run = True
lista_compras = list([])
print("LISTA DE COMPRAS\n")

while run:
    def listarProductos():
        print("===================")
        print("LISTA DE PRODUCTOS")
        print("===================")
        for producto in lista_compras:
            print(str(lista_compras.index(producto))+". "+producto.capitalize())
        print("===================")

    print("Opciones\n")
    print("1. Ver Lista")
    print("2. Agregar Producto")
    print("3. Eliminar Producto")
    print("4. Salir")

    try:
        opcion_lista = int(input("Elija su opción: "))
    except ValueError:
        print("Elija una opción correcta")
    else:
        print()
        if opcion_lista == 1:
            listarProductos()
        elif opcion_lista == 2:
            print()
            nuevo_producto = input("Ingrese el nuevo producto: ")
            lista_compras.append(nuevo_producto)
            print("Articulo agregado")
            print()
        elif opcion_lista == 3:
            print()
            listarProductos()
            try:
                indice_producto = int(
                    input("Ingrese el número del producto que quiere eliminar: "))
            except ValueError:
                print("No se pudo eliminar el producto, ingresa un indice correcto")
            else:
                try:
                    del lista_compras[indice_producto]
                except IndexError:
                    print("No se encontro el indice, intente de nuevo")
                else:
                    print("Articulo eliminado")
                    print()
        elif opcion_lista == 4:
            run = False
    print()
