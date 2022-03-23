# los sets almacenan elementos en una variable simple, de la misma manera que las tuplas y las listas. Los sets son colecciones sin orden, incambiables y sin indices.
# Aunque no se pueden cambiar, se puede remover y adicionar elementos. Ademas, los sets no tienen elementos duplicados.
set = {'mora', 'limon', 'piña', 'kiwi'}
print(set, type(set))

set1 = {'mora', 'limon', 'piña', 'kiwi', 'mora'}
print(set1, type(set1)) # con type() se puede evidenciar el tipo de dato

# si desea ver el tamaño de un set
print(len(set))

# los sets pueden almacenar multiples tipos de datos
set1 = {'mora', 'limon', 'piña'}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {'abc', 34, True, 40, 'malo'}

# se puede construir un set con set()
#elset = set(("mora", "limon", "piña"))
#print(elset, type(elset))

# si desea agregar un elemento al set use add()
set.add('uva')
print(set)

#si desea juntar dos cadenas use update()
set1 = {'coco', 'higo', 'lima', 'pera'}
set.update(set1)
print(set)

# los elemento adicionados por update() no tiene que ser solo sets
set.update(set2)
print(set)

# si desea eliminar un elemento del set use remove()
set.remove(1)
print(set)

# se puede remover un elemento usando discard()
set.discard('kiwi')
print(set)

# se puede eliminar elemento con pop(), pero solo sera el ultimo elemnto del set
set.pop()
print(set)

# si desea limpiar el set use clear()
set1.clear()
print(set1)

# si desea eliminar el set use del
#del set
#print(set)