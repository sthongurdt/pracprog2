# Las tuplas se usan para almacenar multiples elementos en una sola variable, son colecciones ordenadas, inmutable (no se pueden cambiar) y 
# los elementos pueden estar duplicados
tpl = ('mora', 'pera', 'piña', 'kiwi', 'coco', 'higo', 'lima')
print(tpl)

# el tamaño de una tupla se obtienen de la misma manera que una lista
print(len(tpl))

tpl1 = ('hola',) # esto se considera como una tupla de un elemento
tpl2 = ('hola') # esto no es una tupla
print(tpl1, type(tpl1)) # type() nos permite ver el tipo de dato
print(tpl2, type(tpl2))

# las tuplas pueden contener diferentes tipos de datos
tpl1 = ("apple", "banana", "cherry")
tpl2 = (1, 5, 7, 9, 3)
tpl3 = (True, False, False)
tpl4 = ("abc", 34, True, 40, "male")

# una tupla se puede construir usando tuple()
tpl = tuple(('mora', 'pera', 'piña', 'kiwi', 'coco', 'higo', 'lima'))
print (tpl, type(tpl))

# el acceso de un elemento de la tupla se hace de la misma manera que una lista
print(tpl[0])
print(tpl[1])
print(tpl[-1])

# se puede acceder a segmentos de la tupla de la misma manera que las listas
print(tpl[2:5])
print(tpl[3:])
print(tpl[:-3])

# se puede verificar si se encuentra un elemento en la tupla
if 'mora' in tpl:
    print('Si, mora esta en la tupla')

# las tuplas no se pueden cambiar, pero se puede convertir en listas, modificarla y convertirla una tupla
x = ('mora', 'pera', 'piña', 'kiwi', 'coco', 'higo', 'lima')
y = list(x)
y[1] = 'limon'
x = tuple(y)
print(x)

y = list(x)
y.append('pera')
x = tuple(y)
print(x)

# dos tuplas se pueden juntar
z = ('uva',)
x += z
print(x)

# se pueden remover elementos de una tupla
y = list(x)
y.remove('limon')
x = y
print(x)

# si desea eliminar una tupla puede usar del
del x
#print(x)

# una tupla se puede desempaquetar
frt1, frt2, frt3 = tpl[2:5]
print(frt1, frt2, frt3)

# si desea desempaquetar una tupla en una cantidad menor de variables use *
frt1, *frt2 = tpl[2:]
print(frt1)
print(frt2)

frt1, *frt2, frt3 = tpl
print(frt1)
print(frt2)
print(frt3)