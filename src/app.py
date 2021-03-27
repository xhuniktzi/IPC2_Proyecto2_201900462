from tkinter import Tk, Menu, Toplevel, Label, Button
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from models import ListaEnlazada, Matriz
from xml.etree import ElementTree as ET

window = Tk()
menu_bar = Menu(window)

data = ListaEnlazada()


# Aux: buscar matriz por nombre
def search_matrix(name: str):
    count = 0
    while count < data.get_size():
        if data.get_by_index(count).name == name:
            return data.get_by_index(count)
        count = count + 1

    return None


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
    current_matrix = None

    width = 500
    height = 50
    x_win = rotate_h_window.winfo_screenwidth() // 2 - width // 2
    y_win = rotate_h_window.winfo_screenheight() // 2 - height // 2
    data_geometry = '{}x{}+{}+{}'.format(width, height, x_win, y_win)
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


# def insert_dynamic():
#     info = StringVar()
#     label_test = Label(window, textvariable=info)
#     info.set('Información')
#     label_test.pack()

if __name__ == '__main__':
    window.config(menu=menu_bar)

    width = 900
    height = 500
    x_win = window.winfo_screenwidth() // 2 - width // 2
    y_win = window.winfo_screenheight() // 2 - height // 2
    data_geometry = '{}x{}+{}+{}'.format(width, height, x_win, y_win)
    window.geometry(data_geometry)

    window.resizable(0, 0)
    window.title('Proyecto 2 - IPC2')

    menu_bar.add_command(label='Cargar Archivo', command=load_file)

    op_unit_menu = Menu(menu_bar, tearoff=0)
    op_unit_menu.add_command(label='Rotar horizontalmente...',
                             command=invoke_rotate_h)
    op_unit_menu.add_command(label='Rotar verticalmente...')
    op_unit_menu.add_command(label='Transponer imagen...')
    op_unit_menu.add_command(label='Limpiar zona de una imagen...')
    op_unit_menu.add_command(label='Agregar linea horizontal...')
    op_unit_menu.add_command(label='Agregar linea vertical...')
    op_unit_menu.add_command(label='Agregar rectángulo...')
    op_unit_menu.add_command(label='Agregar triangulo rectángulo...')
    menu_bar.add_cascade(label='Operaciones unitarias', menu=op_unit_menu)

    op_bin_menu = Menu(menu_bar, tearoff=0)
    op_bin_menu.add_command(label='Union...')
    op_bin_menu.add_command(label='Intersección...')
    op_bin_menu.add_command(label='Diferencia...')
    op_bin_menu.add_command(label='Diferencia simétrica...')
    menu_bar.add_cascade(label='Operaciones binarias', menu=op_bin_menu)

    menu_bar.add_command(label='Reportes')

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='Acerca del autor...')
    help_menu.add_command(label='Acerca del programa...')
    menu_bar.add_cascade(label='Ayuda', menu=help_menu)

    window.mainloop()