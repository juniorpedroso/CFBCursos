# Aula 78 - Grid

from tkinter import *
from tkinter import ttk


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

lb_canal = Label(app, text='CFB Cursos')
lb_nome = Label(app, text='Digite seu nome')
lb_idade = Label(app, text='Digite sua idade')

en_nome = Entry(app)
en_idade = Entry(app)

btn = Button(app, text='Canal')

lb_canal.grid(column=0, row=0, columnspan=2)
# lb_canal.grid(collumn = 0, row = 0, columnspan = 2, pasy = 15)

# Opções do sticky => w -> esquerda; e-> direita; n-> cima. s-> baixo
lb_nome.grid(column=0, row=1, sticky='w')
en_nome.grid(column=0, row=2)

lb_idade.grid(column=1, row=1, sticky='w')
en_idade.grid(column=1, row=2)


app.mainloop()
