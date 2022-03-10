# copiar una lista se realiza usando copy(), si lst = lst1, lst1 hace una referencia a lst.
lst = ['mora', 'pera', 'mango', 'piña', 'kiwi', 'coco', 'higo', 'lima', 'uva', 'datil', 'fresa', 'sandia']
lst1 = lst.copy()
print(lst1)

# otra manera de copiar es usando el constructor list()
lst2 = list(lst)
print(lst2)

# Si desea juntar dos cadenas
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst = lst1 + lst2
print(lst)

# otra manera de juntar las cadenas es
for x in lst2:
    lst1.append(x)
print(lst1)

# otra manera es usar extend()
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst1.extend(lst2)
print(lst1)

# la lista de metodos de las cadenas es la siguiente:
# append()  Agrega un elemento al final de la lista
# clear()   Elimina todos los elementos de la lista
# copy()    Devuelve una copia de la lista
# count()   Devuelve el número de elementos con el valor especificado
# extend () Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
# index()   Devuelve el índice del primer elemento con el valor especificado
# insert()  Agrega un elemento en la posición especificada
# pop()     Elimina el elemento en la posición especificada
# remove()  Elimina el elemento con el valor especificado
# reverse() Invierte el orden de la lista
# sort()    Ordena la lista 
