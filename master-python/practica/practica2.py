"""
ejercicio2 

escribir un script que nos muestro por pantalla
todos los numeros pares del 1 al 120

agregar si es par o impar

"""



contador = 1

for contador in range (1, 121):
    if contador%2 == 0:

        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")
