from tkinter import Tk, Toplevel, Frame, Label
from config import data, input_matrix_1, input_matrix_2, output_matrix
from models.Matriz import Matriz


def search_matrix(name: str):
    count = 0
    while count < data.get_size():
        if data.get_by_index(count).name == name:
            return data.get_by_index(count)
        count = count + 1
    return None


def define_geometry(element, width: int, height: int):
    x_win = element.winfo_screenwidth() // 2 - width // 2
    y_win = element.winfo_screenheight() // 2 - height // 2
    data_geometry = '{}x{}+{}+{}'.format(width, height, x_win, y_win)
    return data_geometry


def clear_frames():
    for widget in input_matrix_1.winfo_children():
        widget.destroy()

    for widget in input_matrix_2.winfo_children():
        widget.destroy()

    for widget in output_matrix.winfo_children():
        widget.destroy()


def render_grid(grid_element: Frame, matrix: Matriz):
    x_coords = 0
    while x_coords < matrix.m:
        coord_label = Label(grid_element, text=x_coords)
        coord_label.config(width=2, height=1)
        coord_label.grid(column=x_coords + 1, row=0)
        x_coords = x_coords + 1

    y_coords = 0
    while y_coords < matrix.n:
        coord_label = Label(grid_element, text=y_coords)
        coord_label.config(width=2, height=1)
        coord_label.grid(column=0, row=y_coords + 1)
        y_coords = y_coords + 1

    count_x = 0
    while count_x < matrix.m:
        count_y = 0
        while count_y < matrix.n:
            if matrix.get(count_x, count_y) == '*':
                any_label = Label(grid_element, bg='black', text='*')
                any_label.config(width=2, height=1)
                any_label.grid(column=count_x + 1, row=count_y + 1)
            else:
                any_label = Label(grid_element, text='-')
                any_label.config(width=2, height=1)
                any_label.grid(column=count_x + 1, row=count_y + 1)
            count_y = count_y + 1
        count_x = count_x + 1