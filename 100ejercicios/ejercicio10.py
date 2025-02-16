
with open('C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\miarchivito.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)


with open('C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\miarchivito.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('Este es el nuevo contenido del archivo.\n')

with open('C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\miarchivito.txt', 'a', encoding='utf-8') as archivo:
    archivo.write('Esta es una línea añadida al archivo.\n')
with open('miarchivito.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()


lineas[0] = 'Esta es la línea modificada.\n'


with open('C:\\Users\\santi\\OneDrive\\Documentos\\GitHub\\PROGBAS-FCFM-LEONARDO\\100ejercicios\\miarchivito.txt', 'w', encoding='utf-8') as archivo:
    archivo.writelines(lineas)

