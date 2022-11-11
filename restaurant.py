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

    # panel superior
    panel_superior = Frame(aplication, bd=1, relief=FLAT)
    panel_superior.pack(side=TOP)
    etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                            font=('Dosis', 58), bg='burlywood', width=27)
    etiqueta_titulo.grid(row=0, column=0)

    # panel izquierdo
    panel_izquierdo = Frame(aplication, bd=1, relief=FLAT)
    panel_superior.pack(side=LEFT)

    # panel coste
    panel_coste = Frame(panel_izquierdo, bd=1, relief=FLAT)
    panel_coste.pack(side=BOTTOM)

    # panel de menú
    panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4')
    panel_comidas.pack(side=LEFT)
    panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                               bd=1, relief=FLAT, fg='azure4')
    panel_bebidas.pack(side=LEFT)
    panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                               bd=1, relief=FLAT, fg='azure4')
    panel_postres.pack(side=LEFT)

    #panel derecha
    panel_derecha = Frame(aplication, bd=1, relief=FLAT)
    panel_derecha.pack(side=RIGHT)

    panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_calculadora.pack(side=TOP)
    panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_recibo.pack(side=TOP)
    panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_botones.pack(side=TOP)

    # Evitar que la ventana se cierre
    aplication.mainloop()
