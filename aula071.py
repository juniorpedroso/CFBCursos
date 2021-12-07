# Aula 71 - ComboBox


from tkinter import *
from tkinter import ttk


def mostraEsporte():
    esporte = cb_esportes.get()
    # Alterando o texto do LABEL
    l_mostraEsporte.config(text=esporte)


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

listEsportes = ['Futebol', 'Vôlei', 'Basquete']

lb_esportes = Label(app, text='Esportes')
lb_esportes.place(x=30, y=10, width=100, height=20)

cb_esportes = ttk.Combobox(app, values=listEsportes)
# Isto faz com que Futebol fique selecionado
cb_esportes.set('Futebol')
cb_esportes.place(x=30, y=40, width=100, height=20)


btn_mostraEsporte = Button(app, text='Mostra Esporte', command=mostraEsporte)
btn_mostraEsporte.place(x=30, y=70, width=100, height=20)

l_mostraEsporte = Label(app, text='Esporte',
                        background='lightblue', foreground='black')
l_mostraEsporte.place(x=30, y=130, width=100, height=20)

app.mainloop()
