import datetime

central_time = datetime.timezone(datetime.timedelta(hours=-6))

print(central_time)

pacific_time = datetime.timezone(datetime.timedelta(hours=-8))
print(pacific_time)

colombia_time = datetime.timezone(datetime.timedelta(hours=-5))
print(colombia_time)

eastern_time = datetime.timezone(datetime.timedelta(hours=-5))
print(eastern_time)

now = datetime.datetime.now(central_time)
print(now)


as_time_zone = now.astimezone(eastern_time)
print(as_time_zone)
