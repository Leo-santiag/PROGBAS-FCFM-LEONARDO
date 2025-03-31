def agregar_producto(inventario, nombre, categoria, precio, cantidad):
    inventario[nombre] = {"categoría": categoria, "precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado al inventario.\n")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.\n")
    else:
        print(f"Producto '{nombre}' no encontrado.\n")

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        print(f"Información del producto '{nombre}':")
        print(inventario[nombre], "\n")
    else:
        print(f"Producto '{nombre}' no encontrado.\n")

def mostrar_productos_ordenados(inventario):
    print("Productos ordenados por precio de menor a mayor:")
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]["precio"])
    for producto, detalles in productos_ordenados:
        print(f"{producto} - Categoría: {detalles['categoría']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")
    print()

def menu():
    inventario = {}
    while True:
        print("Menú de opciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos ordenados por precio")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            agregar_producto(inventario, nombre, categoria, precio, cantidad)
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)
        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, nombre)
        elif opcion == "4":
            mostrar_productos_ordenados(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.\n")

menu()
