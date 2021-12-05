# Comandos para o banco de dados

import os
import sqlite3 as sql
from sqlite3 import Error


def ConexaoBanco():
    caminho = 'agenda.db'
    con = None
    try:
        con = sql.connect(caminho)
    except Error as erro:
        print(erro)
    return con


# Cria uma tabela de nome pessoas, se não existir antes
def CriaTabela():
    vcon = ConexaoBanco()
    cursor = vcon.cursor()
    vsql = """CREATE TABLE IF NOT EXISTS clientes (
                    n_id INTEGER PRIMARY KEY ,
                    t_nome varchar(30),
                    t_telefone varchar(14), 
                    t_email varchar(30),
                    t_obs varchar(512)
                    );"""
    cursor.execute(vsql)
    vcon.close()


# Função utilizada para INSERT, DELETE e UPDATE


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as erro:
        print(erro)
    finally:
        print('Operação realizada com sucesso!')
        conexao.close()

# Função usada para SELECT


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    # conexao.close()
    return res


def menuPrincipal():
    os.system('cls')
    print('1 - Inserir Novo Registro')
    print('2 - Deletar Registro')
    print('3 - Atualizar Registro')
    print('4 - Consultar Registros')
    print('5 - Consultar Registro por Nome')
    print('6 - Sair')


def menuInserir():
    os.system('cls')
    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o e-mail: ')

    vsql = 'INSERT into clientes (t_nome, t_telefone, t_email) VALUES \
            ("'+vnome+'", "'+vtelefone+'", "'+vemail+'")'

# ("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))

    vcon = ConexaoBanco()
    query(vcon, vsql)
    vcon.close()


def menuDeletar():
    os.system('cls')
    vid = input('Digite o ID do registro a ser deletado: ')
    vsql = 'DELETE from clientes WHERE n_id = ' + vid
    vcon = ConexaoBanco()
    query(vcon, vsql)
    vcon.close()


def menuAtualizar():
    os.system('cls')
    vid = input('Digite o ID do registro a ser alterado: ')
    vcon = ConexaoBanco()
    r = consultar(vcon, 'SELECT * from clientes WHERE n_id = ' + vid)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    print('Dados originais')
    print('Nome: ', rnome)
    print('Telefone: ', rtelefone)
    print('e-mail: ', remail)
    print()
    print('Digite os novos dados')
    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o e-mail: ')

    # Verifica se os campos foram deixados em branco, se sim
    # volta com os dados originais
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail

    vsql = 'UPDATE clientes SET \
            t_nome = "' + vnome + '",\
            t_telefone = "' + vtelefone + '",\
            t_email = "' + vemail + '" \
            WHERE n_id = ' + vid

    query(vcon, vsql)
    vcon.close()


def menuConsultar():
    vsql = 'SELECT * from clientes'
    vcon = ConexaoBanco()
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(
            f'ID: {r[0]:_<3} Nome: {r[1]:_<30} Telefone: {r[2]:_<14} E-mail: {r[3]:_<30}')
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system('pause')
            os.system('cls')

    print('Fim da lista')
    os.system('pause')
    vcon.close()


def menuConsultarNomes():
    vnome = input('Digite o nome: ')
    vsql = 'SELECT * from clientes WHERE t_nome LIKE "%' + vnome + '%"'
    vcon = ConexaoBanco()
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(
            f'ID: {r[0]:_<3} Nome: {r[1]:_<30} Telefone: {r[2]:_<14} E-mail: {r[3]:_<30}')
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system('pause')
            os.system('cls')

    print('Fim da lista')
    os.system('pause')
    vcon.close()
