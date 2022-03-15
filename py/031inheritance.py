# la herencia permite definir una clase que hereda todos los metodos y propiedades de otra clase
# la clase padre es la clase que se hereda (también se llama clase base)
# la clase hijo es la clase que se hereda de otra clase (también llamada clase derivada) 

# creando clase padre
class persona:
    def __init__(yo, nombre, apellido):
        yo.nombre = nombre
        yo.apellido = apellido
    
    def nomComp(yo):
        print(yo.nombre, yo.apellido)

per = persona('Juanito', 'Alimaña')
per. nomComp()

# creando clase hijo - se usa la clase pacre como argumento de la clase hijo
class estudiantes(persona):
    pass

est = persona('Andres','Lopez')
est.nomComp()

# si desea modificar la funcion __init__ de la clase hijo y adicionar propiedades
class estudiantes(persona):
    def __init__(ref, nombre, apellido):
        persona.__init__(ref, nombre, apellido)

est = persona('Andres','Lopez')
est.nomComp()

# puede usar la funcion super() para hacer que la clase hijo herede los metodos y propiedades de la clase padre
class estudiantes(persona):
    def __init__(ref, nombre, apellido):
        super().__init__(nombre, apellido)

est = persona('Andres','Lopez')
est.nomComp()

# agregar propiedades y metodo
class estudiantes(persona):
    def __init__(ref, nombre, apellido, gradoC):
        super().__init__(ref, nombre, apellido)
        ref.gradoCol = gradoC

    def saludo(ref):
        print('hola soy ', ref.nombre, ref.apellido, 'me gradue en el año ', ref.gradoCol)

est = persona('Andres','Lopez',2006)
est.saludo()
