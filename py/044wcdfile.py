# para crear un archivo usamos el metodo open() con los siguientes parametros:
#   x   Crear, crea el archivo y retorna un error si el archivo existe
#   a   Agregar, crea un archivo si el archivo especificado no existe
#   w   Escribir, crea un archivo si el archivo especificado no existe
fx = open('prbx.txt', 'x')
fx.write('Hola, soy prbx; ')
fx.close()

fx = open('prbx.txt', 'r')
print(fx.read())

fa = open('prba.txt', 'a')
fa.write('Hola, soy prba')
fa.close()

fa = open('prba.txt', 'r')
print(fa.read())

fw = open('prbw.txt', 'w')
fw.write('Hola, soy prbw')
fw.close()

fw = open('prbw.txt', 'r')
print(fw.read())

# si desea eliminar un archivo
import os

os.remove('prbx.txt')
os.remove('prba.txt')
os.remove('prbw.txt')

# si desea eliminar directorios (carpetas)
#os.rmdir('miCarpeta')