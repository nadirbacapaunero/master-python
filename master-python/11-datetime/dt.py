import datetime

# date objects
# El dia 30 de Abril del 2019.

date = datetime.date(2019, 4, 30)

#Atributo año de la fecha
print(date.year)

#Atributo mes de la fecha
print(date.month)

#Atributo del dia de la fecha
print(date.day)

# devuelve el dia de la semana el lunes es el cero y el domingo es el 6

print(date.weekday())

# devuelve el dia de la semana el lunes es el uno y el domingo es el 7

print(date.isoweekday())

#devuleve una tupla con tres elementos año, numero de la semana, dia de la semana
print(date.isocalendar())

# devuelve la fecha como un string en el formato 'YYYY-MM-DD'

print(date.isoformat())

# fecha minima

date_min = datetime.date.min
print(date_min)

# fecha maxima

date_max = datetime.date.max

print(date_max)

# el dia de hoy

today = datetime.date.today()
print(today)

# El dia de ayer
yesterday = today - datetime.timedelta(seconds=86900)
print('##############')
print(yesterday)

# datetime objects

# el dia 10 de octubre de 2019 a las 9:15:30

date_and_time = datetime.datetime(2019, 10, 10, 9, 15, 30)
print(date_and_time)

#atributo año de la fecha y hora
date_and_time.year
print(date_and_time.year)

#atributo mes de la fecha y hora
date_and_time.month
print(date_and_time.month)

# atributo hora de la fecha y hora

date_and_time.hour
print(date_and_time.hour)

# atributo de minutos de la fecha y hora
date_and_time.minute
print(date_and_time.minute)

# atributo segundos de la fecha  y hora

date_and_time.second
print(date_and_time.second)

# atributo micro segundo de la fecha y hora

date_and_time.microsecond
print(date_and_time.microsecond)

# obtener un objeto date a partir del objeto datetime

date_and_time.date()

# la fecha y hora actual 8local)
now = datetime.datetime.now()

print(now)

# la fecha y hora actual en UTC (coordinated universal time)

utcnow = datetime.datetime.utcnow()

print(utcnow)

# object time
# la hora 10:20:35

time = datetime.time(10, 20, 35)

print(time)

# atributo hora de la hora
time.hour
# atributo minuto de la hora

time.minute

# atributo segundos de la hora

time.second
# atributo microsegundo de la hora

time.microsecond

# hora minima
time_min = datetime.time.min

# hora maxima

time_max = datetime.time.max







