def merge_sort(arr):
    #Cuenta el arreglo si es mayor a uno 
    if len(arr) > 1:
        #Divide el arreglo en dos partes
        mitad = len(arr) // 2
        #crea dos arreglos separados y los asigna a L y R usa la particion :
        L = arr[:mitad]
        R = arr[mitad:]
        #utiliza recursividad
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    else:
        return arr
arr =  []
# Solicitar al usuario una lista de números
entrada = input("Introduce una lista de números separados por comas: ")
#el metodo split separa elemento de una caden por el argumento que le pases
arr = [float(num) for num in entrada.split(",")]
arrOrg = arr
print("Array original",arrOrg)

merge_sort(arr)

print("Array ordenado:", arr)