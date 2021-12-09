from tkinter import *
import os
import banco

banco.CriaTabela()


def gravarDados():
    if tb_nome.get() != '':
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get('1.0', END)
        vquery = 'INSERT into clientes (t_nome, t_telefone, t_email, t_obs)\
                  VALUES ("' + vnome + '", "' + vfone + '",\
                          "' + vemail + '", "' + vobs + '")'
        banco.dml(vquery)
        # Apagando os Text Box
        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete('1.0', END)
        #   definindo o foco para o Text Box de nome
        tb_nome.focus()
        print('Dados Gravados')

    else:
        print('ERRO')


app = Tk()
app.geometry('500x300')
app.configure(background='#dde')

# anchors=> N=Norte, S=Sul, E=Leste, W=Oeste
# NE=Nordeste, SE=Sudeste, SW=Sudoeste, NW=Noroeste
Label(app, text='None', background='#dde', foreground='#009',
      anchor=W).place(x=10, y=10, width=100, height=20)
tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

Label(app, text='Telefone', background='#dde', foreground='#009',
      anchor=W).place(x=10, y=60, width=100, height=20)
tb_fone = Entry(app)
tb_fone.place(x=10, y=80, width=100, height=20)

Label(app, text='E-mail', background='#dde', foreground='#009',
      anchor=W).place(x=10, y=110, width=100, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=130, width=300, height=20)

Label(app, text='Obs.', background='#dde', foreground='#009',
      anchor=W).place(x=10, y=160, width=100, height=20)
tb_obs = Text(app)
tb_obs.place(x=10, y=180, width=300, height=80)

Button(app, text='Gravar', command=gravarDados).place(
    x=10, y=270, width=100, height=20)

app.mainloop()