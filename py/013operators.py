# las operadores se usan para realizar operaciones entre variables y valores.

# Operadores Aritmeticos
# + Adición
# - Resta
# * Multiplicación
# / División
# % módulo
# ** Exponenciación
# // división de piso 

# Operadores de Asignacion
# =     -->     x = 5   -->     x = 5 	
# +=    -->     x += 3  -->     x = x + 3 	
# -= 	-->     x -= 3 	-->     x = x - 3 	
# *= 	-->     x *= 3  --> 	x = x * 3 	
# /= 	-->     x /= 3  -->     x = x / 3 	
# %= 	-->     x %= 3 	-->     x = x % 3 	
# //= 	-->     x //= 3 --> 	x = x // 3 	
# **= 	-->     x **= 3 --> 	x = x ** 3 	
# &= 	-->     x &= 3 	-->     x = x & 3 	
# |= 	-->     x |= 3 	-->     x = x | 3 	
# ^= 	-->     x ^= 3 	-->     x = x ^ 3 	
# >>= 	-->     x >>= 3 -->	    x = x >> 3 	
# <<= 	-->     x <<= 3 -->     x = x << 3

# Operadores de comparacion
# == 	Igual               x == y 	
# != 	Diferente 	        x != y 	
# > 	Mayor que           x > y 	
# < 	Menor que           x < y 	
# >= 	Mayor igual que     x >= y 	
# <= 	Menor igual que 	x <= y

# Operadores logicos
# and   Devuelve verdadero si ambas afirmaciones son verdaderas                             x < 5 and x < 10
# or    Devuelve verdadero si una de las afirmaciones es verdadera                          x < 5 or x < 4
# not   Invierte el resultado, devuelve Falso si el resultado es verdadero o biseversa      not(x < 5 and x < 10) 

# Operadores de identidad - compara dos objetos
# is        Devuelve verdadero si ambas variables son el mismo objeto       x is y
# is not    Devuelve verdadero si ambas variables no son el mismo objeto    x not is y

# Operadores de pertenencia
# in        Devuelve True si una secuencia con el valor especificado está presente en el objeto             x in y
# not in    Devuelve verdadero si una secuencia con el valor especificado no está presente en el objeto     x not in y 

# Operadores bit a bit
# &     AND                                     Establece cada bit en 1 si ambos bits son 1
# |     OR                                      Establece cada bit en 1 si uno de los dos bits es 1
# ^     XOR                                     Establece cada bit en 1 si solo uno de los dos bits es 1
# ~     NOT                                     Invierte todos los bits
# <<    Rellenar con ceros                      Desplazamiento a la izquierda Desplace a la izquierda empujando ceros desde la derecha y deje que los bits más a la izquierda caigan
# >>    Desplazamiento a la derecha con signo   Desplace a la derecha empujando copias del bit más a la izquierda desde la izquierda, y deje que los bits más a la derecha caigan


print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)


frutas = ["manzana", "banano"]
if "manzana" in frutas:
  print("Si, manzana es una fruta")

if 5 != 10:
  print("5 y 10 no son iguales")

if 5 == 10 or 4 == 4:
  print("Al menos una de las afirmaciones es verdadera")