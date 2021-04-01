from tkinter import Tk, Menu, Frame, Label, LEFT, RIGHT
from models import ListaEnlazada

window = Tk()
menu_bar = Menu(window)

input_matrix_1_label = Label(window, text='Matriz 1')
input_matrix_1_label.grid(row=0, column=0, padx=15)

input_matrix_1 = Frame(window)
input_matrix_1.grid(row=1, column=0, padx=15, pady=15)

input_matrix_2_label = Label(window, text='Matriz 2')
input_matrix_2_label.grid(row=0, column=1, padx=15)

input_matrix_2 = Frame(window)
input_matrix_2.grid(row=1, column=1, padx=15, pady=15)

output_matrix_label = Label(window, text='Matriz Resultado')
output_matrix_label.grid(row=0, column=2, padx=15)

output_matrix = Frame(window)
output_matrix.grid(row=1, column=2, padx=15, pady=15)

data = ListaEnlazada()

log_entrys = list()