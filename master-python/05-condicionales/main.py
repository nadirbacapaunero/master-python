"""
# condicionales
Si se cumple esta condicion 
     se ejecutaran estas instrucciones

     if condicion
        instrucciones
    else
        otras condiciones

  operadores de comparacion < > != <=  >=



print("######## ejemplo1####")
#color= "rojo"
#color= input("adivina cual es mi color favorito?")
if color== "rojo":
    print("el color es rojo")
else:
    print("el color NO es correcto!!")


#ejemplo 2

#year= int (input("En que año estamos?"))

if year >= 2021:
    print("estamos en 2021 en adelante")
else:
    print("es un año anterior  a 2021")  

#ejemplo 3
nombre= "nadir"
ciudad="Bariloche"
continente= "Africano"
edad= 32
mayor_edad= 18


if edad >= mayor_edad:
     print(f"{nombre} es mayor de edad!!")

     if continente != "America":
         print("El usuario no es americano")
     else:
        print(f"Es americano y de  {ciudad}")

else:
     print(f"{nombre} no es mayor de edad")        



"""

#ejemplo4

dia= int (input(" Que numero de dia es?"))

if dia == 1:
    print("Es lunes ")
elif dia == 2:
    print("es martes")
elif dia== 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana")