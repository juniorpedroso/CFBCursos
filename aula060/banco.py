# Aula 060 do CFB Cursos de Python - Criando uma agenda com TKinter

import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + '\\agenda.db'


def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as erro:
        print(erro)
    return con


# Cria uma tabela de nome clientes, se não existir antes
# When SQL is used to create, modify, or destroy objects within an RDBMS, 
# it puts on its Data Definition Language (DDL) hat. 
# Here you have the CREATE, ALTER, and DROP statements, plus a couple of others.
def CriaTabela():
    vcon = ConexaoBanco()
    cur = vcon.cursor()
    vsql = """CREATE TABLE IF NOT EXISTS clientes (
                    n_id INTEGER PRIMARY KEY ,
                    t_nome varchar(30),
                    t_telefone varchar(14), 
                    t_email varchar(30),
                    t_obs varchar(512)
                    );"""
    cur.execute(vsql)
    vcon.close()


# Some bundle the Data Query Language (DQL) into DML,
# arguing that it also manipulates data. There are merits to this argument, 
# not least that there is but a single member in this category: 
# the SELECT statement.
def dql(query):
    vcon = ConexaoBanco()
    cur = vcon.cursor()
    cur.execute(query)
    res = cur.fetchall()
    vcon.close()
    return res

# The Data Manipulation Language (DML) is the domain of 
# INSERT, UPDATE, and DELETE, which you use to manipulate data.
def dml(query):
    try:
        vcon = ConexaoBanco()
        cur = vcon.cursor()
        cur.execute(query)
        vcon.commit()
        vcon.close()
    except Error as erro:
        print(erro)
