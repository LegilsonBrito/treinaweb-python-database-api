import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
print("Conexão realizada com sucesso")
cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Maria', 25)")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
print(cursor.lastrowid)
db.close()