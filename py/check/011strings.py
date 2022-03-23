# los strings se declaran usando comillas simples (''), dobles ("") o cualquier caracter diferente de un numero
print("Hello")
print('Hello')

# asignar un string a una variable
a = "Hello"
print(a) 

# String multilineal
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

# los strings son arrglos (arrays, vectores, matices lineales)
a = "Hello, World!"
print(a[1])

# recorrido de strings
for x in "banana":
  print(x)

# tamaño de un string
a = "Hello, World!"
print(len(a))

# checar si una palabra, frase o caracter se encuentra en un string se puede hacer con 'in'
txt = "The best things in life are free!"
print("he" in txt)

txt = "The best things in life are free!"
if "ee" in txt:
  print("Si, 'ee' esta presente.")

# checar si NO se encuentra una palabra, frase o caracter en un string se puede hacer con 'not in'
txt = "The best things in life are free!"
print("caro" not in txt)

txt = "The best things in life are free!"
if "caro" not in txt:
  print("Si, 'caro' NO esta presente.")

# un string se puede partir de la siguiente manera
b = "Hello, World!"
print(b[2:5])

# desde una posicion hasta el fin
b = "Hello, World!"
print(b[2:])

# usando las posiciones al reves
b = "Hello, World!"
print(b[-5:-2])

# si se desea pasar el string a mayusculas
a = "Hello, World!"
print(a.upper())

# si se desea pasar el string a minusculas
a = "Hello, World!"
print(a.lower())

# se se desea eliminar espacios en blanco antes o despues del string
a = " Hello, World! "
print(a)
print(a.strip()) # returns "Hello, World!" 

# si se desea reemplazar parte del vector
a = "Hello, World!"
print(a.replace("H", "J"))

# si se desea segmentar la matriz
a = "Hello, World!"
print(a.split(",")) # devuelve ['Hello', ' World!'] 

# si desea concatenar strings para crear uno mas grande
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# si desea concatenar strings y numeros, lo puede hacer de la siguiente manera
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# si desea indicar el orden de los numeros
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# si necesita agregar caracteres especiales use las siguientes cadenas
# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Metodos que se pueden usar con las cadenas
# capitalize() - Convierte el primer carácter a mayúsculas
# casefold() - Convierte una cadena en minúsculas
# center() - Devuelve una cadena centrada
# count() - Devuelve el número de veces que aparece un valor especificado en una cadena
# encode() - Devuelve una versión codificada de la cadena
# endswith() - Devuelve verdadero si la cadena termina con el valor especificado
# expandtabs() - Establece el tamaño de tabulación de la cadena
# find() - Busca en la cadena un valor específico y devuelve la posición donde se encontró
# format() - Formatea los valores especificados en una cadena
# format_map() - Formatea los valores especificados en una cadena
# index() - Busca en la cadena un valor específico y devuelve la posición donde se encontró
# isalnum() - Devuelve True si todos los caracteres de la cadena son alfanuméricos
# isalpha() - Devuelve True si todos los caracteres de la cadena están en el alfabeto
# isdecimal() - Devuelve True si todos los caracteres de la cadena son decimales
# isdigit() - Devuelve True si todos los caracteres de la cadena son dígitos
# isidentifier() - Devuelve True si la cadena es un identificador
# islower() - Devuelve True si todos los caracteres de la cadena están en minúsculas
# isnumeric() - Devuelve True si todos los caracteres de la cadena son numéricos
# isprintable() - Devuelve True si todos los caracteres de la cadena son imprimibles
# isspace() Devuelve True si todos los caracteres de la cadena son espacios en blanco
# istitle() Devuelve True si la cadena sigue las reglas de un título
# isupper() Devuelve True si todos los caracteres de la cadena están en mayúsculas
# join() Une los elementos de un iterable al final de la cadena
# ljust() Devuelve una versión justificada a la izquierda de la cadena
# lower() Convierte una cadena en minúsculas
# lstrip() Devuelve una versión recortada a la izquierda de la cadena
# maketrans() Devuelve una tabla de traducción para ser utilizada en las traducciones
# partición () Devuelve una tupla donde la cadena se divide en tres partes
# replace () Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
# rfind() Busca en la cadena un valor específico y devuelve la última posición donde se encontró
# rindex() Busca en la cadena un valor específico y devuelve la última posición donde se encontró
# rjust() Devuelve una versión justificada a la derecha de la cadena
# rpartition() Devuelve una tupla donde la cadena se divide en tres partes
# rsplit() Divide la cadena en el separador especificado y devuelve una lista
# rstrip() Devuelve una versión recortada a la derecha de la cadena
# split() Divide la cadena en el separador especificado y devuelve una lista
# splitlines() Divide la cadena en los saltos de línea y devuelve una lista
# comienza con () Devuelve verdadero si la cadena comienza con el valor especificado
# strip() Devuelve una versión recortada de la cadena
# swapcase() Intercambia mayúsculas y minúsculas y viceversa
# title() Convierte el primer carácter de cada palabra a mayúsculas
# translate() Devuelve una cadena traducida
# upper() Convierte una cadena en mayúsculas
# zfill() Rellena la cadena con un número específico de valores 0 al principio 





a = 'we are'
print(a.capitalize())
print(a.casefold())
print(a.center())
