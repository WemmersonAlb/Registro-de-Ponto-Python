import pandas as pd
import sqlite3 as db

conn = db.connect('DB_SISTEMA_PONTO.db')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
show_db = pd.read_sql_query('select * from TBL_FUNCIONARIO', conn)

query = """
    select PRIMEIRO_NOME_FUNCIONARIO AS NOME, SOBRENOME_FUNCIONARIO AS SOBRENOME from TBL_FUNCIONARIO WHERE ID_FUNCIONARIO = 1;
"""
teste = pd.read_sql_query(query, conn)

print(teste)




conn.close()