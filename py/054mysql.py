# python se puede usar en base de datos, una de ellas es MySQL. 
# Se debe tener instalado MySQL en la PC, primero actualice el OS:
#   sudo apt update
#   sudo apt upgrade
#   sudo apt autoremove
# Se instala el MySQL Server:
#   sudo apt install mysql-server -y
# Si desea instalar el entorno grafico
#   sudo snap install mysql-workbench-community
# Lo siguiente es cambiar el plugin de auth_socket a mysql_native_password:
#   sudo mysql -u root -p
# Las contraseñas son las mismas que usamos para sudo, en mysql usar las siguientes lineas:
#   mysql> use mysql
#   mysql> SELECT User, Host, plugin FROM mysql.user;
#   mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
#   mysql> FLUSH PRIVILEGES;
# Revisamos los cambios:
#   mysql> SELECT User, Host, plugin FROM mysql.user;
# Despues de salir (mysql> exit), generamos una contraseña para el user root:
#   mysqladmin -u root password tupassword
# Es probable que la coneccion se pueda realizar, pero es bueno habilitar la conexion ssh y Password Manager:
#   snap connect mysql-workbench-community:password-manager-service
#   snap connect mysql-workbench-community:ssh-keys
# Las instrucciones anteriores modifican el user root y es poco aconsejable, por ello, es mejor crear y dar privilegios a un usuario
# nuevo_usuario es el usuario que se va a crear y contraseña es la contraseña que le vamos a dar
#   sudo mysql -u root -p
#   CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'contraseña';
# Para otorgar todos los privilegios al nuevo_usuario usar el comando:
#   GRANT ALL PRIVILEGES ON * . * TO 'nuevo_usuario'@'localhost';
# Para que los cambios tengan efecto inmediato usar:
#   FLUSH PRIVILEGES;
# Para conectar python con mysql usar el comando:
#   pip install mysql-connector-python 

# Para probar si la conexion es funcional usar (si se ejecuta el .py sin errores, la conexion es funcional):
import mysql.connector

# lo primero es generar una coneccion con la base de datos
dataBase = mysql.connector.connect(
  host="localhost",
  # user="yourusername",
  user="prb",
  # password="yourpassword",
  password="prb"
)

# para crear una base de datos use la declaracion "CREATE DATABASE"
base1 = dataBase.cursor()
# despues de creada, genera error debido a que ya existe la base de datos, por ello, se deja comentariada
#base1.execute("CREATE DATABASE prb01")

# Para comprobar si la base existe use "SHOW DATABASES" 
base1.execute("SHOW DATABASES")

for x in base1:
  print(x)

# otra manera es accediendo a ella.
datab = mysql.connector.connect(
  host="localhost",
  user="prb",
  password="prb",
  database="prb01"
)

# para crear tablas use "CREATE TABLE", solo usar una ves para no tener problemas
mdf = datab.cursor()

#mdf.execute("CREATE TABLE persona (nombre VARCHAR(255), edad VARCHAR(255))")

# para comprobar si se creo la tabla use "SHOW TABLE"
mdf.execute("SHOW TABLES")

for x in mdf:
  print(x)

# para crear llaves primarias agregamos al campo "PRIMARY KEY", pero como la tabla existe usamos "ALTER TABLE", solo se usa una ves para no generar errores
#mdf.execute("CREATE TABLE persona (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad VARCHAR(255))")
mdf.execute("ALTER TABLE persona ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")