from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()
senha = os.getenv('SENHA_SQL')

try:
    bd_conexao = connection.MySQLConnection(
        host='localhost',
        user='root',
        password=senha,
        database='bd_python'
    )
    print("Conexão bem sucedida!")
except mysql.connector.Error as erro:
    if erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha incorretos!")
    else:
        print(erro)

comando = bd_conexao.cursor()
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado: 
    print(linha)

## INSERIR ALUNO
sql_insert = "INSERT INTO ALUNOS (nome, ano) VALUES (%s, %s)"
valores1 = ('Leonardo', '3 TEC')
valores2 = ('João', '2 TEC')

comando.execute(sql_insert, valores1)
comando.execute(sql_insert, valores2)

print("\n===TESTE INSERT===\n")
comando = bd_conexao.cursor()
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado: 
    print(linha)

##SEMPRE FECHAR A CONEXÃO
comando.close()
bd_conexao.commit()
bd_conexao.close()