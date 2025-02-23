def Inicio(nombre):    
    Menu = f"""
    Bienvenido a su agenda 
    Sr. {nombre}
    Elija una de las opciones 
    >>> (1) Acceder a lista de contactos
    >>> (2) Añadir nuevo contacto 
    >>> (3) Eliminar contacto
    >>> (4) Buscar contacto

    ----------------------------------------
    Si desea todas las funciones actualice a premium 
    #--Categorías y Etiquetas: Organizar contactos en categorías o asignar etiquetas (e.g., Familia, Trabajo, Amigos).
    #--Foto del Contacto: Añadir una fotografía para identificar visualmente a los contactos.
    #--Notas Adicionales: Añadir notas o comentarios adicionales sobre cada contacto.
    #--Recordatorios de Cumpleaños: Configurar recordatorios para cumpleaños y otros eventos importantes.
    #--Sincronización: Sincronizar contactos con otros dispositivos y servicios (e.g., Google Contacts, iCloud).
    #--Importar/Exportar: Importar y exportar contactos desde y hacia diferentes formatos (e.g., CSV, vCard).
    """
    print(Menu)
    return int(input())

path = "C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\"
name = "lista de contactos"
ext = "txt"

def imprimir_documento(rutaarchivo):
    try:
        with open(rutaarchivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{rutaarchivo}' no se encontró.")
    except IOError:
        print(f"Hubo un error al leer el archivo '{rutaarchivo}'.")
def borrar_linea_especifica(rutaarchivo, numero_linea):  
        with open(rutaarchivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        if 0 <= numero_linea < len(lineas):
            del lineas[numero_linea]

            
            with open(rutaarchivo, 'w', encoding='utf-8') as archivo:
                archivo.writelines(lineas)
            print(f"La línea {numero_linea + 1} ha sido borrada.")
        else:
            print(f"El número de línea {numero_linea + 1} no es válido.")
def eliminarcontacto(rutaarchivo):
    indice = int(input("ingrese el indice de lista del contacto que desea borrar"))
    borrar_linea_especifica(rutaarchivo, indice)
def agregarcontacto(rutaarchivo):
    nombre = input("Nombre: ")
    apellidopaterno = input("Apellido Paterno: ")
    apellidoMaterno = input("Apellido Materno: ")
    celular = input("Celular: ")

    with open(rutaarchivo, 'a', encoding='utf-8') as archivo:
        archivo.write(f'\n{nombre}     {apellidopaterno}     {apellidoMaterno}     {celular}')

def Registro():
    print("Ingrese su nombre:")
    return input()
def buscar_palabra_e_imprimir_linea(rutaarchivo, palabra):
        with open(rutaarchivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            lineas_encontradas = []
            for numero_linea, linea in enumerate(lineas, start=1):
                if palabra in linea:
                    lineas_encontradas.append((numero_linea, linea.strip()))
            if lineas_encontradas:
                print(f"La palabra '{palabra}' se encontró en las siguientes líneas:")
                for numero_linea, contenido in lineas_encontradas:
                    print(f"Línea {numero_linea}: {contenido}")
            else:
                print(f"La palabra '{palabra}' no se encontró en el archivo.")
nombre = Registro()
eleccion_1 = Inicio(nombre)

if eleccion_1 == 1:
    imprimir_documento(path + name + "." + ext)
elif eleccion_1 == 2:
    agregarcontacto(path + name + "." + ext)
elif eleccion_1==3:
    eliminarcontacto(path + name + "." + ext)
elif eleccion_1==4:
    palabra= input("Ingrese el nombre primero de su contacto ")
    buscar_palabra_e_imprimir_linea(path + name + "." + ext, palabra)




