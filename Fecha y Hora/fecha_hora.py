import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.minute)
print(now.hour)
print(now.month)

print(now.replace(minute=0))
print(now)
now = now.replace(minute=0, second=0)

tiempo_transcurrido = datetime.datetime.now()-now


print(tiempo_transcurrido)
print(tiempo_transcurrido.days)
print(tiempo_transcurrido.microseconds)
print(tiempo_transcurrido.seconds)
# Para obtener los minutos
print(round(tiempo_transcurrido.seconds/60))
