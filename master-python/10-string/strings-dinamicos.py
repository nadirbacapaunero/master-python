"""
 coding utf-8
"""

name = "Agustin"
"Hola %s" % name
"El numero es %d" % 5
"El numero es %2d" % 5
"El decimal es %f" % 6.5
"El decimal es %.2f" % 6.5
"Hola %(name)s" % {'name' : name}

"Hola {}".format(name)
"La suma de 1 +2 es {0}".format(1 +2)

' '.join(["Hola", name])
', '.join(["1", "2", "3", "4"])

a_string = 'Hola Mundo Python!'
nuevoString = a_string[-7:]

print(nuevoString)
