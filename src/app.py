from tkinter import Tk, Menu, Toplevel, Label, Button
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from xml.etree import ElementTree as ET
from datetime import datetime
from jinja2 import Environment, select_autoescape, PackageLoader
from os import startfile
from models import ListaEnlazada, Matriz
from helpers import define_geometry, search_matrix, clear_frames
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

        white_cells = 0
        black_cells = 0

        y_count = 0
        while y_count < new_matrix.n:
            x_count = 0
            while x_count < new_matrix.m:
                value = info_matrix[y_count][x_count]
                new_matrix.insert(x_count, y_count, value)
                if value == '*':
                    black_cells = black_cells + 1
                else:
                    white_cells = white_cells + 1
                x_count = x_count + 1
            y_count = y_count + 1

        log_str = '{} - {} - Espacios llenos: {} - Espacios en blanco: {}'.format(
            datetime.now(), name, black_cells, white_cells)
        reports.append(log_str)
        data.add_to_end(new_matrix)


def invoke_rotate_h():
    def execute_cmd():
        clear_frames()
        matrix_input = search_matrix(select_matrix.get())
        count_x = 0
        while count_x < matrix_input.m:
            count_y = 0
            while count_y < matrix_input.n:
                if matrix_input.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_1, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_1, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_output = matrix_input.rotate_horizontal()
        count_x = 0
        while count_x < matrix_output.m:
            count_y = 0
            while count_y < matrix_output.n:
                if matrix_output.get(count_x, count_y) == '*':
                    any_label = Label(output_matrix, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(output_matrix, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        log_str = '{} - Rotación Horizontal - Matriz: {}'.format(
            datetime.now(), matrix_input.name)
        reports.append(log_str)

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
        clear_frames()
        matrix_input = search_matrix(select_matrix.get())
        count_x = 0
        while count_x < matrix_input.m:
            count_y = 0
            while count_y < matrix_input.n:
                if matrix_input.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_1, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_1, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_output = matrix_input.rotate_vertical()
        count_x = 0
        while count_x < matrix_output.m:
            count_y = 0
            while count_y < matrix_output.n:
                if matrix_output.get(count_x, count_y) == '*':
                    any_label = Label(output_matrix, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(output_matrix, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        log_str = '{} - Rotación Vertical - Matriz: {}'.format(
            datetime.now(), matrix_input.name)
        reports.append(log_str)

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
        clear_frames()
        matrix_input = search_matrix(select_matrix.get())
        count_x = 0
        while count_x < matrix_input.m:
            count_y = 0
            while count_y < matrix_input.n:
                if matrix_input.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_1, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_1, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_output = matrix_input.transpose()
        count_x = 0
        while count_x < matrix_output.m:
            count_y = 0
            while count_y < matrix_output.n:
                if matrix_output.get(count_x, count_y) == '*':
                    any_label = Label(output_matrix, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(output_matrix, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        log_str = '{} - Transposición - Matriz: {}'.format(
            datetime.now(), matrix_input.name)
        reports.append(log_str)

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


def invoke_union():
    def execute_cmd():
        clear_frames()
        matrix_input_1 = search_matrix(select_matrix_1.get())
        count_x = 0
        while count_x < matrix_input_1.m:
            count_y = 0
            while count_y < matrix_input_1.n:
                if matrix_input_1.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_1, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_1, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_input_2 = search_matrix(select_matrix_2.get())
        count_x = 0
        while count_x < matrix_input_2.m:
            count_y = 0
            while count_y < matrix_input_2.n:
                if matrix_input_2.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_2, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_2, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_output = union_matrix(matrix_input_1, matrix_input_2)

        if matrix_output is None:
            log_str = '{} - Error: Matrices de tamaños distintos, Union - {} y {}'.format(
                datetime.now(), matrix_input_1.name, matrix_input_2.name)
            reports.append(log_str)
            message_str = 'Las matrices deben ser del mismo tamaño'
            showerror(union_window, message=message_str)
            return

        count_x = 0
        while count_x < matrix_output.m:
            count_y = 0
            while count_y < matrix_output.n:
                if matrix_output.get(count_x, count_y) == '*':
                    any_label = Label(output_matrix, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(output_matrix, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        log_str = '{} - Union - Matrices: {} y {}'.format(
            datetime.now(), matrix_input_1.name, matrix_input_2.name)
        reports.append(log_str)

    union_window = Toplevel(window)

    data_geometry = define_geometry(union_window, 500, 100)
    union_window.geometry(data_geometry)

    union_window.resizable(0, 0)
    union_window.title('Unir Imágenes')

    select_matrix_1_label = Label(union_window, text='Selecciona una matriz: ')
    select_matrix_1_label.grid(row=0, column=0, padx=5, pady=5)

    list_matrix = list()
    count = 0
    while count < data.get_size():
        list_matrix.append(data.get_by_index(count).name)
        count = count + 1

    select_matrix_1 = Combobox(union_window, width=24, state='readonly')
    select_matrix_1.grid(row=0, column=1, padx=5, pady=5)
    select_matrix_1['values'] = list_matrix

    select_matrix_2_label = Label(union_window, text='Selecciona una matriz: ')
    select_matrix_2_label.grid(row=1, column=0, padx=5, pady=5)

    select_matrix_2 = Combobox(union_window, width=24, state='readonly')
    select_matrix_2.grid(row=1, column=1, padx=5, pady=5)
    select_matrix_2['values'] = list_matrix

    submit_button = Button(union_window, text="Union", command=execute_cmd)

    submit_button.grid(row=1, column=2, padx=5, pady=5)


def invoke_intersec():
    def execute_cmd():
        clear_frames()
        matrix_input_1 = search_matrix(select_matrix_1.get())
        count_x = 0
        while count_x < matrix_input_1.m:
            count_y = 0
            while count_y < matrix_input_1.n:
                if matrix_input_1.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_1, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_1, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_input_2 = search_matrix(select_matrix_2.get())
        count_x = 0
        while count_x < matrix_input_2.m:
            count_y = 0
            while count_y < matrix_input_2.n:
                if matrix_input_2.get(count_x, count_y) == '*':
                    any_label = Label(input_matrix_2, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(input_matrix_2, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        matrix_output = intersec_matrix(matrix_input_1, matrix_input_2)

        if matrix_output is None:
            log_str = '{} - Error: Matrices de tamaños distintos, Intersección - {} y {}'.format(
                datetime.now(), matrix_input_1.name, matrix_input_2.name)
            reports.append(log_str)
            message_str = 'Las matrices deben ser del mismo tamaño'
            showerror(intersec_window, message=message_str)
            return

        count_x = 0
        while count_x < matrix_output.m:
            count_y = 0
            while count_y < matrix_output.n:
                if matrix_output.get(count_x, count_y) == '*':
                    any_label = Label(output_matrix, bg='black', text='*')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                else:
                    any_label = Label(output_matrix, text=' ')
                    any_label.config(width=2, height=1)
                    any_label.grid(column=count_x, row=count_y)
                count_y = count_y + 1
            count_x = count_x + 1

        log_str = '{} - Intersección - Matrices: {} y {}'.format(
            datetime.now(), matrix_input_1.name, matrix_input_2.name)
        reports.append(log_str)

    intersec_window = Toplevel(window)

    data_geometry = define_geometry(intersec_window, 500, 100)
    intersec_window.geometry(data_geometry)

    intersec_window.resizable(0, 0)
    intersec_window.title('Intersección de Imágenes')

    select_matrix_1_label = Label(intersec_window,
                                  text='Selecciona una matriz: ')
    select_matrix_1_label.grid(row=0, column=0, padx=5, pady=5)

    list_matrix = list()
    count = 0
    while count < data.get_size():
        list_matrix.append(data.get_by_index(count).name)
        count = count + 1

    select_matrix_1 = Combobox(intersec_window, width=24, state='readonly')
    select_matrix_1.grid(row=0, column=1, padx=5, pady=5)
    select_matrix_1['values'] = list_matrix

    select_matrix_2_label = Label(intersec_window,
                                  text='Selecciona una matriz: ')
    select_matrix_2_label.grid(row=1, column=0, padx=5, pady=5)

    select_matrix_2 = Combobox(intersec_window, width=24, state='readonly')
    select_matrix_2.grid(row=1, column=1, padx=5, pady=5)
    select_matrix_2['values'] = list_matrix

    submit_button = Button(intersec_window,
                           text="Intersección",
                           command=execute_cmd)

    submit_button.grid(row=1, column=2, padx=5, pady=5)


def print_reports():
    env = Environment(loader=PackageLoader('app', 'templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('reports.html')

    html_url = '{}{}{}_html_report.html'.format(datetime.now().day,
                                                datetime.now().month,
                                                datetime.now().year)
    html_file = open(html_url, 'w+')
    html_file.write(template.render(reports=reports))
    html_file.close()

    startfile(html_url)


def about_author():
    message_str = 'Xhunik Nikol Miguel Mutzutz \n 201900462'
    showinfo(window, message=message_str)


if __name__ == '__main__':
    window.config(menu=menu_bar)

    data_geometry = define_geometry(window, 900, 500)
    window.geometry(data_geometry)

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
    op_bin_menu.add_command(label='Union...', command=invoke_union)
    op_bin_menu.add_command(label='Intersección...', command=invoke_intersec)
    op_bin_menu.add_command(label='Diferencia...')
    op_bin_menu.add_command(label='Diferencia simétrica...')
    menu_bar.add_cascade(label='Operaciones binarias', menu=op_bin_menu)

    menu_bar.add_command(label='Reportes', command=print_reports)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='Acerca del autor...', command=about_author)
    help_menu.add_command(label='Acerca del programa...')
    menu_bar.add_cascade(label='Ayuda', menu=help_menu)

    window.mainloop()