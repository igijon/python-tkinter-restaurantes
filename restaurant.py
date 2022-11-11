from tkinter import *


def init():
    # Iniciar tkinter
    aplication = Tk()
    # tamaño de la ventana
    aplication.geometry('1020x630+0+0')

    # evitar maximizar
    aplication.resizable(0, 0) # no se puede modificar en ningún eje

    # Título de la ventana
    aplication.title('Mi restaurante - Sistema de facturación')

    # Color de fondo de la ventana. También permite RGB
    aplication.config(bg='burlywood')
    # Evitar que la ventana se cierre
    aplication.mainloop()
