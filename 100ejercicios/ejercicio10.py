path = "C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\"
name = "miarchivito"
ext = "txt"
# Profe no se porque al poner la / no puede dar acceso ero si son la \\
with open(path+name+"."+ext, 'r', encoding='utf-8') as miarchivito:
    contenido = miarchivito.read()
    print(contenido)


with open(path+name+"."+ext, 'w', encoding='utf-8') as miarchivito:
    miarchivito.write('Este es el nuevo contenido del archivo.\n')
    
with open(path+name+"."+ext, 'r', encoding='utf-8') as miarchivito:
    contenido = miarchivito.read()
    print(contenido)

with open(path+name+"."+ext, 'a', encoding='utf-8') as miarchivito:
    miarchivito.write('Esta es una línea añadida al archivo.\n')
with open(path+name+"."+ext, 'r', encoding='utf-8') as miarchivito:
    contenido = miarchivito.read()
    print(contenido)

with open(path+name+"."+ext, 'r', encoding='utf-8') as miarchivito:
    lineas = miarchivito.readlines()


lineas[0] = 'Esta es la línea modificada.\n'


with open(path+name+"."+ext,  'w', encoding='utf-8') as miarchivito:
    miarchivito.writelines(lineas)

miarchivito.close()