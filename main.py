import MySQLdb

MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306)
print("Conexão realizada com sucesso")