import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", db="ekodeadmin", host="localhost", port=3306)
print("Conexão realizada com sucesso")
db.close()