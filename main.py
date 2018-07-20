import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306)
cursor = db.cursor()
print("Conexão realizada com sucesso")
db.close()