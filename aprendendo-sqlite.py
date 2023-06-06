import sqlite3 as db 
import pandas as pd


conn = db.connect('DB_SISTEMA_PONTO01.db')
c = conn.cursor()


#c.execute("create table autores (ID_AUTOR SMALLINT auto_increment primary key, NOME_AUTOR varchar(50));")
#c.execute("create table editoras (ID_EDITORA SMALLINT auto_increment primary key, NOME_EDITORA varchar(50));")
#c.execute("create table livros (ID_LIVRO SMALLINT auto_increment primary key, TITULO varchar(50), ID_AUTOR SMALLINT, ID_EDITORA SMALLINT);")

# c.execute("INSERT INTO autores VALUES (1, 'Michael Scott'), (2, 'Jim Halpert'), (3, 'Pam Beesly'), (4, 'Dwight Schrute'), (5, 'Angela Martin');")
# c.execute("INSERT INTO editoras VALUES (1, 'Dunder Mifflin'), (2, 'Sabre'), (3, 'Vance Refrigeration'), (4, 'Scranton White Pages'), (5, 'Michael Scott Paper Company');")
# c.execute("INSERT INTO livros VALUES (1, 'Aprendendo a Programar', 1, 2), (2, 'O Guia do Desenvolvedor', 3, 4), (3, 'Algoritmos e Estruturas de Dados', 5, 1), (4, 'Programação Avançada em Java', 2, 5), (5, 'Introdução à Inteligência Artificial', 4, 3);")



show_db = pd.read_sql_query('select * from autores', conn)

#print(show_db)
sqlpandas = pd.DataFrame(show_db)
print(sqlpandas)
conn.commit()
c.close()
conn.close()