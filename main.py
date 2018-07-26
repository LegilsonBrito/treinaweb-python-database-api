import MySQLdb, cliente

#Conectando ao banco de dados
db = MySQLdb.connect(user="root", passwd="root", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)

#Criando cursor
cursor = db.cursor()

def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())

def inserir_cliente(cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s, %s)", (cliente.nome, cliente.idade))

def editar_cliente(id_cliente, cliente):
    cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                   ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))

def remover_cliente(id_cliente):
    cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente, ))

cliente = cliente.Cliente("João", 26)

listar_clientes()
inserir_cliente(cliente)
editar_cliente(3, cliente)
remover_cliente(6)

db.close()