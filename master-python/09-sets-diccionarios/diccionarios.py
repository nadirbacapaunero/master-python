#array asociativos

#conjuntos de datos en formato clave: valor;

persona = {
    "nombre": "nadir",
    "apellidos": "Baca Paunero",
    "web": "nadir.com"
}

print(persona["apellidos"])

#lista con diccionarios

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@antonio.com"

    },
    {
        "nombre" : "Salvador",
        "email": "salvador@salvador.com"
    },
    {
        "nombre": "Luis",
        "email": "luis@luis.com"

    }
]

print(contactos[0]["nombre"])
print(contactos[2]["email"])

for contacto in contactos:
    print(f"Nombre del contacto {contacto['nombre']}")
    print(f"Email del contacto {contacto['email']}")
    print("-------------")
