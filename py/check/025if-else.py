# Python soporta los condicionales logicos:
# Igual         a == b
# Diferente     a != b
# Menor que     a < b
# Mayor que     a > b
# Menor igual   a <= b
# Mayor igual   a >= b

# Condicional if
a = 33
b = 200
if b > a:
  print("b mayor que a")

# Condicional elif
a = 33
b = 33
if b > a:
  print("b mayor que a")
elif a == b:
  print("a igual b")

# Condicional else
a = 200
b = 33
if b > a:
    print("b mayor que a")
elif a == b:
    print("a igual b")
else:
    print("a mayor que b")

# if acortado
if a > b: print('a mayor que b')

# if-else acortado
print('A') if a > b else print('B')
a = 330
b = 330
print("A") if a > b else print("Igual") if a == b else print("B")

# AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Ambos son True")

# OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("Una de las condiciones es True")

 # if anidados
x = 41
if x > 10:
  print("Por encima de 10,")
  if x > 20:
    print("y por encima de 20!")
  else:
    print("Pero no por encima de 20.") 

# si tiene un condicional if, pero no tiene nada para colocar en el, use la declaracion pass para que no se genere un error.
a = 33
b = 200
if b > a:
  pass