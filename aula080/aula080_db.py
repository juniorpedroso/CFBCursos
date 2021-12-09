# Aula 80 - TreeView com Banco de Dados
# Inserindo elementos de um Banco de dados

from tkinter import *
from tkinter import ttk
import banco

banco.CriaTabela()

v_query = 'SELECT * FROM clientes'
l_nomes = banco.dql(v_query)

app = Tk()
app.title('Pedroso')
app.geometry('500x300')


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
tv_nomes.pack()

for cliente in l_nomes:
    tv_nomes.insert('', 'end', values=(
        cliente[0], 
        cliente[1],
        cliente[2],
        cliente[3]))

app.mainloop()