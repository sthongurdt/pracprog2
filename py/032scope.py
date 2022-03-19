# las variables locales se crean dentro de la funciones y solo pueden se usadas en ellas.
def prbl():
    x = 200
    print(x)

prbl()

# las funciones anidadas son funciones dentro de otras funciones, las variables locales de una funcion pueden usarse en funciones
# anidadas
def prbl():
    x = 200
    def imp():
        print(x)
    imp()
    
prbl()

# las variables globales son aquellas que se declaran en el cuerpo del programa fuera de las funciones y pueden ser usadas en las funciones.
y = 300
def prbg():
    print(y)

prbg()

# si se dan los mismos nombres a una variable global y local, python las trata como variables diferentes
def prbg():
    y = 200
    print(y)

prbg()
print(y)

# puede declararse una variable global con la palabra "global"
z = 500
def prbg2():
    global z
    z = 400
    print(z)

print(z)
prbg2()
