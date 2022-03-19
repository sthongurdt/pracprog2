# Una función lambda es una pequeña función anónima. Una función lambda puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión.
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6)) 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

# El poder de lambda se muestra mejor cuando los usa como una función anónima dentro de otra función.
def prb(n):
  return lambda a : a * n 
prbx3 = prb(3)
print(prbx3(5))

prbx5 = prb(5)
print(prbx5(5))