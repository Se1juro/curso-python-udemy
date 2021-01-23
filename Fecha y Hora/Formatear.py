import datetime

now = datetime.datetime.now()
# Genera una cadena a partir de una hora o fecha
print(now.strftime("%B %d, %Y %H:%M:%S"))

# Generar una fecha a partir de una cadena
fecha_cadena = "06/02/2017"
fecha_formateada = datetime.datetime.strptime(fecha_cadena, "%d/%m/%Y")
print(fecha_formateada)
