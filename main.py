import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306, autocommit=False)
cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
print("Conexão realizada com sucesso")
try:
    db.begin()
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Pedro', 25)")
    cursor.execute("INSERT INTO cliente (nomes, idade) VALUES ('Augusto', 25)")
    db.commit()
except:
    db.rollback()
cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())
#print(cursor.lastrowid)
#cursor.execute("UPDATE cliente SET nome='Ana' WHERE idcliente=2")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())
#cursor.execute("DELETE FROM cliente WHERE idcliente=2")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())
db.close()