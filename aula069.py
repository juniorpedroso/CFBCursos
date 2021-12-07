# Aula 69 - Checkbutton
# Usando a variável IntVar é melhor pois o Checkbutton não aparece
# como se já estivesse clicado


from tkinter import *
import os


def futebolClicado():
    print('Futebol:' + str(vfutebol.get()))


def voleiClicado():
    print('Vôlei:' + str(vvolei.get()))


def basqueteClicado():
    print('Basquete:' + str(vbasquete.get()))


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

# vfutebol = StringVar()
# vvolei = StringVar()
# vbasquete = StringVar()

vfutebol = IntVar()
vvolei = IntVar()
vbasquete = IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro1, text='Futebol', variable=vfutebol,
                         onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text='Volei', variable=vvolei,
                       onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text='Basquete', variable=vbasquete,
                          onvalue=1, offvalue=0, command=basqueteClicado)
cb_basquete.pack(side=LEFT)


app.mainloop()
