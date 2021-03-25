from tkinter import Tk, Menu
from tkinter.filedialog import askopenfilename
from models import ListaEnlazada, Matriz
from xml.etree import ElementTree as ET

data = ListaEnlazada()


def print_data():
    count = 0
    while count < data.get_size():
        data.get_by_index(count).print_matrix()
        count = count + 1


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
        x_size = int(matrix.find('filas').text)
        y_size = int(matrix.find('columnas').text)
        new_matrix = Matriz(name, x_size, y_size)
        info_matrix = parse_image(matrix.find('imagen').text)

        x_count = 0
        while x_count < new_matrix.m:
            y_count = 0
            while y_count < new_matrix.n:
                value = info_matrix[x_count][y_count]
                new_matrix.insert(x_count, y_count, value)
                y_count = y_count + 1
            x_count = x_count + 1

        data.add_to_end(new_matrix)


if __name__ == '__main__':
    window = Tk()
    menu_bar = Menu(window)
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
    op_unit_menu.add_command(label='Rotar horizontalmente...')
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

    menu_bar.add_command(label='Imprimir matrices (testing)',
                         command=print_data)

    window.mainloop()