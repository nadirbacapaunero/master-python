#tipos de datos que pueden tener una variable

nada = None
cadena ="Hola soy Nadir "
entero = 99
flotante = 4.2
booleano = True
lista = [10, 52, 85, 921]
listaString = [44, "nadircho", 25, "cuarenta"]
tuplaNoCambia =("master", "en","Python")
#los diccionarios no cambian clave y valor
diccionario = {
    "nombre": "Nadir",
    "apellido": "baca Paunero",
    "curso": "master en Python"
}
rango = range(9)
dato_byte = b"probando"

#no tiene nada la variable

print(nada)
print(cadena)
print (entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)
#mostrar tipo de dato

print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

# como cambir un numero a string para concatenar
texto  = 'Hola soy Nadir' 
numerito = str(774)
print(texto + " " + numerito)

numerito= int(774)

print(type(numerito)

numerito = float(774)

print(type(numerito))

