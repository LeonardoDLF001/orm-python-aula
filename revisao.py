from mysql.connector import connection
import os
from dotenv import load_dotenv

load_dotenv()
senha_bd = os.getenv('SENHA_SQL')
print(senha_bd)



conexao_bd = connection.MySQLConnection(
    host='localhost',
    user='root',
    password= senha_bd,
    database='bd_python'
)

comando = conexao_bd.cursor()
print(comando)
comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
print(resultado)

comando.close()
conexao_bd.close()