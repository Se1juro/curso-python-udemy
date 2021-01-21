# Agenda telefonica que permitira guardar numero de contacto y su numero telefonico
# Podemos añadir contactos, borrar contactos, ver todos los contactos, ver un solo contacto a la vez y actualizar contactos
listaContactos = dict()


def imprimirOperacion(nombre_operacion):
    print()
    print("-----------AGENDA TELEFONICA-----------")
    print(nombre_operacion)
    print("---------------------------------------")
    print()


def addContact(nombre, telefono):
    print()
    listaContactos[nombre] = telefono
    imprimirOperacion("Contacto Agregado.")


def showContacts():
    print()
    print("==================")
    print("LISTA DE CONTACTOS")
    print("==================")
    if len(listaContactos) == 0:
        print("No tienes contactos")
    else:
        for contacto in listaContactos:
            print(contacto+" - "+str(listaContactos[contacto]))
    print("==================")
    print()


def searchContact(nombre):
    imprimirOperacion(nombre + " - "+listaContactos[nombre])


def actualizarContacto(nombre):
    print()
    numeroTelefono = input("Ingrese el nuevo numero telefonico: ")
    listaContactos.update({nombre: numeroTelefono})
    print(nombre + " - "+str(listaContactos[nombre]))
    print()


def eliminarContacto(nombre):
    print()
    del listaContactos[nombre]
    print()


while True:
    print("----Lista de contactos----")
    print("Selecciona una opción")
    print("1. Ver contactos")
    print("2. Buscar un contacto")
    print("3. Agregar contacto")
    print("4. Actualizar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

    try:
        opcion = int(input(": "))
    except ValueError:
        imprimirOperacion("Seleccione una opción valida.")
    else:
        if opcion == 1:
            showContacts()
        if opcion == 2:
            print()
            nombre = input("Ingrese el nombre del contacto: ")
            try:
                searchContact(nombre.capitalize())
            except KeyError:
                imprimirOperacion(
                    "No se encontro el contacto en tu lista.")
        if opcion == 3:
            print()
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el telefono del contacto: ")
            addContact(nombre.capitalize(), telefono)
        if opcion == 4:
            print()
            nombre = input("Ingrese el nombre del contacto: ")
            try:
                actualizarContacto(nombre.capitalize())
            except TypeError:
                print("Ingrese un nombre correcto.")
            else:
                imprimirOperacion("Contacto Actualizado")
        if opcion == 5:
            print()
            nombre = input("Ingrese el nombre del contacto: ")
            try:
                eliminarContacto(nombre)
            except KeyError:
                print("No se encontro el contacto que desea eliminar.")
                print()
            else:
                imprimirOperacion("Contacto Eliminado")
        if opcion == 6:
            imprimirOperacion(
                "Gracias por utilizar nuestro software, hasta luego.")
            break
