# Aula 77 - ProgressBar

from tkinter import *
from tkinter import ttk
from time import sleep


def valBarra():
    vvalor = sc_escala.get()
    varBarra.set(vvalor)


def contTempo():
    inicio = sc_escala.get()
    for i in range(inicio, 101):
        varBarra.set(i)
        sc_escala.set(i)
        # Caso não use o update a tela não irá atualizar
        app.update()
        sleep(0.05)


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

varBarra = DoubleVar()
varBarra.set(50)


pb = ttk.Progressbar(app, variable=varBarra, maximum=100)
pb.place(x=0, y=80, width=500, height=40)

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(50)
sc_escala.place(x=0, y=150, width=500, height=40)

# Modifica a Progressbar conforme a Scala
btn_valor = Button(app, text='Valor Escala', command=valBarra)
btn_valor.place(x=200, y=220, width=100, height=20)

# Modifica a Progressbar com a passagem do tempo
btn_tempo = Button(app, text='Tempo', command=contTempo)
btn_tempo.place(x=200, y=250, width=100, height=20)

app.mainloop()
