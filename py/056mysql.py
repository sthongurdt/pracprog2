# Para seleccionar elementos desde una tabla use la sentencia SELECT
import mysql.connector

datab = mysql.connector.connect(
  host="localhost",
  user="prb",
  password="prb",
  database="prb01"
)

'''data = datab.cursor()

data.execute("SELECT * FROM persona")

resp = data.fetchall()

for x in resp:
  print(x)
'''

# si solo le interesa una fila en especifico use el metodo fetchone()
'''data = datab.cursor()

data.execute("SELECT * FROM persona")

resp = data.fetchone()

print(resp)'''

# cuando se realiza una consulta es necesario usar un  un filtro, esto se realiza mediante la sentencia where
'''data = datab.cursor()

sql = "SELECT * FROM persona WHERE edad ='38'"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x)
'''

# los caracteres comodin pueden usarse iniciando o finalizando letrar, palabras o frases
'''data = datab.cursor()

sql = "SELECT * FROM persona WHERE nombre like '%nn%'"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x)
'''

# el metodo mysql.connector realiza scape para evitar la inyeccion sql
'''data = datab.cursor()

sql = "SELECT * FROM persona WHERE nombre = '%s'"
nom = ("%nn%", )

data.execute(sql, nom)

resp = data.fetchall()

for x in resp:
  print(x)
'''

# los resultados pueden ordenarse de manera ascendente
'''data = datab.cursor()

sql = "SELECT * FROM persona ORDER BY nombre"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x)
'''

# o descendente
'''data = datab.cursor()

sql = "SELECT * FROM persona ORDER BY nombre DESC"

data.execute(sql)

resp = data.fetchall()

for x in resp:
  print(x)
'''

# Los registros de una tabla pueden ser eliminados 
'''data = datab.cursor()

sql = "DELETE FROM persona WHERE edad = '4'"

data.execute(sql)

datab.commit()

print(data.rowcount, "Registro(s) Eliminado(s)")
'''
#Para prevenir la inyeccion 
'''data = datab.cursor()

sql = "DELETE FROM persona WHERE nombre = %s"
adr = ("Viola", )

data.execute(sql, adr)
datab.commit()

print(data.rowcount, "Registro(s) Eliminado(s)") 
'''

# Las tablas de una base pueden ser eliminadas usando DROP TABLE
'''data = datab.cursor()

sql = "DROP TABLE persona"

data.execute(sql)
'''

# se puede ser mas selectivo al eliminar una tabla si solo existe con la declaracion IF EXISTS
'''data = datab.cursor()

sql = "DROP TABLE IF EXISTS persona"

data.execute(sql)
'''

# los datos de una tabla se puede actualizar con la declaracion UPDATE
'''data = datab.cursor()

sql = "UPDATE persona SET edad = '12' WHERE edad = '4'"

data.execute(sql)

datab.commit()

print(data.rowcount, "Registro(s) Cambiado(s)") 
'''

# Para prevenir la inyeccion
'''data = datab.cursor()

sql = "UPDATE persona SET edad = %s WHERE edad = %s"
val = ('12', '98')

data.execute(sql, val)

datab.commit()

print(data.rowcount, "Registro(s) Cambiado(s)") 
'''

# los resultados pueden limitarse usando la declaracion LIMIT
'''data = datab.cursor()

data.execute("SELECT * FROM persona LIMIT 5")

resp = data.fetchall()

for x in resp:
  print(x)
'''

# si desea iniciarlo desde otra posicion use la declaracion OFFSET
'''data = datab.cursor()

data.execute("SELECT * FROM persona LIMIT 5 OFFSET 5")

resp = data.fetchall()

for x in resp:
  print(x) 
'''