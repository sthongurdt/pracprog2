# un diccionario puede ser recorrido por un for, pero solo se mostraran sus llaves
dictp = {'marca': 'Ford', 'modelo': 'Mustang', 'año': 2020, 'colores': ['rojo', 'blanco', 'azul', 'negro'], 'cc': 3000}
for x in dictp:
    print(x)
    print(dictp[x])

# se puede usar el metodo values() para mostrar el contenido de la llaves
for x in dictp.values():
    print('values():', x)

for x in dictp.keys():
    print('keys():', x)

for x in dictp.items():
    print('items():', x)

# si desea copiar un diccionario use copy() o el constructor dict()
dict1 = dictp.copy()
dict2 = dict(dictp)
print(dict1)
print(dict2)

# los diccionarios pueden tener diccionarios anidados
dictp = {
   "niño1" : {
    "nombre" : "Emil",
    "año" : 2004
  },
  "niño2" : {
    "nombre" : "Tobias",
    "año" : 2007
  },
  "niño3" : {
    "nombre" : "Linus",
    "año" : 2011
  }
}

# los metodos de los diccionarios son:
# clear()       Elimina todos los elementos del diccionario
# copy()        Devuelve una copia del diccionario
# fromkeys()    Devuelve un diccionario con las claves y el valor especificados
# get()         Devuelve el valor de la clave especificada
# items()       Devuelve una lista que contiene una tupla para cada par de valores clave
# keys()        Devuelve una lista que contiene las claves del diccionario
# pop()         Elimina el elemento con la clave especificada
# popitem()     Elimina el último par clave-valor insertado
# setdefault()  Devuelve el valor de la clave especificada. Si la clave no existe: inserte la clave, con el valor especificado
# update()      Actualiza el diccionario con los pares clave-valor especificados
# values()      Devuelve una lista de todos los valores en el diccionario 