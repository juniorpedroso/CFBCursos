from abc import abstractproperty
from tkinter import *

# Cria uma instância de tela
app = Tk()
# Cria um nome para a tela
app.title('Pedroso')
# Informa o tamanho da tela
app.geometry('500x300')
# Cor do fundo da tela
app.configure(background='#008')

txt1 = Label(app, text='Curso de Python', background='#008', foreground='#fff')
txt1.place(x=10, y=10, width=100, height=20)

vtxt = 'Módulo Tkinter'
vbg = '#ff0'
vfg = '#000'
txt2 = Label(app, text = vtxt, bg = vbg, fg = vfg)
txt2.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side = 'top',\
          fill =X, expand = True)

app.mainloop()
 