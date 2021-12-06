# Aula 65 - sobre MessageBox

from tkinter import *
from tkinter import messagebox


def mostraMsg(tipomsg, msg):
    if tipomsg == '1':
        messagebox.showinfo(title='Pedroso', message=msg)
    elif tipomsg == '2':
        messagebox.showwarning(title='Pedroso', message=msg)
    elif tipomsg == '3':
        messagebox.showerror(title='Pedroso', message=msg)


# Tipos de messagebox
# askyesno, askquestion - SIM E NÃO (True e False)
# askokcancel - OK e Cancela (True e False)
# askretrycancel - Repetir e Cancela - (True e False)
# messagebox - Sim, Não e Cancelar - (True, Fales e None)
def resetarTB():
    res = messagebox.askyesno('Resetar', 'Confirma reset do TextBox?')
    if res:
        tb_num.delete(0, END)
        tb_num.insert(0, '1')


vmsg = 'Curso de Python/TKinter'

app = Tk()
app.title('Pedroso')
app.geometry('500x300')

vnum_cxtexto = StringVar()

Label(app, text='Tipo de cx(1, 2 ou 3)').pack()
tb_num = Entry(app, textvariable=vnum_cxtexto)
vnum_cxtexto.set('1')
tb_num.pack()

# Usando o lambda para passar os parâmetros
btn_msg = Button(app, text='Mostrar mensagem',
                 command=lambda: mostraMsg(vnum_cxtexto.get(), vmsg))
btn_msg.pack()

btn_reset = Button(app, text='Resetar TextBox', command=resetarTB)
btn_reset.pack()

app.mainloop()
