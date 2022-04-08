# Regresión Múltiple
# La regresion multiple es como la regresion lineal, pero con mas de un valor. Esto quiere decir que se predice un valor en funcion de uno o mas valores.
# lo primero es importar pandas para poder trabajar el data sets
import pandas 

# pandas permite manipular archivos csv y devuelve un objeto DataFrame
df = pandas.read_csv("cars.csv") 

# en una variable se almacenan la lista de valores independientes y en otra los de la variable dependiente.
X = df[['Weight', 'Volume']]
y = df['CO2'] 

# se usaran algunos metodos de sklearn por ello se importa el modulo
from sklearn import linear_model 

# Desde el módulo sklearn se usa el método LinearRegression() para crear un objeto de regresión lineal.
# Este objeto tiene un método llamado fit() que toma los valores independientes y dependientes como parámetros y 
# llena el objeto de regresión con datos que describen la relación:
regre = linear_model.LinearRegression()
regre.fit(X, y) 

# Ahora tenemos un objeto de regresión que está listo para predecir los valores de CO2 en función del peso y el volumen
prediCO2 = regre.predict([[2300, 1300]])
print(prediCO2)

# El coeficiente es un factor que describe la relación con una variable desconocida.
# se puede pedir el valor del coeficiente de peso frente a CO2, y el de volumen frente a CO2. 
# Las respuestas que se obtienen nos dice qué pasaría si aumentamos o disminuimos uno de los valores independientes.
print(regre.coef_)

# el resultado presenta los valores de peso y volumen
# Estos valores nos dicen que si el peso aumenta en 1 kg, la emisión de CO2 aumenta en 0,00755095 g.
# Y si el tamaño del motor (Volumen) aumenta en 1 cm3, la emisión de CO2 aumenta en 0,00780526 g.
# se predijo que si un coche con un motor de 1300 cm3 pesa 2300 kg, la emisión de CO2 será de aproximadamente 107.2 g.
# Qué pasa si aumenta el peso en 1000 kg?
prediCO2 = regre.predict([[3300, 1300]])
print(prediCO2)