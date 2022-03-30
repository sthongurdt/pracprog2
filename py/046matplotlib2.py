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