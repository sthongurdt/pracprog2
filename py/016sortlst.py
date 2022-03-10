# las listas pueden ordenar sus elemento alfabeticamente, ascendente y por defecto. Use sort()
lst = ['mora', 'pera', 'mango', 'piña', 'kiwi', 'coco', 'higo', 'lima', 'uva', 'datil', 'fresa', 'sandia']
lst.sort()
print(lst)
lst1 = [100, 50, 65, 82, 91, 32]
lst1.sort()
print(lst1)

# si se desea invertir el ordenamiento
lst1.sort(reverse = True)
print(lst1)
lst.sort(reverse = True)
print(lst)

# se puede utilizar una funcion para el ordenamiento
def prb(n):
    return abs(n - 50)

lst1.sort(key = prb)
print(lst1)

# el orden se realiza teniendo en cuenta las mayusculas
lst2 = ["banano", "Naranja", "Kiwi", "cereza"]
lst2.sort()
print(lst2)

lst2.sort(key = str.lower)
print(lst2)

# se puede realizar una inversion de la lista
lst2 = ["banano", "Naranja", "Kiwi", "cereza"]
lst2.reverse()
print(lst2)