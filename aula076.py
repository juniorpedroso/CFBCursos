# Aula 76 - abas (Frames) e notebook

from tkinter import *
from tkinter import ttk

app = Tk()
app.title('Pedroso')
app.geometry('500x300')

nb = ttk.Notebook(app)
nb.place(x=1, y=0, width=500, height=300)

tb1 = Frame(nb)
tb2 = Frame(nb)

nb.add(tb1, text='Linguagem')
nb.add(tb2, text='Sist. Operacional')

l1_label = Label(tb1, text='Python')
l1_label.pack()

l2_label = Label(tb1, text='C')
l2_label.pack()

l3_label = Label(tb2, text='Windows')
l3_label.pack()

l4_label = Label(tb2, text='Linux')
l4_label.pack()


app.mainloop()
