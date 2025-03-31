def agregar_contacto(agenda, nombre, numero, correo):
    contacto = (nombre.strip().capitalize(), numero.strip(), correo.strip().lower())
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado.\n")

def buscar_contacto(agenda, nombre):
    nombre_busqueda = nombre.strip().capitalize()
    encontrados = [contacto for contacto in agenda if contacto[0] == nombre_busqueda]
    
    if encontrados:
        print(f"Detalles de contacto con nombre '{nombre_busqueda}':")
        for contacto in encontrados:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
        print()
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre_busqueda}'.\n")

def listar_contactos(agenda):
    print("Contactos ordenados alfabéticamente:")
    contactos_ordenados = sorted(agenda, key=lambda contacto: contacto[0])
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
    print()

# Ejemplo de uso
agenda = []

# Agregar contactos
agregar_contacto(agenda, " Ana ", "123456789", "ana@example.com")
agregar_contacto(agenda, " Juan ", "987654321", "juan@example.com")

# Buscar un contacto
buscar_contacto(agenda, " ana ")

# Listar contactos en orden alfabético
listar_contactos(agenda)