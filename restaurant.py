from tkinter import *

operador = ''

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

    gen_precios(panel_coste, 'Comida', 0, 0)
    gen_precios(panel_coste, 'Bebida', 1, 0)
    gen_precios(panel_coste, 'Postre', 2, 0)
    gen_precios(panel_coste, 'Subtotal', 0, 2)
    gen_precios(panel_coste, 'Impuestos', 1, 2)
    gen_precios(panel_coste, 'Total', 2, 2)

    gen_buttons(panel_botones)

    gen_recibo(panel_recibo)

    gen_calculadora(panel_calculadora)

    # Evitar que la ventana se cierre
    aplication.mainloop()

def new_application():
    # Iniciar tkinter
    aplication = Tk()
    # tamaño de la ventana
    aplication.geometry('1042x430+0+0')

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
                            font=('Dosis', 58), bg='burlywood', width=30)
    etiqueta_titulo.grid(row=0, column=0)

    # panel izquierdo
    panel_izquierdo = Frame(aplication, bd=1, relief=FLAT)
    panel_izquierdo.pack(side=LEFT)

    # panel coste
    panel_coste = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
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
    entrada=[]
    text=[]
    cont = 0
    for comida in items_list:
        # Crear checkbuttons
        variable.append(IntVar())  # Crea una variable entera propia de Tkinter
        boton = Checkbutton(panel,
                            text=comida.title(),
                            font=('Dosis', 19, 'bold'),
                            onvalue=1,
                            offvalue=0,
                            variable=variable[cont])
        boton.grid(row=cont,
                   column=0,
                   sticky=W)  # Se colocan a la izquierda
        # Crear cuatros de entrada
        text.append(StringVar())
        text[cont].set('0')
        entrada.append(Entry(panel,
                             font=('Dosis', 18, 'bold'),
                             bd=1,
                             width=6,
                             state=DISABLED,
                             textvariable=text[cont]))
        entrada[cont].grid(row=cont,
                           column=1)
        cont += 1


def gen_precios(panel, concepto, row, column):
    var_precio = StringVar()

    label_precio = Label(panel,
                         text='Precio '+concepto,
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white')
    label_precio.grid(row=row, column=column)
    text = Entry(panel,
                 font=('Dosis', 12, 'bold'),
                 bd=1,
                 width=10,
                 state='readonly',
                 textvariable=var_precio)
    text.grid(row=row, column=column+1, padx=41)

def gen_buttons(panel):
    buttons = ['total', 'recibo', 'guardar', 'reset']
    column = 0
    for button in buttons:
        b = Button(panel,
                   text=button.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='black',
                   bg='azure4',
                   bd=1,
                   width=5,
                   height=2)
        b.grid(row=0,
               column=column)
        column += 1

def gen_recibo(panel):
    texto_recibo = Text(panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=39,
                        height=10)
    texto_recibo.grid(row=0,
                      column=0)

def gen_calculadora(panel):
    visor_calculadora = Entry(panel,
                              font=('Dosis', 16, 'bold'),
                              width=32,
                              bd=1)
    visor_calculadora.grid(row=0,
                           column=0,
                           columnspan=4)
    botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3',
                           'x', '=', 'Borrar', '0', '/']

    botones_guardados = []
    row = 1
    column = 0
    for b in botones_calculadora:
        botones_guardados.append(Button(panel,
                                 text=b.title(),
                                 font=('Dosis', 16, 'bold'),
                                 fg='black',
                                 bg='azure4',
                                   bd=1,
                                   width=5))

        cont = len(botones_guardados)-1
        botones_guardados[cont].grid(row=row,
                                     column=column)
        click_calculadora(cont, botones_calculadora, botones_guardados, visor_calculadora)

        if column == 3:
            row += 1
            column = 0
        else:
            column += 1


def click_calculadora(num, botones_calculadora, botones_guardados, visor_calculadora):
    text = botones_calculadora[num]
    if not text == '=' and not text == 'Borrar':
        botones_guardados[num].config(command=lambda: click_boton(text, visor_calculadora))
    elif text == 'Borrar':
        botones_guardados[num].config(command=lambda: borrar(visor_calculadora))
    else:
        botones_guardados[num].config(command=lambda: get_result(visor_calculadora))

def click_boton(num, visor_calculadora):
    global operador
    operador = operador + num
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar(visor_calculadora):
    global operador
    visor_calculadora.delete(0, END)
    operador = ''


def get_result(visor_calculadora):
    global operador
    result = str(eval(visor_calculadora.get().title()))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, result)
    operador = ''
