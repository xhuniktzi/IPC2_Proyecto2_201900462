from tkinter import Tk, Menu
from tkinter.filedialog import askopenfilename

root = Tk()
menu_bar = Menu(root)
root.config(menu=menu_bar)
root.title('Proyecto 2')

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Cargar...", command=askopenfilename)

menu_bar.add_cascade(label="Archivo", menu=file_menu)

root.mainloop()
