import datetime


def verInstrucciones():
    print("Estas son las operaciones que puedes realizar: ")
    print("1. Ver la Hora")
    print("2. Ver la Fecha y Hora")
    print("3. Ver la hora en Nueva York")
    print("4. Ver la hora en San Francisco")
    print("5. Ver la hora en Tokyo")
    print("6. Ver la hora en Roma")
    print("7. Ver las instrucciones nuevamente")
    print("8. Salir")


def ver_hora(zona_horaria=5):
    if zona_horaria == 5:
        print("\nZona del este\n")
    elif zona_horaria == 8:
        print("Zona del pacifico")
    formato = "%I:%M:%S %p"
    timezone = datetime.timezone(datetime.timedelta(hours=-zona_horaria))
    if zona_horaria:
        hora_actual = datetime.datetime.now(timezone).time()
    else:
        hora_actual = datetime.datetime.now(timezone).time()

    hora_formateada = hora_actual.strftime(formato)
    print(hora_formateada)


def ver_hora_fecha():
    formato = "%A %B %d,%Y   %I:%M:%S %p"
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime(formato)
    print(fecha_formateada)


print("Bienvenido al Reloj Mundial")
verInstrucciones()


def verReloj():
    while True:
        operacion = int(input(": "))

        if operacion == 1:
            ver_hora()
        elif operacion == 2:
            ver_hora_fecha()
        elif operacion == 3:
            ver_hora(5)
        elif operacion == 4:
            ver_hora(8)
        elif operacion == 5:
            ver_hora(-9)
        elif operacion == 6:
            ver_hora(-1)
        elif operacion == 7:
            verInstrucciones()
        elif operacion == 8:
            print("Gracias por usar nuestro software. Te esperamos pronto.")
            break
        else:
            print("Operación desconocida. Intente de nuevo.")


verReloj()
