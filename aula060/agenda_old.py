# Aula 53 do Curso de Python CFBCursos

import os
import comandos

comandos.CriaTabela()

opc = 0
while opc != 6:
    comandos.menuPrincipal()
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        comandos.menuInserir()
    elif opc == 2:
        comandos.menuDeletar()
    elif opc == 3:
        comandos.menuAtualizar()
    elif opc == 4:
        comandos.menuConsultar()
    elif opc == 5:
        comandos.menuConsultarNomes()
    elif opc == 6:
        os.system('cls')
        print('Programa Finalizado!\n')
    else:
        os.system('cls')
        print('Opção inválida!!')
        os.system('pause')


