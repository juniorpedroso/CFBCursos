# Aula 73 - LabelFrame

from tkinter import *

app = Tk()
app.title('Pedroso')
app.geometry('500x300')

lbf_esportes = LabelFrame(app, text = 'Linguagens', borderwidth = 1, relief = 'solid')
lbf_esportes.place(x = 10, y = 10, width = 300, height = 100)

lb1 = Label(lbf_esportes, text = 'Python')
lb1.pack()

lb2 = Label(lbf_esportes, text = 'Java')
lb2.pack()

lb3 = Label(lbf_esportes, text = 'C')
lb3.pack()

app.mainloop()
