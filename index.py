import streamlit as st
import pandas as pd
import sqlite3 as db

conn = db.connect('DB_SISTEMA_PONTO.db')
c = conn.cursor()

query1 = """

select PRIMEIRO_NOME_FUNCIONARIO AS Nome,
SOBRENOME_FUNCIONARIO AS Sobrenome,
CPF_FUNCIONARIO AS CPF,
ORGAO_DE_ORIGEM_FUNCIONARIO AS 'Orgão de origem',
SETOR_LOTACAO_FUNCIONARIO AS "Setor"
from TBL_FUNCIONARIO
ORDER BY PRIMEIRO_NOME_FUNCIONARIO ASC;

"""
tbl_funcionario = pd.read_sql_query(query1, conn)

query2 = """

SELECT PRIMEIRO_NOME_FUNCIONARIO as Nome,
SOBRENOME_FUNCIONARIO AS Sobrenome,
TELEFONE_FUNCIONARIO AS Telefone
FROM TBL_FUNCIONARIO INNER JOIN TBL_TELEFONE_FUNCIONARIO
ON TBL_FUNCIONARIO.ID_FUNCIONARIO = TBL_TELEFONE_FUNCIONARIO.ID_FUNCIONARIO
ORDER BY PRIMEIRO_NOME_FUNCIONARIO ASC;

"""


join_telefone_funcionario= pd.read_sql_query(query2, conn)

query3 = """

SELECT PRIMEIRO_NOME_FUNCIONARIO AS Nome,
DATA_PONTO AS Data,
HORA_ENTRADA_PONTO AS "Hora de Entrada",
HORA_SAIDA_PONTO AS "Hora de Saída"
FROM TBL_FUNCIONARIO
INNER JOIN TBL_REGISTRO_PONTO
ON TBL_FUNCIONARIO.ID_FUNCIONARIO = TBL_REGISTRO_PONTO.ID_FUNCIONARIO
ORDER BY DATA_PONTO ASC;

"""


tbl_registro = pd.read_sql_query(query3, conn)

query4 = """

SELECT PRIMEIRO_NOME_FUNCIONARIO AS Nome,
DATA_PONTO AS Data,
HORA_ENTRADA_PONTO AS "Hora da Entrada",
HORA_SAIDA_PONTO AS "Hora da Saída",
TIPO_OCORRENCIA AS "Tipo da Ocorrência",
HORA_INICIO_OCORRENCIA AS "Início da Ocorrência",
HORA_FIM_OCORRENCIA AS "Fim da Ocorrência",
DESCONTO_OCORRENCIA AS "Desconto Gerado"
FROM TBL_FUNCIONARIO
INNER JOIN TBL_REGISTRO_PONTO
ON TBL_FUNCIONARIO.ID_FUNCIONARIO = TBL_REGISTRO_PONTO.ID_FUNCIONARIO
INNER JOIN TBL_OCORRENCIA_PONTO
ON TBL_REGISTRO_PONTO.ID_REGISTRO_PONTO = TBL_OCORRENCIA_PONTO.ID_REGISTRO_PONTO
ORDER BY DATA_PONTO ASC;

"""


join_registro_ocorrencia = pd.read_sql_query(query4, conn)

query5 = """

SELECT PRIMEIRO_NOME_FUNCIONARIO AS Nome,
DATA_PONTO AS Data,
HORA_ENTRADA_PONTO AS "Hora de Entrada",
HORA_SAIDA_PONTO AS "Hora de Saída"
FROM TBL_FUNCIONARIO
INNER JOIN TBL_REGISTRO_PONTO
ON TBL_FUNCIONARIO.ID_FUNCIONARIO = TBL_REGISTRO_PONTO.ID_FUNCIONARIO
where PRIMEIRO_NOME_FUNCIONARIO = "Felipe"
ORDER BY DATA_PONTO ASC;

"""


registro_mensal = pd.read_sql_query(query5, conn)


st.write("""
# Sistema de Registro de Ponto
""")
st.write("""
### Lista de Funcionários
A tabela de funcionários é um componente essencial em qualquer sistema de gerenciamento de
recursos humanos. Ela armazena informações importantes sobre os colaboradores de uma
organização, como nome, cargo, departamento, data de admissão e outras informações relevantes.
Essa tabela permite o registro e a organização dos dados pessoais e profissionais de cada
funcionário, fornecendo uma visão abrangente de todos os membros da equipe em um único lugar.
""")

st.dataframe(tbl_funcionario, hide_index = True)

st.write("""
### Telefone dos Funcionários
Ao combinar as tabelas de funcionários e telefones por meio de um join, é possível criar uma
 visão completa das informações de contato de cada funcionário. Esse join estabelece uma
 relação entre as duas tabelas, permitindo que sejam associados os telefones corretos a cada
 funcionário. Dessa forma, é possível acessar facilmente os números de telefone de todos os
 funcionários, tornando a comunicação interna e externa mais eficiente e eficaz.
""")

st.dataframe(join_telefone_funcionario, hide_index = True)

st.write("""
### Registro de Ponto
A tabela de registro de ponto é utilizada para acompanhar as marcações de entrada e saída dos
 funcionários em seus respectivos horários de trabalho. Ela registra informações como data,
 hora de entrada e saída, além de outras informações relacionadas à jornada de trabalho. Essa
 tabela é fundamental para o controle de frequência dos colaboradores e para o cálculo de horas
  trabalhadas, permitindo um monitoramento preciso da presença e do tempo de trabalho de cada
   funcionário.
""")
st.dataframe(tbl_registro, hide_index = True)
st.dataframe(registro_mensal, hide_index = True)

st.write("""
### Ocorrência
A tabela de registro de ocorrências é responsável por armazenar informações relacionadas a
 eventos excepcionais que envolvem os funcionários, como atrasos, declarações médicas,
 solicitações de folgas e outros tipos de situações similares. Essa tabela permite o registro
  detalhado de cada ocorrência, incluindo a data, o tipo de ocorrência, o funcionário envolvido
   e quaisquer observações relevantes. Com o uso dessa tabela, é possível acompanhar e
    gerenciar de forma eficiente os incidentes que ocorrem no ambiente de trabalho,
    auxiliando na tomada de decisões e na implementação de políticas e procedimentos
    adequados para lidar com cada situação específica.
""")
st.dataframe(join_registro_ocorrencia, hide_index = True)
