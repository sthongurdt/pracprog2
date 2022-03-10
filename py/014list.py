# Las listas permiten almacenar miltiples datos en una variable, las listas, tuplas, set, diccionario son colecciones de datos.
# Las listas estan ordenadas, son modificables y sus valores pueden estar duplicados. Si se agrega un valor se hara en la ultima posicion.
lst = ['fresa', 'pera', 'piña']
print(lst)

# si se desea ver el tamaño de una lista
print(len(lst))

# las lista pueden contener cualquier tipo de dato
lst1 = ['fresa', 'pera', 'piña']
lst2 = [1, 5, 7, 9, 3]
lst3 = [True, False, False]
lst4 = ['abc', 34, True, 40, 'malo']
print(type(lst1))
print(type(lst4))

# es posible usar el constructor list() para crear una lista
lst5 = list(('abc', 34, True, 40, 'malo'))
print(lst5)

# los elementos de una lista pueden ser accedidos por medio de sus indices
print(lst[0])
print(lst[1])

# los indices pueden ser positivos (se recorre la lista de izquierda a derecha) o negativos (se recorre de derecha a izquierda)
lst = ['mora', 'pera', 'piña', 'kiwi', 'coco', 'higo', 'lima']
print(lst[0], lst[1], lst[2])
print(lst[-1], lst[-2], lst[-3])

# los indices puden usarse como rango para definir un segmento de una lista
print(lst[2:5])

# si se desea tomar el segemeto desde el inicio hasta un indice
print(lst[:3])

# si desea segmentar desde un indice hasta el final
print(lst[3:])

# si se desea segmentar con indices negativos
print(lst[-4:-1])

# si desea buscar un elemento en una lista
if 'mora' in lst:
    print('Si, mora esta en la lista')

# los valores en una lista se pueden cambiar, la forma mas simple es usando los indices
print(lst)
lst[1] = 'uva'
print(lst)

# se puede cambiar un segmento de la lista
lst[1:3] = ['pera', 'mango']
print(lst)

# para insertar un elemento en la lista use insert()
lst.insert(3, 'piña')
print(lst)

# si desea agregar un elemento a la lista use append()
lst.append('uva')
print(lst)

# si desea adicionar una lista a otra use extend(), extend() puede adicionar cualquier objeto a la lista (tuplas, sets, diccionarios, etc.).
lst1 = ['datil', 'fresa', 'sandia']
lst.extend(lst1)
print(lst)

# si desea eliminar elementos de una lista use remove()
lst.remove('coco')
print(lst)

# si desea eliminar un indice especifico, sino se especifica el indice se elimina el ultimo elemento
lst.pop(2)
print(lst)

# tambien se puede eliminar un indice con la palabra del, sino se especifica el indice se elimina toda la lista (del lst).
del lst[2]
print(lst)

# si desea eliminar los elementos de una lista use clear() 
lst1.clear()
print(lst1)