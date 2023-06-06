import pandas as pd
import sqlite3 as db


conn = db.connect('DB_SISTEMA_PONTO01.db')
c = conn.cursor()

show_db = pd.read_sql_query('select * from livros', conn)
#print(show_db)

sqlpandas = pd.DataFrame(show_db)
print(sqlpandas)
conn.commit()
c.close()
conn.close()