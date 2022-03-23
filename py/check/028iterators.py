# los iteradores son un objeto que contiene un numero de valores contables
# listas, tuplas, conjuntos y diccionarios son todos iterables, todos tienen un metodo iter() que es usado para devolver una iteracion.
tpl = ("mora", "pera", "lulo")
itr = iter(tpl)
print(next(itr))
print(next(itr))
print(next(itr))

stg = 'mora'
itr2 = iter(stg)
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))

# si desea crear su propio iterado puede hacerlo de la siguiente manera
class MiIter:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

miprb = MiIter()
miter = iter(miprb)

print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter)) 

# si deseamos acotar el iterador para que no se ejecute indefinidamente puede agregar una parada
class MiIter:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else: 
        raise StopIteration


miprb = MiIter()
miter = iter(miprb)

for x in miter:
    print(x)