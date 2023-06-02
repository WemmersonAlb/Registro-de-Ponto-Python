import pandas as pd

# editora = {'codigo-editora': [1,2,3,4,5], 'nome-editora':['Alta Books', 'Sextante', 'Suma de Letras', 'IFPE', 'Academia Brasileira de Letras']}

# autores = {'codigo-autor': [1,2,3,4,5], 'nome-autor':['Maria', 'Ana', 'João', 'José', 'Marta']}

# livros = {'codigo-livro': [1,2,3,4,5], 'nome-livro':['Programando em C', 'Programando em Java', 'Programando em Python', 'Programando em Javascript', 'Programando em COBOL'], 'codigo-editora':[1,2,3,4,5], 'codigo-autor':[1,2,3,4,5]}

# db_editora = pd.DataFrame(editora)
# db_autores = pd.DataFrame(autores)
# db_livros = pd.DataFrame(livros)
db_editora = pd.read_csv('db_editora.csv')
db_autores = pd.read_csv('db_autores.csv')
db_livros = pd.read_csv('db_livros.csv')

juntou1 = db_livros.merge(db_autores, how='inner', on=['codigo-autor'])
juntou2 = juntou1.merge(db_editora, how='inner', on=['codigo-editora'])

print(juntou2)