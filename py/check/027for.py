# for es un bucle usado para iterar una secuencia
lst = ['mora','pera','lulo']
for i in lst:
    print(i)

# una cadena puede ser recorrida por un for
for i in 'lulo':
    print(i)

#  la declaracion break puede usarse en un for
for i in lst:
    print(i)
    if i == 'pera': break

# si el break se usa antes de la ejecucion del bucle, dicha ejecucion no sera implementada
for i in lst:
    if i == 'pera': break
    print(i)

# continue detiene la iteracion actual y pasa a la siguiente
for i in lst:
    if i == 'pera': continue
    print(i)

# si el bucle for se desea realizar una cantidad determinada de veces use range()
for x in range(7):
    print(x)

for x in range(2,6): # se toma el rango entre 2 y 6, excluyendo el 6.
    print(x)

for x in range(1,31,3): # se toma el rango entre 1 y 31, y un paso de 3.
    print(x)

# else especifica un bloque de codigo despues del for
for x in range(6):
    print(x)
else: print('se acabo el for')

# for anidados
num = [1, 2, 3]
for x in num:
    for y in lst:
        print(x, y)

# pass puede ser usado para realizar un buble sin una ejecucion aparente
for i in range(6):
    pass