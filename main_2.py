from db.db_utils import *

conn, cursor = conectar('db/database_teste.db')

dicionario_colunas_parametros = {'coluna1': 'INTEGER', 'coluna2': 'TEXT NOT NULL'}
criar_tabela(cursor, 'teste', dicionario_colunas_parametros)

lista_colunas = ['coluna1', 'coluna2']
lista_linhas = [(234, 'oi'), (777, 'tchau')]
inserir_tabela(cursor, conn, 'teste', lista_colunas, lista_linhas)

mostrar_registro(cursor, 'teste', '*')

mostrar_registro_especifico(cursor, 'teste', '*', 'coluna1', 234)

editar_registro(cursor, conn, 'teste', 'coluna1', 'coluna2', 'oi', 666)

mostrar_registro(cursor, 'teste', '*')

deletar_registro(cursor, conn, 'teste', 'coluna1', '666')

mostrar_registro(cursor, 'teste', '*')

fechar_conexao(conn)