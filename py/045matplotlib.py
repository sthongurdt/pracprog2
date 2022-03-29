# Matplotlib es una libreria para visualizacion sencilla.
#   Para instalar matplotlib use el comando:
#       pip install matplotlib
# Para importar la libreria use:
import matplotlib as plotlib

# si desea verificar la version de matplotlib
print(plotlib.__version__)

# muchas de las utilidades de matplotlib se encuentran en el submodulo 
import matplotlib.pyplot as plt
import numpy as np

ejeX = np.array([0,6])
ejeY = np.array([0,250])

# la funcion plot tiene 2 parametros basicos, eje x y eje y, 
plt.plot(ejeX, ejeY)
plt.show()

ejeX1 = np.array([2,5])
ejeY1 = np.array([1,10])
# si deseamos que se vean solo los puntos
plt.plot(ejeX1, ejeY1, 'o')
plt.show()

ejeX2 = np.array([2, 5, 3, 6])
ejeY2 = np.array([1, 10, 2, 9])

# si deseas enfatizar los puntos usa marker, los marker pueden ser:
#   'o' Círculo 
#   '*' Estrella
#   '.' Punto
#   ',' píxel
#   'x' X
#   'X' X (lleno)
#   '+' más
#   'P' Más (lleno)
#   's' Cuadrado
#   'D' Diamante
#   'd' Diamante (delgado)
#   'p' Pentágono
#   'H' Hexágono 
#   'h' Hexágono 
#   'v' Triángulo Abajo
#   '^' Triángulo arriba
#   '<' Triángulo a la izquierda
#   '>' Triángulo a la derecha
#   '1' Tri abajo
#   '2' Tri arriba
#   '3' Tri izquierda
#   '4' Tri derecho 
#   '|' V-line
#   '_' H-line 
plt.plot(ejeX2, ejeY2, marker = '*')
plt.show()

# si no se especifica el eje x, plot lo genera por defecto
ejeY3 = np.array([2, 16, 8, 32])
plt.plot(ejeY3, marker = 'o')
plt.show()

# se puede usar una notacion reducida de caracteres para especificar el market, se le llama fmt (marker, linea, color)
# la linea puede tener los siguientes valores:
#   '-'     Línea sólida
#   ':'     Linea punteada
#   '--' 	Linea discontinua
#   '-.'    Línea discontinua/punteada
# para definir el color use:
#   'r'     rojo
#   'v'     verde
#   'b'     azul
#   'c'     cian
#   'm'     magenta
#   'y'     amarillo
#   'k'     negro
#   'w'     blanco 
ejeY4 = np.array([3, 8, 1, 10])
plt.plot(ejeY4, 'o:r')
plt.show()

# el tamaño del marker se puede definir usando ms
plt.plot(ejeY4, marker = 'o', ms = 20)
plt.show()

# los contornos del marker pueden tener color usando mec
plt.plot(ejeY4, marker = 'o', ms = 20, mec = 'r')
plt.show()

# los marker pueden ser rellenados de un color diferente usando mfc
plt.plot(ejeY4, marker = 'o', ms = 20, mec = 'r', mfc = 'y')
plt.show()

# los colores del marker puede se hex