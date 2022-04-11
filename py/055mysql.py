# para insertar y llenar un campo use la declaracio "INSERT INTO" 
import mysql.connector

datab = mysql.connector.connect(
  host="localhost",
  user="prb",
  password="prb",
  database="prb01"
)

'''data = datab.cursor()

sql = "INSERT INTO persona (nombre, edad) VALUES (%s, %s)"
val = ("John", "21")
data.execute(sql, val)

datab.commit()

print(data.rowcount, "Datos Agregados.")'''

# para insertar multioles datos use executemany(), el parametro valuees una lista de tuplas que contiene los datos que desea insertar:
'''data = datab.cursor()
sql = "INSERT INTO persona (nombre, edad) VALUES (%s, %s)"
val = [
  ('Peter', '4'),
  ('Amy', '52'),
  ('Hannah', '21'),
  ('Michael', '34'),
  ('Sandy', '12'),
  ('Betty', '21'),
  ('Richard', '31'),
  ('Susan', '98'),
  ('Vicky', '23'),
  ('Ben', '38'),
  ('William', '54'),
  ('Chuck', '89'),
  ('Viola', '33')
]

data.executemany(sql, val)

datab.commit()

print(data.rowcount, "Se agregaron.")'''

# es posible identificar la fila que se acaba de insertar preguntando al objeto cursor().
'''data = datab.cursor()

sql = "INSERT INTO persona (nombre, edad) VALUES (%s, %s)"
val = ("Michelle", "23")
data.execute(sql, val)

datab.commit()

print("1 registro insertado, ID:", data.lastrowid)''' 