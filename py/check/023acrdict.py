# si desea acceder a los elemnto de un diccionario use las llaves
dict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964,
  "colores": ["rojo", "blanco", "azul"]
}
print(dict["colores"])

# se puede acceder por get()
print(dict.get("colores"))

# si desea conocer la llaves del diccionario use keys()
print(dict.keys())

# si desea conocer los valores del diccionario use values()
print(dict.values())

# items() genera una lista de tuplas, las tuplas contienen la (llave,valor)
print(dict.items())

# si desea verificar si un datos se encuentra en el diccionario use la llave
if 'año' in dict:
    print('año se encuentra en el diccionario')

# si desea agregar un dato al diccionario
dict["cc"] = 3000
print(dict)

# si desea cambiar un dato del diccionario use la llave
dict['año'] = 2020
print(dict)

# un dato se puede actualizar utilizando update()
x = list(dict.get('colores'))
x.append('negro')
dict.update({'colores':x})
print(dict)
dict1 = dict

# si desea eliminar un dato del diccionario debe especificar la llave y usar pop(). Si desea eliminar el ultimo dato del diccionario use popitem()
dict.pop('cc')
print(dict)
dict.popitem()
print(dict)
del dict['año']
print(dict)

# si desea eliminar el diccionario use del
#del dict

# si desea vaciar el diccionario use clear()
print(dict1.clear())