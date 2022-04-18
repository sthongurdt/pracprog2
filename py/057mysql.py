# las tablas pueden juntarse en una consulta con la declaracion join
import mysql.connector

datab = mysql.connector.connect(
  host="localhost",
  user="prb",
  password="prb",
  database="prb01"
)

data = datab.cursor()

# Agregamos 2 tablas nuevas, con sus datos
'''data.execute("CREATE TABLE usuario (id INT PRIMARY KEY, nombre VARCHAR(255), fav VARCHAR(255))")

data.execute("CREATE TABLE producto (id INT PRIMARY KEY, nombre VARCHAR(255))")

data.execute("ALTER TABLE usuario MODIFY COLUMN id INT AUTO_INCREMENT")

data.execute("SHOW TABLES")

for x in data:
  print(x)

sql = "INSERT INTO usuario (nombre, fav) VALUES (%s, %s)"
val = [
  ('John', '154'),
  ('Peter', '154'),
  ('Amy', '155'),
  ('Hannah', ''),
  ('Michael', '')
]

data.executemany(sql, val)

datab.commit()

print(data.rowcount, "Registro(s) Agregado(s).")

sql = "INSERT INTO producto (id, nombre) VALUES (%s, %s)"
val = [
  (154, 'Chocolate Heaven'),
  (155, 'Tasty Lemons'),
  (156, 'Vanilla Dreams')
]

data.executemany(sql, val)

datab.commit()

print(data.rowcount, "Registro(s) Agregado(s).")

data = datab.cursor()
data.execute("SELECT * FROM usuario")
resp = data.fetchall()
for x in resp:
  print(x)

data = datab.cursor()
data.execute("SELECT * FROM producto")
resp = data.fetchall()
for x in resp:
  print(x)
'''

# ambas tablas pueden combinarse usando el campo fav
data = datab.cursor()

sql = "SELECT \
  usuario.nombre AS us, \
  producto.nombre AS favorito \
  FROM usuario \
  INNER JOIN producto ON usuario.fav = producto.id"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x) 

# INNER JOIN solo muestra los registros que coinciden, LEFT JOIN nos permitiria ver los usuarios aunque no coincidan los favoritos
data = datab.cursor()

sql = "SELECT \
  usuario.nombre AS us, \
  producto.nombre AS favorito \
  FROM usuario \
  LEFT JOIN producto ON usuario.fav = producto.id"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x) 

# si desea devolver todos los productos y usuarios que los tienen como favoritos use RIGHT JOIN
data = datab.cursor()

sql = "SELECT \
  usuario.nombre AS us, \
  producto.nombre AS favorito \
  FROM usuario \
  RIGHT JOIN producto ON usuario.fav = producto.id"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x) 