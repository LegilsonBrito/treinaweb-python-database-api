import MySQLdb

#Conectando ao banco de dados
db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)

#Criando cursor
cursor = db.cursor()
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

#TRABALHANDO COM TRANSAÇÕES
#try:
#    db.begin()
#    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Pedro', 25)")
#    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Augusto', 25)")
#    db.commit()
#except:
#    db.rollback()

#CONSULTANDO DADOS
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

#CONSULTANDO ÚLTIMO ID INSERIDO
#print(cursor.lastrowid)

#ATUALIZANDO DADOS
#cursor.execute("UPDATE cliente SET nome='Ana' WHERE idcliente=2")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

#REMOVENDO DADOS
#cursor.execute("DELETE FROM cliente WHERE idcliente=2")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

#INSERÇÃO COM PARÂMETROS SEM PREVENIR SQL INJECTION
#nome = "Antônio"
#cursor.execute(f"INSERT INTO cliente (nome, idade) VALUES ('{nome}', 25)")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

#SQL INJECTION
#nome = "'Carlos' , idade = 80"
#consulta = f"UPDATE cliente SET nome={nome} WHERE idcliente=13"
#print(consulta)
#cursor.execute(f"UPDATE cliente SET nome={nome} WHERE idcliente=13")
#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

nome = "João"
idade = 40
cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=13", ({'nome': nome, 'idade': idade}))
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

db.close()