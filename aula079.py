# Aula 79 - TreeView
# Inserindo elementos de uma lista em um componente TreeView

from tkinter import *
from tkinter import ttk


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

v_lista_nomes = [['0', 'Brertilda', '(14)99999-1234'],
                 ['1', 'Bruce', '(14)97874-5489'],
                 ['2', 'Calzone', '(14)99123-7823']]

tv_nomes = ttk.Treeview(app, columns=('id', 'nome', 'fone'),
                        show='headings')
tv_nomes.column('id', minwidth=0, width=50)
tv_nomes.column('nome', minwidth=0, width=200)
tv_nomes.column('fone', minwidth=0, width=100)

tv_nomes.heading('id', text='ID')
tv_nomes.heading('nome', text='NOME')
tv_nomes.heading('fone', text='TELEFONE')
tv_nomes.pack()

for i, n, f in v_lista_nomes:
    tv_nomes.insert('', 'end', values=(i, n, f))

app.mainloop()
