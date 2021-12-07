# Aula 70 - Password
# Como alterar o texto do LABEL


from tkinter import *


def mostraSenha():
    senha = p_senha.get()
    print(senha)
    # Alterando o texto do LABEL
    l_mostraSenha.config(text=senha)
    # Apagando o valor anterior de ENTRY
    p_senha.delete(0, END)


app = Tk()
app.title('Pedroso')
app.geometry('500x300')

vsenha = StringVar()

p_senha = Entry(app, textvariable=vsenha, show='*')
# p_senha.pack()
p_senha.place(x=30, y=10, width=100, height=20)
# Forçando o foco para o ENTRY
p_senha.focus_force()

btn_mostraSenha = Button(app, text='Imprimir Senha', command=mostraSenha)
btn_mostraSenha.place(x=30, y=40, width=100, height=20)

l_mostraSenha = Label(app, text='PASSWORD',
                      background='lightblue', foreground='black')
l_mostraSenha.place(x=30, y=70, width=100, height=20)

app.mainloop()
