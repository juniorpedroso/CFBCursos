# Aula 63 - Como usar o componente Radiobutton no TKinter

from tkinter import *


def imprimirEsporte():
    ve = vesporte.get()
    if ve == 'f':
        print('Esporte Futebol')
    elif ve == 'v':
        print('Esporte Vôlei')
    elif ve == 'b':
        print('Esporte Basquete')
    else:
        print('Selecione um esporte!')


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

vesporte = StringVar()
vcor = StringVar()

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

rb_futebol = Radiobutton(app, text='Futebol', value='f', variable=vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text='Volei', value='v', variable=vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text='Basquete', value='b', variable=vesporte)
rb_basquete.pack()

rb_verde = Radiobutton(app, text='Verde', value='#0f0', variable=vcor)
rb_verde.pack()

rb_vermelho = Radiobutton(app, text='Vermelho', value='#f00', variable=vcor)
rb_vermelho.pack()

btn_esporte = Button(app, text='Esporte Selecionado',
                     command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()
