import pandas as pd
import sqlite3 as db

conn = db.connect('DB_SISTEMA_PONTO.db')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
show_db = pd.read_sql_query('select * from TBL_FUNCIONARIO', conn)

query = """
    
SELECT PRIMEIRO_NOME_FUNCIONARIO, DATA_PONTO, HORA_ENTRADA_PONTO, HORA_SAIDA_PONTO, TIPO_OCORRENCIA, HORA_INICIO_OCORRENCIA, HORA_FIM_OCORRENCIA, DESCONTO_OCORRENCIA FROM TBL_FUNCIONARIO
INNER JOIN TBL_REGISTRO_PONTO
ON TBL_FUNCIONARIO.ID_FUNCIONARIO = TBL_REGISTRO_PONTO.ID_FUNCIONARIO
INNER JOIN TBL_OCORRENCIA_PONTO
ON TBL_REGISTRO_PONTO.ID_REGISTRO_PONTO = TBL_OCORRENCIA_PONTO.ID_REGISTRO_PONTO;


"""
teste = pd.read_sql_query(query, conn)

print(teste)




conn.close()