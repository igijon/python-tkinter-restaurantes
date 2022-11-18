from tkinter import *

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
text_comidas = []
text_bebidas = []
text_postres = []
var_precio_comida = ''
var_precio_bebidas = ''
var_precio_postres = ''
var_precio_subtotal = ''
var_precio_impuestos = ''
var_precio_total = ''
text = {}

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

    gen_items(lista_comidas, panel_comidas, text_comidas)
    gen_items(lista_bebidas, panel_bebidas, text_bebidas)
    gen_items(lista_postres, panel_postres, text_postres)

    gen_precios(panel_coste, 'Total', 2, 2)
    gen_precios(panel_coste, 'Comida', 0, 0)
    gen_precios(panel_coste, 'Bebida', 1, 0)
    gen_precios(panel_coste, 'Postre', 2, 0)
    gen_precios(panel_coste, 'Subtotal', 0, 2)
    gen_precios(panel_coste, 'Impuestos', 1, 2)
    text['Total'].config(textvariable=var_precio_total)
    text['Comida'].config(textvariable=var_precio_comida)
    text['Bebida'].config(textvariable=var_precio_bebidas)
    text['Postre'].config(textvariable=var_precio_postres)
    text['Subtotal'].config(textvariable=var_precio_subtotal)
    text['Impuestos'].config(textvariable=var_precio_impuestos)

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



def gen_items(items_list, panel, text):
    # Generar items comida
    variable = []
    entrada = []

    cont = 0
    for comida in items_list:
        # Crear checkbuttons
        variable.append(IntVar())  # Crea una variable entera propia de Tkinter
        boton = Checkbutton(panel,
                            text=comida.title(),
                            font=('Dosis', 19, 'bold'),
                            onvalue=1,
                            offvalue=0,
                            variable=variable[cont],
                            command=lambda: revisar_check(variable, entrada, text))
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
    global var_precio_comida
    global var_precio_bebidas
    global var_precio_postres
    global var_precio_total
    global var_precio_impuestos
    global var_precio_subtotal
    global text

    var_precio_comida = StringVar()
    var_precio_bebidas = StringVar()
    var_precio_postres = StringVar()
    var_precio_subtotal = StringVar()
    var_precio_impuestos = StringVar()
    var_precio_total = StringVar()

    label_precio = Label(panel,
                         text='Precio '+concepto,
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white')
    label_precio.grid(row=row, column=column)
    text[concepto]=(Entry(panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly'))
    text[concepto].grid(row=row, column=column+1, padx=41)


def gen_buttons(panel):
    buttons = ['total', 'recibo', 'guardar', 'reset']
    botones_creados = []
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
        botones_creados.append(b)
        click_botones(len(botones_creados)-1, botones_creados, buttons)
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


def revisar_check(variable, entrada, text):
    x = 0
    for e in entrada:
        if variable[x].get() == 1:
            e.config(state=NORMAL)
            if text[x].get() == '0':
                e.delete(0, END)
            e.focus()
        else:
            e.config(state=DISABLED)
            text[x].set('0')
        x += 1


def click_botones(num, botones_creados, botones_etiquetas):
    if botones_etiquetas[num] == 'total':
        botones_creados[num].config(command=lambda: total())


def total_parcial(var, text, precios):
    sub_total = 0

    for cont in range(len(precios)):
        try:
            cant = float(text[cont].get())
        except ValueError:
            cant = 0
        sub_total += cant*precios[cont]
    var.set(f'{round(sub_total, 2)} €')
    return sub_total


def total():
    global var_precio_comida
    global var_precio_bebidas
    global var_precio_postres
    global var_precio_subtotal
    global var_precio_impuestos
    global var_precio_total

    global text_comidas
    global text_bebidas
    global text_postres

    sub_total_comida = total_parcial(var_precio_comida, text_comidas, precios_comida)
    var_precio_comida.set(f'{round(sub_total_comida, 2)} €')

    sub_total_bebida = total_parcial(var_precio_bebidas, text_bebidas, precios_bebida)
    var_precio_bebidas.set(f'{round(sub_total_bebida, 2)} €')

    sub_total_postres = total_parcial(var_precio_postres, text_postres, precios_postres)
    var_precio_postres.set(f'{round(sub_total_postres, 2)} €')

    sub_total = sub_total_comida+sub_total_bebida+sub_total_postres
    impuestos = sub_total * 0.21
    precio_total = sub_total+impuestos
    var_precio_total.set(f'{round(precio_total, 2)} €')
    var_precio_subtotal.set(f'{round(sub_total, 2)} €')
    var_precio_impuestos.set(f'{round(impuestos, 2)} €')