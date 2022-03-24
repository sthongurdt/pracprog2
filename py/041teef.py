#   try         Permite probar codigo en busca de errores
#   except      Permite manejar el error
#   else        Permite ejecutar codigo cuando no hay errores
#   finally     Permite ejecutar codigo independiente del resultado de try y except
'''
# Cuando ocurre un error, python normalmente se detendrá y generará un mensaje de error.
# Estas excepciones se pueden manejar usando try:
try:
  print(x)
except:
  print("Ha ocurrido algo")

# Imprima un mensaje si se genera un NameError y otro para otros errores
try:
  print(x)
except NameError:
  print("La variable no esta definida")
except:
  print("Algo mas fallo") 

# else se usa para ejecutar codigo si no se encuentra errores
try:
  print("Hola mundo")
except:
  print("Algo fallo")
else:
  print("No fallo nada")

# finally se ejecuta independientemente si se genera un error o no.
try:
  print(x)
except:
  print("Ha ocurrido algo")
finally:
  print("try-except finalizo")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Algo salio mal al escribir en el archivo")
  finally:
    f.close()
except:
  print("Algo salio mal al abrir el archivo ") 

# Se puede optar por generar una excepción si se produce una condición. Para lanzar (o generar) una excepción, use la palabra clave raise. 
x = -1

if x < 0:
  raise Exception("Paila, el numero no puede ser menor a cero")

x = "hola"

if not type(x) is int:
  raise TypeError("Solo se permiten enteros")  
'''
