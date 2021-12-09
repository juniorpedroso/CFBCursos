# Aula 71 - Scale


from tkinter import *


def valorEscala():
    vvalor = str(sc_escala.get())
    lb_mostraValor.config(text=vvalor)


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

lb_valor = Label(app, text='Valor')
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(50)
sc_escala.pack()

lb_mostraValor = Label(app, text='50')
lb_mostraValor.pack()

btn_valor = Button(app, text='Valor Escala', command=valorEscala)
btn_valor.pack()


app.mainloop()
