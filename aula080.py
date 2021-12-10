# Aula 80 - TreeView com Banco de Dados
# Inserindo elementos de um Banco de dados

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

l_id = Label(app, text='ID')
v_id = Entry(app)

l_nome = Label(app, text='Nome')
v_nome = Entry(app)

l_fone = Label(app, text='Fone')
v_fone = Entry(app)

tv_nomes = ttk.Treeview(app, columns=('id', 'nome', 'fone'),
                        show='headings')
tv_nomes.column('id', minwidth=0, width=50)
tv_nomes.column('nome', minwidth=0, width=200)
tv_nomes.column('fone', minwidth=0, width=100)

tv_nomes.heading('id', text='ID')
tv_nomes.heading('nome', text='NOME')
tv_nomes.heading('fone', text='TELEFONE')

bt_inserir = Button(app, text='Inserir', command=inserir)
bt_deletar = Button(app, text='Deletar', command=deletar)
bt_obter = Button(app, text='Obter', command=obter)


l_id.grid(column=0, row=0, sticky='w')
v_id.grid(column=0, row=1)

l_nome.grid(column=1, row=0, sticky='w')
v_nome.grid(column=1, row=1)

l_fone.grid(column=2, row=0, sticky='w')
v_fone.grid(column=2, row=1)

tv_nomes.grid(column=0, row=3, columnspan=3, padx=1, pady=1)

bt_inserir.grid(column=0, row=4)
bt_deletar.grid(column=1, row=4)
bt_obter.grid(column=2, row=4)

app.mainloop()
