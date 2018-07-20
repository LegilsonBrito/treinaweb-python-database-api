import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(1))
print("Conexão realizada com sucesso")
db.close()