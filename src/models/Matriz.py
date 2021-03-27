from models import ListaEnlazada, Matriz
from os import system, startfile


class Matriz:
    def __init__(self, name: str, m: int, n: int):
        self.name = name
        self.m = m
        self.n = n
        self.row_list = ListaEnlazada()

        count_rows = 0
        while self.n > count_rows:
            row = ListaEnlazada()

            count_cols = 0
            while self.m > count_cols:
                row.add_to_end(None)
                count_cols = count_cols + 1

            self.row_list.add_to_end(row)
            count_rows = count_rows + 1

    # Obtener fila
    def get_row(self, y: int):
        return self.row_list.get_by_index(y)

    # Insertar fila
    def set_row(self, y: int, row: ListaEnlazada):
        act_row = self.get_row(y)
        count = 0
        while count < self.m:
            act_row.set_by_index(count, row.get_by_index(count))
            count = count + 1

    # Insertar en un indice
    def insert(self, x: int, y: int, data):
        row = self.get_row(y)
        row.set_by_index(x, data)

    # Obtener un indice
    def get(self, x: int, y: int):
        row = self.get_row(y)
        return row.get_by_index(x)

    # Imprimir matriz
    def print_matrix(self):
        count = 0
        print(self.name)
        size = self.row_list.get_size()
        while size > count:
            self.get_row(count).print_list()
            count = count + 1
        print()

    # Obtener columna
    def get_column(self, x: int):
        count = 0
        column = ListaEnlazada()
        while count < self.n:
            column.add_to_end(self.get(x, count))
            count = count + 1
        return column

    # Insertar columna
    def set_column(self, x: int, column: ListaEnlazada):
        count = 0
        while count < self.n:
            value = column.get_by_index(count)
            self.insert(x, count, value)
            count = count + 1

    # Rotar horizontalmente
    def rotate_horizontal(self):
        rotate_matrix = Matriz(self.name, self.m, self.n)
        count_y = 0
        aux_count_y = self.n - 1
        while count_y < self.n:
            act_row = self.get_row(count_y)
            rotate_matrix.set_row(aux_count_y, act_row)
            count_y = count_y + 1
            aux_count_y = aux_count_y - 1
        return rotate_matrix

    # Rotar vertical
    def rotate_vertical(self):
        rotate_matrix = Matriz(self.name, self.m, self.n)
        count_x = 0
        aux_count_x = self.m - 1
        while count_x < self.m:
            act_column = self.get_column(count_x)
            rotate_matrix.set_column(aux_count_x, act_column)
            count_x = count_x + 1
            aux_count_x = aux_count_x - 1

        return rotate_matrix