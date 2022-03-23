# los arrays son usados para almacenar multiples valores en una sola variable
lst = ['mora','coco','lulo']
print(lst)

# los elementos pueden ser accedidos de la siguiente manera
x = lst[0]
print(x)

# los elementos pueden ser modificado de la siguiente manera
lst[0] = 'pera'
print(lst)

# la cantidad de elementos de un arrays se puede ver de la siguiente manera
print(len(lst))

# si desea recorer el array con un bucle lo puede hacer asi
for i in lst:
    print(i) 

# si desea agregar un elemento al final de la lista
lst.append('mora')
print(lst)

# si desea eliminar un elemento por su indice
lst.pop(1)
print(lst)

# si desea eliminar un elemento por su valor
lst.remove('lulo')
print(lst)

# Estos son todos los metodos del array:
# append() Agrega un elemento al final de la lista
# clear() Elimina todos los elementos de la lista
# copy() Devuelve una copia de la lista
# count() Devuelve el número de elementos con el valor especificado
# extend() Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
# index() Devuelve el índice del primer elemento con el valor especificado
# insert() Agrega un elemento en la posición especificada
# pop() Elimina el elemento en la posición especificada
# remove() Elimina el primer elemento con el valor especificado
# reverse() Invierte el orden de la lista
# sort() Ordena la lista
#