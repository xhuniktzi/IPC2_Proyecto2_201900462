from tkinter import Tk, Menu, Toplevel, Label, Button
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from xml.etree import ElementTree as ET
from models import ListaEnlazada, Matriz
from helpers import define_geometry, search_matrix
from config import *
from binary_ops import union_matrix, intersec_matrix


def load_file():
    def parse_image(image: str):
        matrix_parse = []
        lines = image.strip().replace(' ', '').splitlines()
        for line in lines:
            matrix_parse.append([char for char in line])
        return matrix_parse

    filename = askopenfilename()
    xml_tree = ET.parse(filename)
    xml_root = xml_tree.getroot()
    for matrix in xml_root:
        name = matrix.find('nombre').text
        x_size = int(matrix.find('columnas').text)
        y_size = int(matrix.find('filas').text)
        new_matrix = Matriz(name, x_size, y_size)
        info_matrix = parse_image(matrix.find('imagen').text)

        y_count = 0
        while y_count < new_matrix.n:
            x_count = 0
            while x_count < new_matrix.m:
                value = info_matrix[y_count][x_count]
                new_matrix.insert(x_count, y_count, value)
                x_count = x_count + 1
            y_count = y_count + 1

        data.add_to_end(new_matrix)


def invoke_rotate_h():
    def execute_cmd():
        search_matrix(select_matrix.get()).print_matrix()
        search_matrix(select_matrix.get()).rotate_horizontal().print_matrix()

    rotate_h_window = Toplevel(window)

    data_geometry = define_geometry(rotate_h_window, 500, 50)
    rotate_h_window.geometry(data_geometry)

    rotate_h_window.resizable(0, 0)
    rotate_h_window.title('Rotar Horizontal')

    select_matrix_label = Label(rotate_h_window,
                                text='Selecciona una matriz: ')

    select_matrix_label.grid(row=0, column=0, padx=5, pady=5)

    list_matrix = list()
    count = 0
    while count < data.get_size():
        list_matrix.append(data.get_by_index(count).name)
        count = count + 1

    select_matrix = Combobox(rotate_h_window, width=24, state='readonly')
    select_matrix.grid(row=0, column=1, padx=5, pady=5)
    select_matrix['values'] = list_matrix

    submit_button = Button(rotate_h_window,
                           text="Rotar Horizontalmente",
                           command=execute_cmd)

    submit_button.grid(row=0, column=2, padx=5, pady=5)


def invoke_rotate_v():
    def execute_cmd():
        search_matrix(select_matrix.get()).print_matrix()
        search_matrix(select_matrix.get()).rotate_vertical().print_matrix()

    rotate_v_window = Toplevel(window)

    data_geometry = define_geometry(rotate_v_window, 500, 50)
    rotate_v_window.geometry(data_geometry)

    rotate_v_window.resizable(0, 0)
    rotate_v_window.title('Rotar Vertical')

    select_matrix_label = Label(rotate_v_window,
                                text='Selecciona una matriz: ')

    select_matrix_label.grid(row=0, column=0, padx=5, pady=5)

    list_matrix = list()
    count = 0
    while count < data.get_size():
        list_matrix.append(data.get_by_index(count).name)
        count = count + 1

    select_matrix = Combobox(rotate_v_window, width=24, state='readonly')
    select_matrix.grid(row=0, column=1, padx=5, pady=5)
    select_matrix['values'] = list_matrix

    submit_button = Button(rotate_v_window,
                           text="Rotar Verticalmente",
                           command=execute_cmd)

    submit_button.grid(row=0, column=2, padx=5, pady=5)


def invoke_transpose():
    def execute_cmd():
        search_matrix(select_matrix.get()).print_matrix()
        search_matrix(select_matrix.get()).transpose().print_matrix()

    transpose_window = Toplevel(window)

    data_geometry = define_geometry(transpose_window, 500, 50)
    transpose_window.geometry(data_geometry)

    transpose_window.resizable(0, 0)
    transpose_window.title('Transponer Imagen')

    select_matrix_label = Label(transpose_window,
                                text='Selecciona una matriz: ')

    select_matrix_label.grid(row=0, column=0, padx=5, pady=5)

    list_matrix = list()
    count = 0
    while count < data.get_size():
        list_matrix.append(data.get_by_index(count).name)
        count = count + 1

    select_matrix = Combobox(transpose_window, width=24, state='readonly')
    select_matrix.grid(row=0, column=1, padx=5, pady=5)
    select_matrix['values'] = list_matrix

    submit_button = Button(transpose_window,
                           text="Transponer",
                           command=execute_cmd)

    submit_button.grid(row=0, column=2, padx=5, pady=5)


def testing_union():
    matrix_2 = search_matrix('M2')
    matrix_5 = search_matrix('M5')

    matrix_2.print_matrix()
    matrix_5.print_matrix()

    union_matrix(matrix_5, matrix_2).print_matrix()


def testing_intersec():
    matrix_2 = search_matrix('M2')
    matrix_5 = search_matrix('M5')

    matrix_2.print_matrix()
    matrix_5.print_matrix()

    intersec_matrix(matrix_5, matrix_2).print_matrix()


if __name__ == '__main__':
    window.config(menu=menu_bar)

    data_geometry = define_geometry(window, 900, 500)
    window.geometry(data_geometry)

    window.resizable(0, 0)
    window.title('Proyecto 2 - IPC2')

    menu_bar.add_command(label='Cargar Archivo', command=load_file)

    op_unit_menu = Menu(menu_bar, tearoff=0)
    op_unit_menu.add_command(label='Rotar horizontalmente...',
                             command=invoke_rotate_h)
    op_unit_menu.add_command(label='Rotar verticalmente...',
                             command=invoke_rotate_v)
    op_unit_menu.add_command(label='Transponer imagen...',
                             command=invoke_transpose)
    op_unit_menu.add_command(label='Limpiar zona de una imagen...')
    op_unit_menu.add_command(label='Agregar linea horizontal...')
    op_unit_menu.add_command(label='Agregar linea vertical...')
    op_unit_menu.add_command(label='Agregar rectángulo...')
    op_unit_menu.add_command(label='Agregar triangulo rectángulo...')
    menu_bar.add_cascade(label='Operaciones unitarias', menu=op_unit_menu)

    op_bin_menu = Menu(menu_bar, tearoff=0)
    op_bin_menu.add_command(label='Union...', command=testing_union)
    op_bin_menu.add_command(label='Intersección...', command=testing_intersec)
    op_bin_menu.add_command(label='Diferencia...')
    op_bin_menu.add_command(label='Diferencia simétrica...')
    menu_bar.add_cascade(label='Operaciones binarias', menu=op_bin_menu)

    menu_bar.add_command(label='Reportes')

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='Acerca del autor...')
    help_menu.add_command(label='Acerca del programa...')
    menu_bar.add_cascade(label='Ayuda', menu=help_menu)

    window.mainloop()