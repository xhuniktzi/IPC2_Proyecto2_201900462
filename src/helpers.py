from tkinter import Tk, Toplevel, Frame
from config import data, input_matrix_1, input_matrix_2, output_matrix


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

    # input_matrix_1.destroy()
    # input_matrix_2.destroy()
    # output_matrix.destroy()