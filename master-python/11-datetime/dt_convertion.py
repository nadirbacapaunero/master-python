import datetime

date_and_time = datetime.datetime(2019, 4, 30, 11, 25, 30)

# la funcion strftime crea un string  a partir de un objeto datatime
print(date_and_time.strftime('%Y-%m-%d'))

print(date_and_time.strftime('%Y-%m-%d %H:%M:%S'))

print(date_and_time.strftime('%Y/%m/%d'))

print(date_and_time.strftime('%Y-%m-%d T%H:%M:%S'))


# la funcion strptime crea un objeto datetime a partir de un string

print(datetime.datetime.strptime('2019-01-10', '%Y-%m-%d'))


print(datetime.datetime.strptime('2019-01-10 11:30:25', '%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.strptime('2019-01-10 T11:30:25', '%Y-%m-%d T%H:%M:%S'))


