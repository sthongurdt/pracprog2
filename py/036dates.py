# el tiempo en python no se maneja de manera cotidiana, pero existe una libreria que ayuda con esto

import datetime as dt

x = dt.datetime.now()
print(x)

# datetime posee diferentes metodos para mostrar el tiempo
print(x.year)
print(x.strftime('%A'))

# el tiempo puede manejarse como un objeto y se construye asi:
y = dt.datetime(2022,1,20)
print(y)

# el metodo strftime() retorna diferentes formatos:
#   %a  Día de la semana, versión corta miércoles
#   %A  Día de la semana, versión completa miércoles
#   %w  Día de la semana como un número 0-6, 0 es el domingo 3
#   %d  Día del mes 01-31 31
#   %b  Nombre del mes, versión corta Dic
#   %B  Nombre del mes, versión completa Diciembre
#   %m  Mes como número 01-12 12
#   %y  Año, versión corta, sin siglo 18
#   %Y  Año, versión completa 2018
#   %H  Hora 00-23 17
#   %I  Hora 00-12 05
#   %p  AM/PM PM
#   %M  Minuto 00-59 41
#   %S  Segundo 00-59 08
#   %f  Microsegundo 000000-999999 548513
#   %z  Desplazamiento UTC +0100
#   %Z  Zona horaria CST
#   %j  Número de día del año 001-366 365
#   %U  Número de semana del año, domingo como primer día de la semana, 00-53 52
#   %W  Número de semana del año, lunes como primer día de la semana, 00-53 52
#   %c  Versión local de fecha y hora lun 31 de diciembre 17:41:00 2018
#   %C  Siglo 20
#   %x  Versión local de fecha 31/12/18
#   %X  Versión local de la hora 17:41:00
#   %% 	Un personaje 	%
#   %G ISO 8601 año 2018
#   %u ISO 8601 día laborable (1-7) 1
#   %V ISO 8601 número de semana (01-53) 01 

print(y.strftime('%B')) 
print(y.strftime('%x'))
print(y.strftime('%y'))