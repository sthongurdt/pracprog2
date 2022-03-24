# las expresiones regulares son una secuencia de caracteres que forman un camino de busqueda
# python tiene integrado un paquete para manejarlas
import re

t = 'la lluvia en colombia'
x = re.search('^la.*colombia$', t)
print(x)

# las funciones de re son:
#   findall Devuelve una lista que contiene todas las coincidencias
#   search  Devuelve un objeto Match si hay una coincidencia en cualquier parte de la cadena
#   split   Devuelve una lista donde la cadena se ha dividido en cada coincidencia
#   sub     Reemplaza una o varias coincidencias con una cadena

# los metacaracteres tienen un significado especial
#   []  Un conjunto de caracteres   "[a-m]"
x = re.findall("[a-m]", t)
print(x)

#   \   Señala una secuencia especial (también se puede usar para escapar de caracteres especiales) "\d"
x = re.findall("\d", t)
print(x)

#   .   Cualquier carácter (excepto el carácter de nueva línea) "he..o"
x = re.findall("ll..a", t)
print(x)

#   ^   Comienza con "^hola"
x = re.findall("^lluvia", t)
if x:
  print('si')
else:
  print('no')

#   $   Termina con "mundo$"
x = re.findall("colombia$", t)
if x:
  print("si")
else:
  print("no")

#   *   Cero o más ocurrencias de "h.*a"
x = re.findall("ll.*a", t)
print(x)

#   +   Una o más apariciones "h.+a"
x = re.findall("ll.+a", t)
print(x)

#   ?   Cero o una aparición de "h.?a"
x = re.findall("ll.?a", t)
print(x)

#   {}  Exactamente el número especificado de ocurrencias "h.{2}o"
x = re.findall("ll.{2}a", t)
print(x)

#   |   Cualquiera "cae|mantiene"
x = re.findall("en|cae", t)
print(x)
if x:
  print("si, al menos una coincidencia")
else:
  print("no")

#   ()  Capturar y agrupar



# Secuencuas especiales:
#   \A      Devuelve una coincidencia si los caracteres especificados están al principio de la cadena "\AThe"
x = re.findall("\Ala", t)
print(x)

#   \b      Devuelve una coincidencia donde los caracteres especificados están al principio o al final de una palabra (la "r" al principio se 
#           asegura de que la cadena se trate como una "cadena sin procesar") r"\bain"  r "lluvia\b"
x = re.findall(r"\bvia", t)
print(x)
x = re.findall(r"via\b", t)
print(x)

#   \B      Devuelve una coincidencia en la que están presentes los caracteres especificados, pero NO al principio (o al final) de una palabra
#           (la "r" al principio se asegura de que la cadena se trate como una "cadena sin procesar") r"\Bain"  r "lluvia\B"
x = re.findall(r"\Bvia", t)
print(x)
x = re.findall(r"via\B", t)
print(x)

#   \d      Devuelve una coincidencia donde la cadena contiene dígitos (números del 0 al 9) "\d"
x = re.findall("\d", t)
print(x)

#   \D      Devuelve una coincidencia donde la cadena NO contiene dígitos "\D"
x = re.findall("\D", t)
print(x)

#   \s      Devuelve una coincidencia donde la cadena contiene un carácter de espacio en blanco "\s"
x = re.findall("\s", t)
print(x)

#   \S      Devuelve una coincidencia en la que la cadena NO contiene un carácter de espacio en blanco "\S"
x = re.findall("\S", t)
print(x)

#   \w      Devuelve una coincidencia en la que la cadena contiene cualquier palabra (caracteres de la A a la Z, dígitos del 0 al 9 y el carácter de subrayado _) "\w"
x = re.findall("\w", t)
print(x)

#   \W      Devuelve una coincidencia donde la cadena NO contiene ningún carácter de palabra "\W"
x = re.findall("\W", t)
print(x)

#   \Z      Devuelve una coincidencia si los caracteres especificados están al final de la cadena "España\Z"
x = re.findall("colombia\Z", t)
print(x)


# los conjuntos son caracteres encerrados entre []
#   [arn]       Devuelve una coincidencia en la que está presente uno de los caracteres especificados (a, r o n)
t = 'hola mundo'
x = re.findall("[arn]", t)
print(x)

#   [a-n]       Devuelve una coincidencia para cualquier carácter en minúscula, alfabéticamente entre a y n
x = re.findall("[a-n]", t)
print(x)

#   [^arn]      Devuelve una coincidencia para cualquier carácter EXCEPTO a, r y n
x = re.findall("[^arn]", t)
print(x)

#   [0123]      Devuelve una coincidencia donde cualquiera de los dígitos especificados (0, 1, 2 o 3) está presente
x = re.findall("[0123]", t)
print(x)

#   [0-9]       Devuelve una coincidencia para cualquier dígito entre 0 y 9
x = re.findall("[0-9]", t)
print(x)

#   [0-5][0-9]  Devuelve una coincidencia para cualquier número de dos dígitos entre 00 y 59
x = re.findall("[0-5][0-9]", t)
print(x)

#   [a-zA-Z]    Devuelve una coincidencia para cualquier carácter alfabéticamente entre a y z, minúsculas O mayúsculas 
x = re.findall("[a-zA-Z]", t)
print(x)

#   [+]         En conjuntos, +, *, ., |, (), $,{} no tiene un significado especial, por lo que [+] significa: devolver 
#               una coincidencia para cualquier carácter + en la cadena
t = '5 pa las 9:00 AM'
x = re.findall("[+]", t)
print(x)


# la funcion findall() retorna una lista que contiene todas las coincidencias
t = "Llueve en Colombia"
x = re.findall("ia", t)
print(x) 

t = "La lluvia"
x = re.findall("Colombia", t)
print(x)

# la funcion search() busca coincidencia en la cadena y devuelve un objeto match si la hay. Solo se devuelve la primera coincidencia
t = "La lluvia en Latinoamerica"
x = re.search("\s", t)
print("El primer caracter de espacio en blanco se encuentra en la posicion:", x.start())

x = re.search("Portugal", t)
print(x) 

# La función split() devuelve una lista en la que la cadena se ha dividido en cada coincidencia: 
t = "La lluvia en Latinoamerica"
x = re.split("\s", t)
print(x)

# Se puede controlar el número de ocurrencias especificando el parámetro maxsplit: 
x = re.split("\s", t, 1)
print(x) 

# La función sub() reemplaza las coincidencias con el texto de su elección:
x = re.sub("\s", "9", t)
print(x) 

# Se puede controlar la cantidad de reemplazos especificando el parámetro de conteo:
x = re.sub("\s", "9", t, 2)
print(x) 

# Un objeto Match es un objeto que contiene información sobre la búsqueda y el resultado.
# El objeto Match tiene propiedades y métodos que se utilizan para recuperar información sobre la búsqueda y el resultado:
#   .span() devuelve una tupla que contiene las posiciones inicial y final de la coincidencia.
#   .string devuelve la cadena pasada a la función
#   .group() devuelve la parte de la cadena donde hubo una coincidencia 

t = "La lluvia en Latinoamerica"
x = re.search(r"\bL\w+", t)
print(x.span())

x = re.search(r"\bL\w+", t)
print(x.string)

x = re.search(r"\bL\w+", t)
print(x.group()) 