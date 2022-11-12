from tkinter import *


def init():

    # crear aplicación
    aplication = new_application()

    # crear paneles
    panel_superior, panel_izquierdo, panel_coste, panel_comidas, panel_bebidas, panel_postres, panel_derecha, \
    panel_calculadora, panel_recibo, panel_botones = new_panels(aplication)

    # lista de productos
    lista_comidas = ['pollo', 'cordero', 'salmón', 'merzlua', 'kebab', 'pizza1', 'pizza2', 'pizza3']
    lista_bebidas = ['agua', 'fanta', 'coca cola', 'vino', 'cerveza', 'zumo', 'tónica', 'bitter']
    lista_postres = ['helado', 'brownie', 'fruta', 'flan', 'mousse', 'pastel', 'tarta zanahoria', 'tarta de chocolate']

    gen_items(lista_comidas, panel_comidas)
    gen_items(lista_bebidas, panel_bebidas)
    gen_items(lista_postres, panel_postres)

    # Evitar que la ventana se cierre
    aplication.mainloop()

def new_application():
    # Iniciar tkinter
    aplication = Tk()
    # tamaño de la ventana
    aplication.geometry('1020x630+0+0')

    # evitar maximizar
    aplication.resizable(0, 0)  # no se puede modificar en ningún eje

    # Título de la ventana
    aplication.title('Mi restaurante - Sistema de facturación')

    # Color de fondo de la ventana. También permite RGB
    aplication.config(bg='burlywood')
    return aplication

def new_panels(aplication: object) -> object:
    # panel superior
    panel_superior = Frame(aplication, bd=1, relief=FLAT)
    panel_superior.pack(side=TOP)
    etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                            font=('Dosis', 58), bg='burlywood', width=27)
    etiqueta_titulo.grid(row=0, column=0)

    # panel izquierdo
    panel_izquierdo = Frame(aplication, bd=1, relief=FLAT)
    panel_izquierdo.pack(side=LEFT)

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

    # panel derecha
    panel_derecha = Frame(aplication, bd=1, relief=FLAT)
    panel_derecha.pack(side=RIGHT)

    panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_calculadora.pack()
    panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_recibo.pack()
    panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_botones.pack()

    return (panel_superior, panel_izquierdo, panel_coste, panel_comidas, panel_bebidas, panel_postres, panel_derecha, \
    panel_calculadora, panel_recibo, panel_botones)


def gen_items(items_list, panel):
    # Generar items comida
    variable = []
    cont = 0
    for comida in items_list:
        variable.append(IntVar())  # Crea una variable entera propia de Tkinter
        boton = Checkbutton(panel, text=comida.title(), font=('Dosis', 19, 'bold'),
                            onvalue=1, offvalue=0, variable=variable[cont])
        boton.grid(row=cont, column=1, sticky=W)  # Se colocan a la izquierda
        cont += 1

