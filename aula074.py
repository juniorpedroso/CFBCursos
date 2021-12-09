# Aula 74 - Listbox

from tkinter import *


def mostraLinguagem():
    vlinguagem = lb_linguagens.get(ACTIVE)
    l_selecionado.config(text=vlinguagem)


def insereLinguagem():
    lb_linguagens.insert(END, e_novaLinguagem.get())


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

listaLinguagens = ['Python', 'Java', 'C++', 'Delphi']

lb_linguagens = Listbox(app)
for linguagem in listaLinguagens:
    lb_linguagens.insert(END, linguagem)
lb_linguagens.pack()

# Elemento ENTRY recebe uma nova linguagem
e_novaLinguagem = Entry(app)
e_novaLinguagem.pack()

# Elemento Button chama a função insereLinguagem
btn_insereNova = Button(app, text='Insere linguagem',
                        command=insereLinguagem)
btn_insereNova.pack()

# Este LABEL exibe a linguagem selecionada
l_selecionado = Label(app, text='Linguagem')
l_selecionado.pack()

# Este Button chama a função mostraLinguagem
btn_mostraLinguagem = Button(app, text='Mostra Linguagem',
                             command=mostraLinguagem)
btn_mostraLinguagem.pack()

app.mainloop()
