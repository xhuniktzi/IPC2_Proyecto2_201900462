from tkinter import Tk, Menu

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

    menu_bar.add_command(label='Cargar Archivo')

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

    window.mainloop()