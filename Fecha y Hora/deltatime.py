import datetime

now = datetime.datetime.now()
print(now + datetime.timedelta(days=5, minutes=30, hours=5))

print(now + datetime.timedelta(days=-5))

print(now.date())
print(now.time())
