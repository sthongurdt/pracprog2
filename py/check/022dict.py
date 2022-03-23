# los diccionarios se usan para lamacenar datos usando pares llave:valor.
dict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
print(dict)

# los elementos estan ordenados, se pueden cambiar, no permite duplicados y pueden referenciarse usando la llave.
print(dict["marca"]) 
dict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964,
  "año": 2020
}
print(dict)

# imprimir el numero de elementos en el diccionario
print(len(dict))

# se pueden almacenar diferente tipos de datos
dict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964,
  "colores": ["rojo", "blanco", "azul"]
}
print(dict, type(dict))