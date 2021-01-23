import datetime

# La diferencia con now es que a now se le puede pasar una zona horaria como argumento.
today = datetime.datetime.today()

print(today)

print(datetime.time())

fecha_hoy = datetime.datetime.combine(
    datetime.datetime.today(), datetime.time())
print(fecha_hoy)
