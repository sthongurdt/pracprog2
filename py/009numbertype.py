# los tres tipos de numeros basicos son: enteros, flotantes y complejos
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# los enteros son numeros positivos y negativos (+-) sin decimales
x = 1
y = 3565622256
z = -3255522
print(type(x))
print(type(y))
print(type(z)) 

# los flotantes son numeros (+-) con decimales
x = 1.101
y = 1.1
z = -35.59
print(type(x))
print(type(y))
print(type(z)) 

# los flotantes se pueden expresar en notacion cientifica con la 'e' o 'E'
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z)) 

# los complejos son numeros que tienen una parte imaginaria expresada con una 'j'
x = 3+5j
y = 5j
z = -20-5j
print(type(x))
print(type(y))
print(type(z))

# las conversiones se logran fijando el tipo de dato a una variable
x = 12          # int
y = 42.8        # float
z = -4+5j       # complex
a = float(x)    #convierte entero en flotante
b = int(y)      #convierte flotante en entero
c = complex(x)  #convierte entero en complejo
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c)) 

# si desea trabajar con numero aleatorios importe la libreria random
import random
print (random.randrange(1,10))