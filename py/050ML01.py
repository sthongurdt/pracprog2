# Machine Learning (ML) que analiza datos y aprende a predecir los resultados
# ML es parte de las bases en direccion a la Inteligencia Artificial (AI)
# Lo fundamental es el estudio de la matematica y estadistica, y como calcular lo importante apartir de data sets

# Data set: data set es una coleccion de datos, puede se desde una matriz hasta una base de datos completa

# Tipos de datos: puede dividirse en tres categorias proncipales:
#   Numerical: son numeros y puede dividirse en dos categorias:
#       Discrete data: se limita a numeros enteros. Ejp: La cantidad de carros
#       Continuous data: numeros que tiene valor infinito. Ejp: El precio de un articulo, el tamaño de un item
#   Categorical: son valores que no pueden compararse entre si. Ejp: el valor de un color, Valores Si/No
#   Ordinal: Son datos categorical que se pueden comparar entre si. Ejp: Calificaciones donde A es mejor que B.

# Conocer el tipo de dato podra saber que tecnica utilizar al analizarlos

# En ML casi siempre hay tres valores que interesan:
#   Media: valor promedio
#   Mediana: valor del punto medio
#   Moda: valor mas comun
import numpy as np
from scipy import stats as sts 

v1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]
v2 = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

# La media es la suma de todos los valores dividido por su cantidad, use la funcion mean() de NumPy 
print(np.mean(v1))
print(np.mean(v2))

# la mediana es el valor en el medio despues de ordenar los valores, use la funcion median(), Si hay dos números en el medio, 
# divide la suma de esos números por dos.
print(np.median(v1))
print(np.median(v2))

# la moda es el valor que aparece mas numero de veces, use mode() de SciPy
print(sts.mode(v1))
print(sts.mode(v2))

# La Desvicacion Estandar (DE) describe que tan dispersos estan los valores, una DE baja significa que los valores estan cerca del valor promedio
# Un DE alta significa que los valores estan distribuidos en un rango mas amplio
v3 = [86,87,88,86,87,85,86]
v4 = [32,111,138,28,59,77,97]
DE1 = np.std(v3)
DE2 = np.std(v4)

print(np.std(v3))
print(np.std(v4))

# La Varianza es otro numero que indica que tan disperso estan los valores. La raiz cuadrad de la varianza es la DE o DE x DE = Varianza
# La varianza se calcula de la siguiente manera:
#   Encuentra la media
#   para cada valor encuentre la diferencia con la media
#   para cada diferencia encuentre su doble (cuadrado o ^2)
#   la varianza es el promedio de las diferencias al cuadrado
# En Python use var()
print(np.var(v3))
print(pow(DE1, 2))
print(np.var(v4))
print(pow(DE2, 2))

# los percentiles son un numero que describe el valor en porcentaje por debajo de un valor, se usa el metodo percentile()
e = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(np.percentile(e, 80))
# cual es el precentil 80 o significa que el 80% de los valores es 48 o menos
# cual seria el percentil 40
print(np.percentile(e, 40))
