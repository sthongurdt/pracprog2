# Un bucle puede realizarse en una lista usando for
lst = ['mora', 'pera', 'mango', 'piña', 'kiwi', 'coco', 'higo', 'lima', 'uva', 'datil', 'fresa', 'sandia']
for x in lst:
    print(x)

# si desea recorrer una lista con for por medio de sus indices use len() y range()
for i in range(len(lst)):
    print(lst[i])

# los bucles pueden esperar a que suceda algo, los bucles while() nos dan esta posibilidad
c = 0
while c < len(lst):
    print(lst[c])
    c = c + 1

# los bucles pueden usar la comprension en las listas 
[print(x) for x in lst]

# la comprension ofrece una sintaxis ordenada simple de cierta operaciones para diferentes fines, newlist = [expression for item in iterable if condition == True]
lst1 = []
for x in lst:
    if 'a' in x:
        lst1.append(x)
print(lst1)

lst1 = [x for x in lst if 'a' in x]
print(lst1)

lst2 = [x for x in range(10)]
print(lst2)

lst3 = [x for x in range(10) if x > 5]
print(lst3)

lst4 = [x.upper() for x in lst]
print(lst4)

lst1 = ['hola' for x in lst]
print(lst1)
