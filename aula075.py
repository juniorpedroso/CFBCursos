# Aula 75 - SpinBox

from tkinter import *

app = Tk()
app.title('Pedroso')
app.geometry('500x300')


def exibirValor():
    vvalor = sb_valores.get()
    l_valor.config(text=vvalor)


# sb_valores = Spinbox(app, from_=0, to=10)
# Os valores podem ser informados por uma faixa, como acima,
# ou como abaixo, em uma tupla
sb_valores = Spinbox(app, values=(2, 4, 6, 8, 10))
sb_valores.pack()

l_valor = Label(app, text='Valor')
l_valor.pack()

btn_exibeValor = Button(app, text='Exibe Valor', command=exibirValor)
btn_exibeValor.pack()

app.mainloop()
