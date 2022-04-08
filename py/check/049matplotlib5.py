# Matplotlib crea graficos de barras
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 5, 10])

plt.bar(x,y)
plt.show()

# si desea generar barras horizontales
plt.barh(x, y)
plt.show()

# si desea cambiar el color de las barras use el argumento color, los colores pueden definirse con una letra, nombre o hex
plt.bar(x, y, color = 'r')
plt.show()

plt.barh(x, y, color = 'yellow')
plt.show()

# el grosor de las barra puede modificarse con width
plt.bar(x, y, width = 0.1)
plt.show()

# el grosor para las barras horizontales seria su altura
plt.barh(x, y, height= 0.1)
plt.show()

# los histogramas muestran la distribucion de frecuencias, para crear un histograma se usa la funcion hist()
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

# si desea generar graficos de pie o torta use la funcion pie()
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# si desea agregar la etiquetas
etq = ['Piña', 'Mora', 'Lulo', 'Coco']

plt.pie(y, labels= etq)
plt.show()

# el grafico de pie puede ser iniciado en diferentes angulos
plt.pie(y, labels = etq, startangle = 45)
plt.show()

# el grafico pie puede se secmentado con el argumento explode()
sec = [0.3, 0.2, 0, 0.1]

plt.pie(y, labels = etq, explode = sec)
plt.show() 

# al grafico pie se le puede agregar sombra
plt.pie(y, labels = etq, explode = sec, shadow = True)
plt.show()  

# los colores pueden asignarse por letra, nombre, o hex
clrs = ["k", "hotpink", "b", "#4CAF51"]

plt.pie(y, labels = etq, colors = clrs)
plt.show() 

# si desea agregar leyendas use el argumento legend()
plt.pie(y, labels = etq)
plt.legend()
plt.show()

# si desea agregar un titulo a las leyendas
plt.pie(y, labels = etq)
plt.legend(title= 'Cantidad de Frutas')
plt.show()