# Manejar archivos es importante para cualquier app, python tiene varias funciones para el CRUD (Create, Read, Update, Delete)
# open() es la principal funcion para trabajar con archivos, toma dos argumentos: nombre del archivo y modo.
# Existen 4 modos de abrir un archivo:
#   r   Lectura - Valor predeterminado. Abre un archivo para lectura, error si el archivo no existe
#   a   Agregar - Abre un archivo para agregar, crea el archivo si no existe
#   w   Escribir - Abre un archivo para escribir, crea el archivo si no existe
#   x   Create - Crea el archivo especificado, devuelve un error si el archivo existe
# Se puede especificar si el archivo debe manejarse como modo binario o de texto.
#   t   Texto - Valor por defecto. Modo de texto
#   b   Binario - Modo binario (por ejemplo, imágenes) 
f = open('/home/prb/prb/pracprog2/py/prb.txt', "r")

# La función open() devuelve un objeto de archivo, que tiene un método read() para leer el contenido del archivo: 
#print(f.read()) 

# el método read() devuelve el texto completo, pero también puede especificar cuántos caracteres desea devolver:
#print(f.read(5))

# Puedes devolver una línea usando el método readline(): 
print(f.readline())

# Al llamar a readline() dos veces, puede leer las dos primeras líneas
print(f.readline()) 

# Al recorrer las líneas del archivo, puede leer el archivo completo, línea por línea: 
for x in f.readline():
  print(x) 

# Es una buena práctica cerrar siempre el archivo cuando haya terminado con él. 
f.close()