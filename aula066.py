# Aula 66 - sobre Frame

from tkinter import *
from tkinter import messagebox


def mostraMsg():
    messagebox.showinfo(title='Pedroso', message='Pedroso')


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

vnum_cxtexto = StringVar()

# Valores de relief: flat, raised, sunken, solid
# raised - elevada
# sunken - afundada
fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
fr_quadro1.place(x=10, y=10, width=300, height=100)

lb_tipo = Label(fr_quadro1, text='Tipo de cx(1, 2 ou 3)')
lb_tipo.place(x=10, y=10)
tb_num = Entry(fr_quadro1, textvariable=vnum_cxtexto)
vnum_cxtexto.set('1')
tb_num.place(x=10, y=30)

# Usando o lambda para passar os parâmetros
btn_msg = Button(fr_quadro1, text='Mostrar mensagem', command=mostraMsg)
btn_msg.place(x=10, y=50)

fr_quadro2 = Frame(app, borderwidth=1, relief='solid', bg='lightblue')
fr_quadro2.place(x=10, y=120, width=300, height=100)

app.mainloop()
