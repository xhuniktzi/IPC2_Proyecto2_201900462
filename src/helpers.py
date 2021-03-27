from tkinter import Tk, Toplevel
from config import data


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