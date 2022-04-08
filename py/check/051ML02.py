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

# Regresion Poligonal
# si los puntos no se adaptan a una regresion lineal, es probable que lo haga la regresion polinomial
# se usa la relacion entre x e y, para encontrar la mejor forma de dibujar una linea a través de los puntos
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy tiene un metodo que genera la linea
modelo = np.poly1d(np.polyfit(x, y, 3)) 

# especifique como se dibuja la linea, inicia el 1 y termina en 22
ejexlinea = np.linspace(1, 22, 100) 

plt.scatter(x, y)
plt.plot(ejexlinea, modelo(ejexlinea)) 
plt.show() 

# R-cuadrado
# Se debe conocer la relacion entre los valores de x e y, sino existe no se puede realizar la regrecion
# la relacion se mide con R-cuadrado, el valor va de 0 a 1, 0 significa que no existe relacion y 1 es el 100% de relacion.
# esto se calcula importando r2_score() desde sklearn.metrics
# sklearn.metrics se habilita instalando scikit-learn: pip install scikit-learn
from sklearn.metrics import r2_score

print(r2_score(y, modelo(x)))

# si desea predecir algun valor, solo agregelo al modelo
print(modelo(15))

# si se elige mal la regresion polinomial puede pasar cosas como esta
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

modelo = np.poly1d(np.polyfit(x, y, 3))

ejexlinea = np.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(ejexlinea, modelo(ejexlinea))
plt.show()
print(r2_score(y, modelo(x)))