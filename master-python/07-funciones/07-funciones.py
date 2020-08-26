"""
FUNCIONES


def nombreDeMiFuncion(mi_parametro):
    # BLOQUE DE CODIGO  
    print("mi funcion hace esto...")


#llamo a la funcion

##nombreDeMiFuncion()    

## PARAMETROS 
def mostrarTuNombre(nombre):
    print(f"Tu nombre es {nombre} ")
nombre= input("introduce tu nombre")
mostrarTuNombre(nombre)
#mostrarTuNombre("nadir")

###

def tabla (numero):
    print(f"tabla de multiplicar del numero: {numero}")
     
     for contador in range (11):
         operacion= numero*contador
         print(f"{numero} x {contador} = {operacion}")

     print("\n")    

tabla(3)


#parametros opcionales

def getEmpleado(nombre, dni= None):
    print("empleado")
    print(f"nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")
    
getEmpleado("nadir", 303494)        


def calculadora(numero1, numero2, basicas= False):
    suma= numero1 + numero2
    resta= numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena =""

    cadena +="Suma. " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacon: "+ str(multi)
    cadena += "\n"
    cadena += "division: " + str(division)
     
    return cadena

print(calculadora(5, 4))   
"""

# funcion LAMBDA            pequeña funcion

dime_el_year= lambda year: f"El año es {year}"

print(dime_el_year(2934))