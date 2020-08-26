s1 = "Prueba"
s2 = "prueba"
s3 = "  prueba  "
s4 = "Hola Mundo"

#Capitalizar cadena de texto
print(s2.capitalize())

# Convertir en minuscula todos los caracteres de la cadena

print(s1.lower())

# Covertir en mayuscula todos los caracteres

print(s2.upper())

# Saca los espacios al comienzo y al final de la cadena de caracteres

print(s3.strip())

# Separa la cadena de caracteres segun lo que se le pase

print(s4.split(" "))

# Intercambia las mayusculas por las minusculas y vicversas

print(s1.swapcase())

# Le pone formato titulo a la cadena de caracteres

print(s2.title())

# Quita los espacion en blanco de la derecha

print(s3.rstrip())

# Quita los espacios en blanco de la izquierda
print(s3.lstrip())

# Justifica la cadena de texto a la derecha con una longitud de tantos caracteres como indica por parametro

print(s1.rjust(10))

# Justifica la cadena de texto a la izquierda con una longitud de tantos caracteres como indica por parametro

print(s1.ljust(10))

# Remplaza una cadena de texto por otra cadena de texto

print(s2.replace("r", "h"))

# centra la cadena de texto tomando por longitud la cantidad de caracteres pasados por parametros

print(s1.center(10))

# Completa la cadena de texto   con ceros tomando la longitud pasada por parametros

print(s1.zfill(10))

# devuelve el numero de ocurrencias de una subcadena de texto en toda la cadena o en un rango

print(s1.count("a"))

# Indica si la cadena de texto empieza con la pasada por para metro

print(s1.startswith("a"))

# Indica si la cadena de texto termina con la pasada por para metro

print(s1.endswith("a"))

# Busca la subcadena pasada por parametro

print(s1.find("ue"))

# similar al find solo que al no encontrar devuelve tipo ValueError
print(s1.index("a"))

# igual a find solo que devuelve la ultima ocurrencia

print(s1.rfind("ue"))

# igual a rfind solo que devuelve valueError al no encontrar

print(s1.rindex("a"))

# indica si todos los caracteres de la cadena de texto son decimales

print(s1.isdecimal())

# indica si todos los caracteres de la cadena de texto son digitos

print(s1.isdigit())

# Indica si todos los caracteres de la cadena de texto son minusculas

print(s1.islower())

# Indica si todos los caracteres de la cadena de texto son mayusculas

print(s1.isupper())

# Indica si las cadena de texto esta con mayusculas y minusculas al estilo titulo

print(s1.istitle())

# Indica si la cadena de texto son todos espacios

print(s1.isspace())

# Indica si la cadena de texto esta compuesta por todos caracteres alfabeticos

print(s1.isalpha())

# Indica si la cadena de texto esta compuesta por todos caracteres alfanumericos

print(s1.isalnum())
print("############")


a_list = ['1', '2', '3']

print('-'.join(a_list))
