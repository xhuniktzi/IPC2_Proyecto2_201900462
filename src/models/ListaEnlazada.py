from models import Nodo


class ListaEnlazada:
    def __init__(self):
        self.head = None

    # Ver si esta vacío
    def is_void(self):
        return self.head == None

    # Insertar al inicio
    def add_to_head(self, data):
        self.head = Nodo(self.head, data)

    # Insertar al final
    def add_to_end(self, data):
        if self.is_void():
            self.head = Nodo(None, data)
            return
        node = self.head
        while node.next != None:
            node = node.next
        node.next = Nodo(None, data)

    # Devuelve el tamaño de la lista
    def get_size(self):
        count = 0
        node = self.head
        while node != None:
            node = node.next
            count = count + 1
        return count

    # Devuelve el primer elemento
    def get_first(self):
        if not self.is_void():
            return self.head.data
        else:
            return None

    # Devuelve el ultimo elemento
    def get_last(self):
        if self.is_void():
            return None
        node = self.head
        while node.next != None:
            node = node.next
        return node.data

    # Devuelve el dato en base al indice
    def get_by_index(self, index: int):
        count = 0
        node = self.head
        while node != None:
            if index == count:
                return node.data
            count = count + 1
            node = node.next
        return None

    # Añade un elemento en el indice
    def set_by_index(self, index: int, data):
        count = 0
        node = self.head
        while node != None:
            if index == count:
                node.data = data
                return
            count = count + 1
            node = node.next
        return

    # Elimina el primer elemento de la lista
    def delete_first(self):
        if not self.is_void():
            self.head = self.head.next

    # Elimina el ultimo elemento de la lista
    def delete_last(self):
        if not self.is_void():
            node = self.head
            prev = None
            while node.next != None:
                prev = node
                node = node.next
            if self.get_size() == 1:
                self.head = None
            else:
                prev.next = None

    # Eliminar indicando el indice
    def delete_by_index(self, index: int):
        if index == 0:
            self.delete_first()
            return
        count = 0
        node = self.head
        prev = None
        while node != None:
            if index == count:
                prev.next = node.next
            prev = node
            node = node.next
            count = count + 1

    # Vaciar lista enlazada
    def clear(self):
        self.head = None

    # Imprimir Lista
    def print_list(self):
        if not self.is_void():
            node = self.head
            while node != None:
                print('{}'.format(node.data), end=' -> ')
                node = node.next
            print()
        else:
            print('is void')
