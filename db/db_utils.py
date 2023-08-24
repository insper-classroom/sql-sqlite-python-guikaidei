import sqlite3

#FUNÇÃO PARA CONECTAR COM A DB
#O ÚNICO VALOR UTILIZADO É A VARIÁVEL DATABASE QUE DEVE SER UMA STRING COM O CAMINHO DA DATABASE
def conectar(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return conn, cursor


#FUNÇÃO PARA CRIAR TABELA
#É UTILIZADO O CURSOR, NOME DA TABELA EM STRING E UM DICIONARIO COM O NOME DAS COLUNAS 
#E O TIPO DE INFO ARMAZENADO NELAS. EX.: {'COLUNA1': INTEGER, 'COLUNA2'; TEXT NOT NULL}
def criar_tabela(cursor, nome_tabela, dicionario_colunas_parametros):
    colunas = ''
    contador = 0
    for coluna, parametro in dicionario_colunas_parametros.items():
        if contador != len(dicionario_colunas_parametros) - 1:
            colunas += f' {coluna} {parametro},'
            contador += 1
        else:
            colunas += f' {coluna} {parametro}'
    command = f"""CREATE TABLE IF NOT EXISTS {nome_tabela} (ID INTEGER PRIMARY KEY AUTOINCREMENT,{colunas});"""
    return cursor.execute(command)

#FUNÇÃO PARA INSERIR INFOS NA TABELA
#É UTILIZADO O CURSOR, O CONN, NOME DA TABELA EM STRING, UMA LISTA COM O NOME DAS COLUNAS DA TABELA 
#E UMA LISTA COM TUPLAS QUE CONTÉM OS VALORES PRESENTES EM CADA LINHA ORDENADOS PELA ORDEM DAS COLUNAS
def inserir_tabela(cursor, conn, nome_tabela, lista_colunas, lista_linhas):
    colunas = ''
    valores = []
    interrogacoes = (len(lista_colunas) - 1) *'? ,' + '?'
    for linha in lista_linhas:
        valores.append(linha)
    contador = 0
    for coluna in lista_colunas:
        if contador == 0:
            colunas += f'{coluna},'
            contador += 1
        elif contador != len(lista_colunas) - 1:
            colunas += f' {coluna},'
            contador += 1
        else:
            colunas += f' {coluna}'
    command = f"""INSERT INTO {nome_tabela} ({colunas}) VALUES ({interrogacoes});"""
    cursor.executemany(command, valores)
    conn.commit()

#FUNÇÃO PARA EDITAR INFOS NA TABELA
#É UTILIZADO O CURSOR, O CONN, NOME DA TABELA EM STRING, O NOME DA COLUNA QUE TERÁ SEU VALOR EDITADO,
#O NOME DE UMA COLUNA E SEU VALOR PARA IDENTIFICAR A LINHA QUE DEVE SER EDITADA
def editar_registro(cursor, conn, nome_tabela, coluna_valor_editado, coluna_identificadora, valor_identificador, valor_atualizado):
    cursor.execute(f"UPDATE {nome_tabela} SET {coluna_valor_editado} = ? WHERE {coluna_identificadora} = ?", (valor_atualizado, valor_identificador))
    conn.commit()

#FUNÇÃO PARA DELETAR INFOS NA TABELA
#É UTILIZADO O CURSOR, O CONN, NOME DA TABELA EM STRING E O NOME DA COLUNA
#E SEU VALOR PARA IDENTIFICAR A LINHA QUE DEVE SER DELETADA
def deletar_registro(cursor, conn, nome_tabela, coluna, valor):
    cursor.execute(f"DELETE FROM {nome_tabela} WHERE {coluna} = {str(valor)}")
    conn.commit()

#FUNÇÃO PARA MOSTRAR INFOS NA TABELA
#É UTILIZADO O CURSOR, NOME DA TABELA EM STRING E O NOME DA COLUNA A SER MOSTRADA
def mostrar_registro(cursor, nome_tabela, coluna):
    cursor.execute(f"SELECT {coluna} FROM {nome_tabela}")
    print(cursor.fetchall())

#FUNÇÃO PARA MOSTRAR INFOS ESPECÍFICAS NA TABELA
#É UTILIZADO O CURSOR, NOME DA TABELA EM STRING, O NOME DA COLUNA A SER MOSTRADA
#E O NOME DA COLUNA E SEU VALOR QUE VÃO ESPECIFICAR QUAL LINHA DEVE SER MOSTRADA
def mostrar_registro_especifico(cursor, nome_tabela, coluna, coluna_especificadora, valor_especificador):
    cursor.execute(f"SELECT {coluna} FROM {nome_tabela} WHERE {coluna_especificadora} = {valor_especificador}")
    print(cursor.fetchall())

#FUNÇÃO PARA FECHAR CONEXÃO
def fechar_conexao(conn):
    conn.close()