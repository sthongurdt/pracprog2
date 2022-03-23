# se pueden realizar bucles usando for
tpl = ('mora', 'limon', 'piña', 'kiwi', 'coco', 'higo', 'lima', 'pera', 'uva')
for x in tpl:
    print(x)

# se puede recorer una tupla usando range() y len()
for i in range(len(tpl)):
    print(tpl[i])

# se puede recorrer una tupla con while
i = 0
while i < len(tpl):
    print(tpl[i])
    i = i + 1

# se pueden unir dos tuplas con concatenaciones
tpl1 = ('a', 'b', 'c')
tpl2 = (1, 2, 3)
tpl3 = tpl1 + tpl2
print(tpl3)

# El contenido se puede multiplicar
tpl4 = tpl1 * 2
tpl5 = tpl2 * 2
print(tpl4)
print(tpl5)

# las tuplas tienen los siguientes dos metodos
# count() Devuelve el número de veces que aparece un valor especificado en una tupla
# index() Busca en la tupla un valor específico y devuelve la posición donde se encontró