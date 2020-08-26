"""

    Listas  



peliculas= ["batman", "superman", "el señor de los anillos"]
cantantes= list(('2pac', 'drake', 'jenifer lopez'))
years= list((range(2020, 2045)))
print(peliculas)
print(cantantes)
print (years)


"""

#listas multidimensionales

contactos = [
    [ "antonio", "antonio@antonio.com"],

    ["luis", "luis@luis.com"],

    ["salvador", "salvardor@salvador.com"]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else :  
            print("Email: " + elemento)  
    
    print("\n")  


# print(contactos[2][1])