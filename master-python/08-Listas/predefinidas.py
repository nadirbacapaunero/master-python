cantantes = [" 2pac", "Drake", "Bad Bunny", "Julio iglesias"]

numeros = [1, 2, 5, 8, 3,  4,]

#ordenar listas

numeros.sort()
print(numeros)

#añadir elementos

cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)


#eliminar elemetos

cantantes.pop(1)

cantantes.remove("Bad Bunny")
print(cantantes)



#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)


# Buscar dentro de una lista

print("Drake" in cantantes)

#contar elementos

print(len(cantantes))

# cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice 
print(cantantes.index("Drake"))

#Unir listas

cantantes.extend(numeros)

print(cantantes)