def procesar_texto(cadena):
    palabras = cadena.split()  # Dividir el texto en palabras
    dic = {palabra: palabras.count(palabra) for palabra in set(palabras)}  # Contar cada palabra
    palabra_mas_repetida = max(dic, key=dic.get)  # Obtener la palabra más repetida
    return palabras, dic, len(palabras), set(palabras), (palabra_mas_repetida, dic[palabra_mas_repetida])


cadena = "Queridos camaradas, soldados, marineros y trabajadores: me siento feliz al saludarlos en nombre de la victoriosa revolución rusa; de saludar en vosotros a la vanguardia del ejército proletario internacional. Ya no está lejos la hora en que, al llamamiento de nuestro camarada Karl Liebkchnet, el pueblo volverá sus armas contra los capitalistas que lo explotan. La revolución rusa, hecha por vosotros, ha abierto una nueva era. ¡Viva la revolución socialista mundial!"

# Ejecución
palabras, dic, total_palabras, palabras_unicas, palabra_repetida = procesar_texto(cadena)
print(palabras)  # Lista de palabras
print(dic)  # Diccionario con palabras y frecuencias
print(total_palabras)  # Total de palabras
print(palabras_unicas)  # Palabras únicas
print(palabra_repetida)  # Palabra más repetida y su frecuencia