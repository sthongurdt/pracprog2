# las funciones en python se declaran usando la palabra "def"
def funcion():
    print("hola mundo")

funcion()

# los argumentos son informacion que se le puede pasar a una funcion
def nomcom(nombre):
    print(nombre + ' Perez')

nomcom('Mateo')
nomcom('Marcos')

# los parametros y argumentos son lo mismo, informacion que se pasa a una funcion. Una funcion debe llamarse con el numero correcto de argumentos.
def nom(nombre, apellido):
    print(nombre + ' ' + apellido)

nom('Mateo', 'Perez')

# Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función
def nomb(*nombre):
    print('Su nombre es ' + nombre[1])

nomb('Mateo', 'Marcos', 'Lucas')

# se pueden usar la palabra clave para pasar los argumentos sin que importe el orden
def nomk(n1, n2, n3):
    print('Su nombre es ' + n3)

nomk(n1 = 'Mateo', n2 = 'Marcos', n3 = 'Lucas')

# Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos (**) antes del nombre del parámetro 
# en la definición de la función
def nomcom(**n):
    print('Su nombre es ' + n['apellido'])

nomcom(nombre = 'Mateo', apellido = 'Perez')

# se puede definir un argumento por defecto 
def pais(p = "Colombia"):
    print("Soy de " + p)

pais("India")
pais()
pais("Brasil")

# se puede pasar una lista como argumento
def imp_lst(x):
    for i in x:
        print(i)

lst = range(3)

imp_lst(lst)

# Para permitir que una función devuelva un valor, use la declaración return
def prb(x):
    return x * 3

for i in lst:
    print(prb(i))

# tambien se puede usar "pass" como contenido a una funcion

# Python también acepta la función recursiva, lo que significa que una función definida puede llamarse a sí misma.
def recursiva(k):
  if(k > 0):
    res = k + recursiva(k - 1)
    print(res)
  else:
    res = 0
  return res

print("Ejp. recursividad")
recursiva(6)