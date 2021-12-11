# Aula 80 - TreeView com Banco de Dados
# Inserindo deletando e obtendo elementos

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import aula082_banco as banco

banco.CriaTabela()


def popular():
    tv_nomes.delete(*tv_nomes.get_children())
    vquery = 'SELECT * FROM clientes order by n_id'
    linhas = banco.dql(vquery)
    for i in linhas:
        tv_nomes('', 'end', values=i)


def inserir():
    nome = v_nome.get()
    fone = v_fone.get()
    email = v_email.get()
    if not nome or not fone or not email:
        messagebox.showinfo(title='ERRO', message='Digite todos os dados')
        return
    try:
        vquery = 'INSERT into clientes (t_nome, t_fone, t_email) \
                  VALUES ("' + nome + '", "' + fone + '", + "' + email + '")'
        banco.dml(vquery)
    except:
        messagebox.showinfo(title='ERRO', message='Erro ao inserir')
        return
    popular()
    v_id.delete(0, END)
    v_nome.delete(0, END)
    v_fone.delete(0, END)
    v_email.delte(0, END)
    v_id.focus()


def deletar():
    try:
        itemSel = tv_nomes.selection()[0]
        tv_nomes.delete(itemSel)
    except:
        messagebox.showinfo(title='ERRO',
                            message='Selecione um elemento a ser deletado')


def obter():
    try:
        itemSel = tv_nomes.selection()[0]
        valores = tv_nomes.item(itemSel, 'values')
        # Primeiro eu apago os campos dos elementos ENTRY
        v_id.delete(0, END)
        v_nome.delete(0, END)
        v_fone.delete(0, END)
        # Aqui eu preencho os campos
        v_id.insert(0, valores[0])
        v_nome.insert(0, valores[1])
        v_fone.insert(0, valores[2])
    except:
        messagebox.showinfo(title='ERRO',
                            message='Selecione um elemento')


app = Tk()
app.title('Pedroso')
app.geometry('560x350')

l_id = Label(app, text='ID')
v_id = Entry(app)

l_nome = Label(app, text='Nome')
v_nome = Entry(app)

l_fone = Label(app, text='Fone')
v_fone = Entry(app)

l_email = Label(app, text='E-mail')
v_email = Entry(app)


tv_nomes = ttk.Treeview(app, columns=('id', 'nome', 'fone', 'email'),
                        show='headings')
tv_nomes.column('id', minwidth=0, width=50)
tv_nomes.column('nome', minwidth=0, width=200)
tv_nomes.column('fone', minwidth=0, width=100)
tv_nomes.column('email', minwidth=0, width=200)

tv_nomes.heading('id', text='ID')
tv_nomes.heading('nome', text='NOME')
tv_nomes.heading('fone', text='TELEFONE')
tv_nomes.heading('email', text='E-MAIL')

bt_inserir = Button(app, text='Inserir', command=inserir)
bt_deletar = Button(app, text='Deletar', command=deletar)
bt_obter = Button(app, text='Obter', command=obter)


l_id.grid(column=0, row=0, sticky='w')
v_id.grid(column=0, row=1)

l_nome.grid(column=1, row=0, sticky='w')
v_nome.grid(column=1, row=1)

l_fone.grid(column=2, row=0, sticky='w')
v_fone.grid(column=2, row=1)

l_email.grid(column=0, row=3, sticky='w')
v_email.grid(column=0, row=4)

tv_nomes.grid(column=0, row=5, columnspan=3, padx=1, pady=1)

bt_inserir.grid(column=0, row=6)
bt_deletar.grid(column=1, row=6)
bt_obter.grid(column=2, row=6)

app.mainloop()
