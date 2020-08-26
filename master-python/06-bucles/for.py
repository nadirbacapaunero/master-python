### for ###


contador = 0

for contador in range (0, 10):
    print ("Voy por el " + str (contador))

## sumar todo lo que esta adentro de range ##

resultado = 0

for contador in range (0, 10):
    print ("Voy por el " + str (contador))


    resultado= resultado + contador
    print (f"el total es:   {resultado}")


    #ejemplo tablas de multiplicar

numero_usuario= int(input("ingresa numero"))


if numero_usuario < 1:
    numero_usuario= 1

print(f"# tabla de multiplicacion {numero_usuario}")  

for numero_tabla in range (1, 11):
    print( f"{numero_usuario} x {numero_tabla } = {numero_usuario* numero_tabla}")














