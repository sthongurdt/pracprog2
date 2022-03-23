# python es un lenguaje orientado a objetos

# para crear una clase use la palabra class
class miClase:
    y = 9

# cree un objeto
obj = miClase()
print(obj.y)

# los objetos tienen una funcion __init__() que se ejecuta cuando se inicia la clase, esta funcion asigna los valores a las propiedades del objeto u otras 
# operaciones que sean necesarias cuando se crea el objeto
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

per = persona('Juan', 30)
print(per.nombre)
print(per.edad)

# si desea agregar un metodo a el objeto

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def pres(self):
        print("Hola soy, " + self.nombre)

per = persona('Juan', 30)
per.pres()

# el parametro self es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase.
# No tiene que llamarse self , puedes llamarlo como quiera, pero tiene que ser el primer parámetro de cualquier función en la clase.
class persona:
    def __init__(ref, nombre, edad):
        ref.nombre = nombre
        ref.edad = edad

    def hola(yo):
        print('Hola soy, ' + yo.nombre)

per = persona('Juan', 30)
per.hola()

# si desea modificar la propiedad del objeto
per.edad = 32
print(per.edad)

# si desea eliminar una propiedad 
#del per.edad

# si desea elimnar el objeto
#del per

# los objetos no puede estar vacios, pero si llega a tener una objeto sin contenido use pass.
class prb:
    pass