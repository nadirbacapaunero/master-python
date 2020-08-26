"""
1 Programa con una lista de 8 elementos
Recorrer las lista y mostrarla
Ordenarla y mostrarla
Mostrar su longitud
Buscar algun elemento ("que el usuario ingreso por teclado")
"""

#Crear lista

numeros = [13,64, 73, 21, 7, 91, 63]

#recorrer y mostrar
"""
for numero in numeros:
    print(numero)
"""
#crear funcion que recorra lista y devuelva string

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += " \n"

    return resultado


print(mostrarLista(numeros))

#ordenar y mostrar

numeros.sort()
print(mostrarLista(numeros))

#mostrar su longitud

print(len(numeros))

#mostrar elementos que el usuario pida por teclado

busqueda = int(input("introduce un numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int (input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"### Buscar en la lista el numero {busqueda} ###")   

search = numeros.index(busqueda)
print(f"El numero busquedo existe en la lista, es el indice {search}")