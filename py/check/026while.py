# un bucle while se mantiene mientras una declaracion sea verdadesra
i = 1
while i < 6:
  print(i)
  i += 1

# break permite detener el bucle si un evento sucede
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

# continue detiene la actual iteracion y continua con la siguiente declaracion
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else ejecuta un bloque de codigo una vez se ha cumplido la declaracion
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i ya no es menor que 6")