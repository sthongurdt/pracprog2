# en la programacion es necesario saber si una expresion es verdadera o falsa, si se comparan dos valores el resultado es una respuesta booleana.
print(10 > 9)
print(10 == 9)
print(10 < 9)

# una comparacion if tiene un resultado booleano

a = 200
b = 33

if b > a:
  print("b es > que a")
else:
  print("b es < que a") 

# bool() permite evaluar una variable y muestra si es verdadera o falsa. Las listas, tuplas, set, numeros, cadenas son verdaderas, exepto 0 (cero) y cadenas vacias.

x = "Hello"
y = 15

print(bool("Hello"))
print(bool(15))
print(bool(x))
print(bool(y))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# una funcion puede retornar un boolean
 
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

x = 200
print(isinstance(x, int)) 