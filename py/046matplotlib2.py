# la lineas en matplotlib tinen estilo y pueden definirse con ls o linestyle
import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 2, 10])

plt.plot(y, linestyle = 'dotted')
plt.show()

plt.plot(y, linestyle = 'dashed')
plt.show()

# la sintaxis acortada es:
#   ls  linestyle
#   :   punteda
#   --  raya
#   -   linea solida
#   -.  raya punto
#   or  Nada

# el color se puede definir con color o 'c':
plt.plot(y, color = 'r')
plt.show()

# tambien se puede agregar colores hex
plt.plot(y, c = '#4CAF50')
plt.show()

# o por un nombre definido
plt.plot(y, c = 'hotpink')
plt.show()

# el grosor de la lineas se puede definir por linewidth o lw
plt.plot(y, linewidth = '20.5')
plt.show()

# Se pueden mostrar varias lineas en un mismo grafico
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 4, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 4])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# se puede agragar etiquetas a los plots, con xlabel para el eje x, con ylabel para el eje y
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Pulso Promedio")
plt.ylabel("Calorias Quemadas")

plt.show()

# si desea agregar un titulo use title()
plt.plot(x, y)

plt.title("Datos Smartwatch")
plt.xlabel("Pulso Promedio")
plt.ylabel("Calorias Quemadas")

plt.show()

# se puede usar fontdict para pasar los parametros xlabel(), ylabel() y title()
d1 = {'family':'serif','color':'b','size':20}
d2 = {'family':'serif','color':'r','size':10}

plt.title("Datos Smartwatch", fontdict = d1)
plt.xlabel("Pulso Promedio", fontdict = d2)
plt.ylabel("Calorias Quemadas", fontdict = d2)

plt.plot(x, y)
plt.show()

# el titulo puede colocarse en lugares (por defecto esta en el centro) como:
#   left    izquierda
#   right   derecha
#   center  centro
plt.title("Datos Smartwatch", fontdict = d2, loc = 'left')
plt.xlabel("Pulso Promedio", fontdict = d2)
plt.ylabel("Calorias Quemadas", fontdict = d2)

plt.plot(x, y)
plt.show()

# con la funcion grid() puede agregarse una maya a el grafico
plt.title("Datos Smartwatch", fontdict = d1)
plt.xlabel("Pulso Promedio", fontdict = d2)
plt.ylabel("Calorias Quemadas", fontdict = d2)

plt.plot(x, y)
plt.grid()
plt.show()

# la maya puede colocarse en diferentes ejes
plt.title("Datos Smartwatch", fontdict = d1)
plt.xlabel("Pulso Promedio", fontdict = d2)
plt.ylabel("Calorias Quemadas", fontdict = d2)

plt.plot(x, y)
plt.grid(axis = 'x')
plt.show()

plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

# la maya puede tener color (color), estilo (linestyle) y grosor (linewidth)
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()