# Aula 82 - TreeView com Banco de Dados

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
        tv_nomes.insert('', 'end', values=i)


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
    v_nome.delete(0, END)
    v_fone.delete(0, END)
    v_email.delete(0, END)
    v_nome.focus()


def deletar():
    vid = -1
    itemSel = tv_nomes.selection()[0]
    valores = tv_nomes.item(itemSel, 'Values')
    vid = valores[0]
    try:
        vquery = 'DELETE FROM clientes WHERE n_id=' + vid
        banco.dml(vquery)
    except:
        messagebox.showinfo(title='ERRO',
                            message='Erro ao deletar')
        return
    tv_nomes.delete(itemSel)


def pesquisar():
    tv_nomes.delete(*tv_nomes.get_children())
    vquery = 'SELECT * FROM clientes WHERE t_nome LIKE "%'\
        + v_nomePesquisar.get() + '%" order by n_id'
    linhas = banco.dql(vquery)
    for i in linhas:
        tv_nomes.insert('', 'end', values=i)
    v_nomePesquisar.delete(0, END)
    v_nomePesquisar.focus()


app = Tk()
app.title('Pedroso')
app.geometry('630x450')

#################################################

quadroGrid = LabelFrame(app, text='Contatos')
quadroGrid.pack(fill='both', expand='yes', padx=10, pady=10)

tv_nomes = ttk.Treeview(quadroGrid, columns=('id', 'nome', 'fone', 'email'),
                        show='headings')
tv_nomes.column('id', minwidth=0, width=50)
tv_nomes.column('nome', minwidth=0, width=200)
tv_nomes.column('fone', minwidth=0, width=100)
tv_nomes.column('email', minwidth=0, width=200)
tv_nomes.heading('id', text='ID')
tv_nomes.heading('nome', text='NOME')
tv_nomes.heading('fone', text='TELEFONE')
tv_nomes.heading('email', text='E-MAIL')
tv_nomes.pack()
popular()

#################################################

quadroInserir = LabelFrame(app, text='Inserir Novos Clientes')
quadroInserir.pack(fill='both', expand='yes', padx=10, pady=10)

l_nome = Label(quadroInserir, text='Nome')
l_nome.pack(side='left')

v_nome = Entry(quadroInserir)
v_nome.pack(side='left', padx=10)

l_fone = Label(quadroInserir, text='Fone')
l_fone.pack(side='left')

v_fone = Entry(quadroInserir)
v_fone.pack(side='left', padx=10)

l_email = Label(quadroInserir, text='E-mail')
l_email.pack(side='left')

v_email = Entry(quadroInserir)
v_email.pack(side='left')

bt_inserir = Button(quadroInserir, text='Inserir', command=inserir)
bt_inserir.pack(side='left', padx=10)

#################################################

quadroPesquisar = LabelFrame(app, text='Pesquisar Clientes')
quadroPesquisar.pack(fill='both', expand='yes', padx=10, pady=10)

l_nomePesquisar = Label(quadroPesquisar, text='Nome')
l_nomePesquisar.pack(side='left')
v_nomePesquisar = Entry(quadroPesquisar)
v_nomePesquisar.pack(side='left', padx=10)
bt_pesquisar = Button(quadroPesquisar, text='Pesquisar', command=pesquisar)
bt_pesquisar.pack(side='left', padx=10)
bt_todos = Button(quadroPesquisar, text='Mostrar Todos', command=popular)
bt_todos.pack(side='left', padx=10)


app.mainloop()
