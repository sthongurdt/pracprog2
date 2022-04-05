# Distribucion de Datos Normal
# se puede crear una matriz donde se concentren valores al rededor de un valor dado.
# a esta distribucion se le conoce como distribucion de datos normal o gaussiana.
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show() 

# otra manera de graficar es usar scatter
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

# la regrecion es usada para tratar de encontrar la relacion entre variables
# esta relacion es usada para predecir los resultados de futuros eventos
# la regrecion lineal utiliza la relacion de los datos para trazar una linea recta a través de todos ellos, esta linea se puede usar para determinar valores futuros
from scipy import stats as sts

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# la funcion linregress() genera la pendiente (slope), interseccion (intercept), relacion (r), (p), (std_err)
slope, intercept, r, p, std_err = sts.linregress(x, y)

def puntolinea(x):
  return slope * x + intercept

linea = list(map(puntolinea, x))

plt.scatter(x, y)
plt.plot(x, linea)
plt.show()

# r o coeficiente de relacion permite saber la relacion entre los valores del eje x y y, no no hay relacion no se puede medir nada.
# el valor de r va desde -1 a 1, si es 0 no existe ninguna relacion y 1 o -1 significa 100% de relacion
print(r)

# la funcion puntolinea() permite la generacion de futuros valores
fp = puntolinea(10)
print(fp)

# existen casos en los que la regresion lineal no es la mejor opcion
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = sts.linregress(x, y)

def puntolinea(x):
  return slope * x + intercept

linea = list(map(puntolinea, x))

print(r)
plt.scatter(x, y)
plt.plot(x, linea)
plt.show() 