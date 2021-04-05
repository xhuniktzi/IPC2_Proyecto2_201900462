from models import ListaEnlazada, Matriz
from os import system, startfile
from datetime import datetime
from Excepts import InvalidRangeException, MatrixSizeException


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
        print('{}x{}'.format(self.m, self.n))
        size = self.row_list.get_size()
        while size > count:
            self.get_row(count).print_list()
            count = count + 1
        print()

    # Dibujar graphviz
    def render_graphviz(self):
        dot_filename = '{}{}{}_{}{}{}_graph_{}.dot'.format(
            datetime.now().second,
            datetime.now().minute,
            datetime.now().hour,
            datetime.now().day,
            datetime.now().month,
            datetime.now().year, self.name)
        dot_file = open(dot_filename, 'w+')
        dot_file.write('digraph G {')  # Begin file
        dot_file.write('label="Matriz: {}";'.format(self.name))
        dot_file.write('labelloc=t;')
        dot_file.write('graph [fontname="Verdana" compound=true rankdir=LR];')
        dot_file.write('node [shape=record fontname="Verdana"];')
        dot_file.write('subgraph cluster_0 {')  # Begin cluster rows
        dot_file.write('node [style=filled];')
        dot_file.write('label="Filas";')
        dot_file.write('color=blue;')

        row_count = 0
        while row_count < self.n:
            dot_file.write('f{} [label="Fila {}"];'.format(
                row_count, row_count + 1))
            row_count = row_count + 1

        dot_file.write('}')  # End cluster rows

        count_x = 0
        while count_x < self.m:
            count_y = 0
            while count_y < self.n:
                dot_file.write('e{x}_{y} [label="{x},{y} | {value}"];'.format(
                    x=count_x, y=count_y, value=self.get(count_x, count_y)))
                count_y = count_y + 1
            count_x = count_x + 1

        count_y = 0
        while count_y < self.n:
            dot_file.write('f{y} -> e0_{y};'.format(y=count_y))
            count_x = 0
            while count_x < self.m:
                if not count_x + 1 >= self.m:
                    dot_file.write('e{}_{} -> e{}_{};'.format(
                        count_x, count_y, count_x + 1, count_y))
                count_x = count_x + 1
            count_y = count_y + 1

        dot_file.write('}')  # End file
        dot_file.close()

        output_filename = '{}{}{}_{}{}{}_graph_{}.svg'.format(
            datetime.now().second,
            datetime.now().minute,
            datetime.now().hour,
            datetime.now().day,
            datetime.now().month,
            datetime.now().year, self.name)
        system('dot -Tsvg {} -o {}'.format(dot_filename, output_filename))

    # Definir Matriz
    def define(self, matrix: Matriz):
        self.row_list.clear()

        self.m = matrix.m
        self.n = matrix.n
        self.name = matrix.name

        count_rows = 0
        while self.n > count_rows:
            row = ListaEnlazada()

            count_cols = 0
            while self.m > count_cols:
                row.add_to_end(None)
                count_cols = count_cols + 1

            self.row_list.add_to_end(row)
            count_rows = count_rows + 1

        count_x = 0
        while count_x < self.m:
            count_y = 0
            while count_y < self.n:
                value = matrix.get(count_x, count_y)
                self.insert(count_x, count_y, value)
                count_y = count_y + 1
            count_x = count_x + 1
        # self.row_list = matrix.row_list

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

    # Transponer imagen
    def transpose(self):
        transpose_matrix = Matriz(self.name, self.n, self.m)
        count_x = 0
        while count_x < self.m:
            count_y = 0
            while count_y < self.n:
                value = self.get(count_x, count_y)
                transpose_matrix.insert(count_y, count_x, value)
                count_y = count_y + 1
            count_x = count_x + 1
        return transpose_matrix

    # Limpiar una zona
    def clear_zone(self, x_o: int, y_o: int, x_f: int, y_f: int):
        if (x_o > x_f) or (y_o > y_f):
            raise InvalidRangeException
        elif (x_o > self.m) or (y_o > self.n) or (x_f > self.m) or (y_f >
                                                                    self.n):
            raise MatrixSizeException
        else:
            clear_matrix = Matriz(self.name, self.m, self.n)
            clear_matrix.define(self)
            count_x = x_o
            while count_x <= x_f:
                count_y = y_o
                while count_y <= y_f:
                    clear_matrix.insert(count_x, count_y, '-')
                    count_y = count_y + 1
                count_x = count_x + 1
            return clear_matrix

    # Añadir Linea horizontal
    def add_horizontal_line(self, x: int, y: int, count: int):
        x_init = x
        x_end = x + (count - 1)
        if (x_end > self.m) or (count <= 0):
            raise InvalidRangeException
        else:
            horizontal_line_matrix = Matriz(self.name, self.m, self.n)
            horizontal_line_matrix.define(self)
            x_count = x_init
            while x_count <= x_end:
                horizontal_line_matrix.insert(x_count, y, '*')
                x_count = x_count + 1
            return horizontal_line_matrix

    # Añadir Linea Vertical
    def add_vertical_line(self, x: int, y: int, count: int):
        y_init = y
        y_end = y + (count - 1)
        if (y_end > self.m) or (count <= 0):
            raise InvalidRangeException
        else:
            vertical_line_matrix = Matriz(self.name, self.m, self.n)
            vertical_line_matrix.define(self)
            y_count = y_init
            while y_count <= y_end:
                vertical_line_matrix.insert(x, y_count, '*')
                y_count = y_count + 1
            return vertical_line_matrix