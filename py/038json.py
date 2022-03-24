# json es una sintaxis para el almacen e intercambio de datos
# python tiene incorporado un paquete para manejar json
import json

# si se tiene un json se puede analizar en python con json.loads() para convertirlo a un diccionario

jc = '{ "nombre":"John", "edad":30, "ciudad":"New York"}'

t = json.loads(jc)

print(t, type(t))

# si quiere convertir a un json use json.dumps()
ojc = json.dumps(t)

print(ojc, type(ojc))

# los siguientes objetos se pueden convertir a cadenas json:
# dict, list, tuple, string, int, float, True, False, None
print(json.dumps({"nombre": "John", "apellido": 'Perez'}))
print(json.dumps(["manzana", "banano"]))
print(json.dumps(("manzana", "banano")))
print(json.dumps("hola"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

x = {
  "nombre": "John",
  "edad": 30,
  "casado": True,
  "divorciado": False,
  "hijos": ("Ann","Billy"),
  "mascotas": None,
  "carros": [
    {"modelo": "BMW 230", "mpg": 27.5},
    {"modelo": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# los resultados del pueden tener formato usando indent, separators y sort_keys
print(json.dumps(x, indent = 4))
print(json.dumps(x, indent = 4, separators=(". ", " = ")))
print(json.dumps(x, indent = 4, separators=(". ", " = "), sort_keys=True))