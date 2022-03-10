#las variables creadas fuera de una funcion se conocen como variables globales
x = "la onda"

def mifunc():
  print("Python es " + x)

mifunc()

def mifunc2():
  x = "fantastico"
  print("Python es " + x)

mifunc2()

print("Python sera " + x)

#las variables dentro de una funcion se pueden declarar globales 
def mifunc3():
  global x
  x = "fantastic"

mifunc3()

print("Python is " + x) 