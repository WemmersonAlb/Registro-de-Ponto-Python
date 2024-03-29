import pandas as pd
import sqlite3 as db

conn = db.connect('DB_SISTEMA_PONTO.db')
c = conn.cursor()

#           Criando Tabelas


# FUNCIONARIO
c.execute("""
    CREATE TABLE IF NOT EXISTS TBL_FUNCIONARIO (
        ID_FUNCIONARIO INTEGER PRIMARY KEY,
        PRIMEIRO_NOME_FUNCIONARIO VARCHAR(50) NOT NULL,
        SOBRENOME_FUNCIONARIO VARCHAR(200) NOT NULL,
        DATA_NASCIMENTO_FUNCIONARIO DATE NOT NULL,
        CPF_FUNCIONARIO VARCHAR(11) NOT NULL,
        PISPASEP_FUNCIONARIO VARCHAR(11) NOT NULL,
        MATRICULA_FUNCIONARIO VARCHAR(10) NOT NULL,
        VINCULO_FUNCIONARIO VARCHAR(12) NOT NULL,
        ORGAO_DE_ORIGEM_FUNCIONARIO VARCHAR(16),
        SETOR_LOTACAO_FUNCIONARIO VARCHAR(20) NOT NULL,
        CARGO_FUNCIONARIO VARCHAR(8) NOT NULL,
        CEP_FUNCIONARIO VARCHAR(8) NOT NULL,
        LOGRADOURO_FUNCIONARIO VARCHAR(20) NOT NULL,
        NUMERO_RESIDENCIA_FUNCIONARIO VARCHAR(4),
        COMPLEMENTO_FUNCIONARIO VARCHAR(40),
        BAIRRO_FUNCIONARIO VARCHAR(20) NOT NULL,
        CIDADE_FUNCIONARIO VARCHAR(20) NOT NULL,
        VALE_TRANSPORTE VARCHAR(6) NOT NULL,
        QTD_FILHOS VARCHAR(2)
    );

""")
# TELEFONE FUNCIONARIO
c.execute("""
    CREATE TABLE IF NOT EXISTS TBL_TELEFONE_FUNCIONARIO (
        ID_FUNCIONARIO SMALLINT NOT NULL,
        TELEFONE_FUNCIONARIO VARCHAR(11) NOT NULL,
        PRIMARY KEY (ID_FUNCIONARIO, TELEFONE_FUNCIONARIO),
        CONSTRAINT FK_ID_FUNCIONARIO FOREIGN KEY (ID_FUNCIONARIO) REFERENCES TBL_FUNCIONARIO (ID_FUNCIONARIO)
    );

""")
# REGISTRO PONTO
c.execute("""
    CREATE TABLE IF NOT EXISTS TBL_REGISTRO_PONTO (
        ID_REGISTRO_PONTO INTEGER PRIMARY KEY,
        ID_FUNCIONARIO SMALLINT NOT NULL,
        DATA_PONTO DATE NOT NULL,
        HORA_ENTRADA_PONTO TIME NOT NULL,
        HORA_SAIDA_PONTO TIME NOT NULL,
        CONSTRAINT FK_ID_FUNCIONARIO01 FOREIGN KEY (ID_FUNCIONARIO) REFERENCES TBL_FUNCIONARIO (ID_FUNCIONARIO)
    );

""")
# OCORRENIA PONTO
c.execute("""
    CREATE TABLE IF NOT EXISTS TBL_OCORRENCIA_PONTO (
        ID_REGISTRO_PONTO SMALLINT NOT NULL,
        TIPO_OCORRENCIA VARCHAR(20) NOT NULL,
        HORA_INICIO_OCORRENCIA TIME NOT NULL,
        HORA_FIM_OCORRENCIA TIME NOT NULL,
        DESCONTO_OCORRENCIA DECIMAL(10,2),
        PRIMARY KEY (ID_REGISTRO_PONTO, TIPO_OCORRENCIA, HORA_INICIO_OCORRENCIA, HORA_FIM_OCORRENCIA),
        CONSTRAINT FK_ID_REGISTRO_PONTO FOREIGN KEY (ID_REGISTRO_PONTO) REFERENCES TBL_REGISTRO_PONTO (ID_REGISTRO_PONTO)
    );

""")
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())


#     Inserindo Dados


funcionarios = [(1, 'Felipe', 'Lima', '1994-12-08', '11122233345', '66677788890', '12345', 'clt', 'sad', 'administração', 'CTD', '5400000', 'Rua 01', 's/n', 'casa verde', 'Recife Antigo', 'Recife', '2a2b', 0),
(2, 'Maria', 'Silva', '1985-05-20', '22233344456', '77788899901', '54321', 'clt', 'funape', 'contabilidade', 'CTD', '5500000', 'Rua 02', '100', 'casa azul', 'Centro', 'Recife', '1b2a', 0),
(3, 'João', 'Santos', '1992-08-15', '33344455567', '88899900012', '67890', 'est', 'compesa', 'administração', 'CTD', '5600000', 'Rua 03', '250', 'casa amarela', 'Boa Viagem', 'Recife', '1a1a', 0),
(4, 'Ana', 'Pereira', '1997-03-10', '44455566678', '99900011123', '98765', 'clt', 'compesa', 'rh', 'CTD', '5700000', 'Rua 04', '50', 'casa laranja', 'Pina', 'Recife', '3b3b', 0),
(5, 'Carlos', 'Gomes', '1988-11-25', '55566677789', '00011122234', '76543', 'est', 'detran', 'administração', 'CTD', '5800000', 'Rua 05', '75', 'casa roxa', 'Madalena', 'Recife', '2a2a', 0),
(6, 'Juliana', 'Rodrigues', '1990-09-18', '66677788890', '11122233345', '23456', 'clt', 'seteq', 'contabilidade', 'CTD', '5900000', 'Rua 06', '300', 'casa marrom', 'Candeias', 'Jaboatão', '1b1b', 0),
(7, 'Pedro', 'Ferreira', '1995-07-12', '77788899901', '22233344456', '54321', 'clt', 'detran', 'rh', 'CTD', '6000000', 'Rua 07', '85', 'casa branca', 'Barro', 'Jaboatão', '2b2b', 0),
(8, 'Mariana', 'Rocha', '1983-04-05', '88899900012', '33344455567', '67890', 'est', 'sad', 'administração', 'CTD', '6100000', 'Rua 08', '150', 'casa cinza', 'Cavaleiro', 'Jaboatão', '1a1a', 0)]

c.executemany("INSERT INTO TBL_FUNCIONARIO VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", funcionarios)

telefones = [(6, '819123456'),
(4, '819987654'),
(5, '819654321'),
(3, '819456789'),
(8, '819999999'),
(2, '819111111'),
(7, '819333333'),
(1, '819888888'),
(3, '819222222'),
(6, '819777777'),
(5, '819444444'),
(2, '819666666'),
(4, '819555555'),
(8, '819000000'),
(7, '819111111'),
(1, '819222222'),
(6, '819333333'),
(3, '819444444'),
(2, '819555555'),
(5, '819666666')]

c.executemany("INSERT INTO TBL_TELEFONE_FUNCIONARIO VALUES (?,?)", telefones)

registros = [(1, 1, '2023-05-12', '07:20:00', '13:00:00'),
(2, 2, '2023-05-12', '07:25:00', '13:10:00'),
(3, 3, '2023-05-12', '07:30:00', '13:20:00'),
(4, 4, '2023-05-12', '07:35:00', '13:30:00'),
(5, 5, '2023-05-12', '07:40:00', '13:40:00'),
(6, 6, '2023-05-12', '07:45:00', '13:50:00'),
(7, 7, '2023-05-12', '07:50:00', '14:00:00'),
(8, 8, '2023-05-12', '07:55:00', '14:10:00'),
(9, 1, '2023-05-13', '07:20:00', '13:00:00'),
(10, 2, '2023-05-13', '07:25:00', '13:10:00'),
(11, 3, '2023-05-13', '07:30:00', '13:20:00'),
(12, 4, '2023-05-13', '07:35:00', '13:30:00'),
(13, 5, '2023-05-13', '07:40:00', '13:40:00'),
(14, 6, '2023-05-13', '07:45:00', '13:50:00'),
(15, 7, '2023-05-13', '07:50:00', '14:00:00'),
(16, 8, '2023-05-13', '07:55:00', '14:10:00'),
(17, 1, '2023-05-14', '07:20:00', '13:00:00'),
(18, 2, '2023-05-14', '07:25:00', '13:10:00'),
(19, 3, '2023-05-14', '07:30:00', '13:20:00'),
(20, 4, '2023-05-14', '07:35:00', '13:30:00'),
(21, 5, '2023-05-14', '07:40:00', '13:40:00'),
(22, 6, '2023-05-14', '07:45:00', '13:50:00'),
(23, 7, '2023-05-14', '07:50:00', '14:00:00'),
(24, 8, '2023-05-14', '07:55:00', '14:10:00')]

c.executemany("INSERT INTO TBL_REGISTRO_PONTO VALUES (?,?,?,?,?)", registros)

ocorrencias = [(1, 'Saida Antecipada', '13:00:00', '14:00:00', 6.00),
(2, 'Saída Antecipada', '13:10:00', '14:00:00', 5.50),
(3, 'Saída Antecipada', '13:20:00', '14:00:00', 4.50),
(4, 'Comp. Médico', '13:30:00', '14:00:00', 0),
(5, 'Saída Antecipada', '13:40:00', '14:00:00', 2.50),
(6, 'Atraso abonado', '07:40:00', '07:45:00', 0),
(6, 'Saída Antecipada', '13:45:00', '14:00:00', 1.50)]

c.executemany("INSERT INTO TBL_OCORRENCIA_PONTO VALUES (?,?,?,?,?)", ocorrencias)


conn.commit()
c.close()
conn.close()
