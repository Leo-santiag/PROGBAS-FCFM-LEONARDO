print(" Implementar estructuras de datos basicas: pila, cola y lista enlazada.")
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def ver_cima(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)


pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila.desapilar())  
print(pila.ver_cima())  
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        return self.items.pop()

    def ver_frente(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)


cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.desencolar())  
print(cola.ver_frente())  
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
            previo = actual
            actual = actual.siguiente
        if actual is None:
            return
        if previo is None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print(None)


lista = ListaEnlazada()
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_inicio(0)
lista.mostrar_lista()  
lista.eliminar(1)
lista.mostrar_lista() 
