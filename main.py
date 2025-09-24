from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from load dontenv import load_dontenv

bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password=senha,
    database='bd_python'
)