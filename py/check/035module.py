# un modulo se puede considerar como una libreria, puede contener todas las funciones necesarias para el funcionamiento
# de una app.

import py.check.mdl as mdl

mdl.prbmdl('Alex')

# los modulos puden almacenar diferentes tipos de datos para ser usados en cualquier momento
a = mdl.p1['edad']
print(a, type(a))

# existen varios modulos precargados en python
import platform as pt

x = pt.system()
print(x)

# la funcion dir() lista todas las funciones en un modulo. 
x = dir(pt)
print(x)

# si desea usar una parte especifica del modulo use:
# from mdl import p1