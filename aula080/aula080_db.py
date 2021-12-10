# Aula 80 - TreeView com Banco de Dados
# Inserindo elementos de um Banco de dados

from tkinter import *
from tkinter import ttk
import banco


def inserir():
    id = v_id.get()
    nome = v_nome.get()
    fone = v_fone.get()
    if not id or not nome or not fone:
        messagebox.showinfo(title='ERRO', message='Digite todos os dados')
        return
    tv_nomes.insert('', 'end', values=(id, nome, fone))
    v_id.delete(0, END)
    v_nome.delete(0, END)
    v_fone.delete(0, END)
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


banco.CriaTabela()

v_query = 'SELECT * FROM clientes'
l_nomes = banco.dql(v_query)

app = Tk()
app.title('Pedroso')
app.geometry('500x300')

l_id = Label(app, text='ID')
l_mostraID = Label(app, text='ID atual')

l_nome = Label(app, text='Nome')
e_nome = Entr(app)

l_fone = Label(app, text='Fone')
e_fone = Entry(app)

l_email = Label(app, text='E-mail')
e_email = Entry(app)

tv_nomes = ttk.Treeview(app, columns=(
    'id', 'nome', 'fone', 'email', 'obs'), show='headings')
tv_nomes.column('id', minwidth=0, width=20)
tv_nomes.column('nome', minwidth=0, width=200)
tv_nomes.column('fone', minwidth=0, width=100)
tv_nomes.column('email', minwidth=0, width=300)

tv_nomes.heading('id', text='ID')
tv_nomes.heading('nome', text='NOME')
tv_nomes.heading('fone', text='TELEFONE')
tv_nomes.heading('email', text='E-MAIL')

# tv_nomes.pack()
bt_inserir = Button(app, text='Inserir', command=inserir)

for cliente in l_nomes:
    tv_nomes.insert('', 'end', values=(
        cliente[0],
        cliente[1],
        cliente[2],
        cliente[3]))

app.mainloop()
