# Como usar OptionMenu no TKinter

from tkinter import *


def imprimirEsporte():
    ve = vesporte.get()
    if ve == 'Futebol':
        print('Esporte Futebol')
    elif ve == 'Vôlei':
        print('Esporte Vôlei')
    elif ve == 'Basquete':
        print('Esporte Basquete')
    else:
        print('Selecione um esporte!')


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

listaEsportes = ['Futebol', 'Vôlei', 'Basquete']

vesporte = StringVar()
# Valor padrão
vesporte.set(listaEsportes[0])

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

op_esportes = OptionMenu(app, vesporte, *listaEsportes)
op_esportes.pack()

btn_esporte = Button(app, text='Esporte Selecionado',
                     command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()
