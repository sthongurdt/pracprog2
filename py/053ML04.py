# Funcion Scale
# los datos pueden ser dificiles de comparar, por ello, podemos escalar los datos en nuevos valores
# que son mas faciles de comparar. Se usa cars2.csv

# En Scale se usa el metodo de estandarizacion, el metodos usa la formula: z = (x - u) / s
# Donde z es el nuevo valor, x es el valor original, u es la media y s es la desviación estándar.
# el módulo sklearn de Python tiene un método llamado StandardScaler() que devuelve un objeto Scaler con métodos para transformar conjuntos de datos.
# se realiza scale a un csv con datos similares al data set usado en 052ML03.py
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scalado = scale.fit_transform(X)

print(scalado)  

# Cuando se escala el conjunto de datos, tendrá que usar la escala cuando prediga valores:
y = df['CO2']

regre = linear_model.LinearRegression()
regre.fit(scalado, y)

scala = scale.transform([[2300, 1.3]])

prediCO2 = regre.predict([scala[0]])
print(prediCO2)

# Evaluacion de Modelos
# en ML se crean modelos para predecir resultados, para probar un modelo podemos usar train/test.
# train/test mide la precision de un modelo, se dividen los datos en 80% para train y 20% para test.
# train significa crear el modelo, test significa probar la precision del modelo.
# Comience con un conjunto de datos que desee probar.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show() 

# divide los datos en train (80) y test (20)
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show() 

plt.scatter(test_x, test_y)
plt.show() 

# para este caso se usa una regrecion polinimial
modelo = np.poly1d(np.polyfit(train_x, train_y, 4))

ejexlinea = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(ejexlinea, modelo(ejexlinea))
plt.show() 

# usamos R-cuadrado para corroborar si la regrecion es la correcta
from sklearn.metrics import r2_score
r2 = r2_score(train_y, modelo(train_x))
print(r2) 

# el resultado es aceptable, ahora se pasan los datos de test al modelo probado
r2 = r2_score(test_y, modelo(test_x))
print(r2)
# se puede ver que la presicion del modelo con los datos de test aumenta

# Los arboles de decision son un diagrama de flujo que ayuda a tomar decisiones basado en experiencias previas.
# instale pydotplus: pip install pydotplus
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

# para generar un arbol de decision, todos los datos deben de ser numericos. Se deben de convertir la columnas no numericas, 
# el metodo map() toma un diccionario para convertir los datos
d1 = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d1)
d2 = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d2)

# los datos se separan entre caracteristicas y destino. Las caracteristicas (feature) son las columnas a partir de las que vamos a decidir, 
# el destino (target) es la columna con los valores que vamos a predecir.
features = ['Age', 'Experience', 'Rank', 'Nationality']

x = df[features]
y = df['Go']

# ahora se puede crear el arbol, agregarle los datos y guardar un .png.
import pydotplus
dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('tree.png')

img=pltimg.imread('tree.png')
imgplot = plt.imshow(img)
plt.show()  