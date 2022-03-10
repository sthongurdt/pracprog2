# se puede acceder a los elementos de un set con un for
set = {'mora', 'limon', 'piña', 'kiwi'}
for x in set:
    print(x)

# si desea verivicar un elemento en el set
print('mora' in set)

# ademas de update() puede usar union() para juntar set
set1 = {"a", "b" , "c", "kiwi"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set.union(set3)
print(set4)

# si desea seleccionar los elementos que se encuentran en ambos sets use intersection_update()
x = {'mora', 'limon', 'piña'}
y = {'limon', 'piña', 'kiwi'}
x.intersection_update(y)
print(x)

# si desea crear un nuevo set con los elementos en ambos set use intersection()
x = {'mora', 'limon', 'piña'}
y = {'limon', 'piña', 'kiwi'}
z = x.intersection(y)
print(z)

# si desea ver los elementos que no se encuentran en ambos sets use symmetric_difference_update()
x = {'mora', 'limon', 'piña'}
y = {'limon', 'piña', 'kiwi'}
x.symmetric_difference_update(y)
print(x)

# si desea crear un nuevo set con los elementos que no estan en ambos set use symmetric_difference() 
x = {'mora', 'limon', 'piña'}
y = {'limon', 'piña', 'kiwi'}
z = x.symmetric_difference(y)
print(z)

# Estos son lo metodos que se pueden usar con los sets
# add()                 Agrega un elemento al conjunto
# clear()               Elimina todos los elementos del conjunto
# copy()                Devuelve una copia del conjunto
# difference()          Devuelve un conjunto que contiene la diferencia entre dos o más conjuntos
# difference_update()   Elimina los elementos de este conjunto que también están incluidos en otro conjunto especificado
# discard()             Eliminar el elemento especificado
# intersection()            Devuelve un conjunto, que es la intersección de otros dos conjuntos
# intersection_update()     Elimina los elementos de este conjunto que no están presentes en otro(s) conjunto(s) especificado(s)
# isdisjoint()              Devuelve si dos conjuntos tienen una intersección o no
# issubset()                Devuelve si otro conjunto contiene este conjunto o no
# issuperset()              Devuelve si este conjunto contiene otro conjunto o no
# pop()                         Elimina un elemento del conjunto
# remove()                      Elimina el elemento especificado
# symmetric_difference()        Devuelve un conjunto con las diferencias simétricas de dos conjuntos
# metric_difference_update()    Inserta las diferencias simétricas de este conjunto y otro
# union()                       Devuelve un conjunto que contiene la unión de conjuntos
# update()                      Actualizar el conjunto con la unión de este conjunto y otros 