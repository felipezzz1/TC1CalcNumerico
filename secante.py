import numpy as np

def f(x):
  return x**3-9*x+3

def secante(x0, x1, Erro, itMax):
  it = 0
  Er = 1
  xa1 = x0
  x = x1
  while(Er >= Erro and it < itMax):
    xa2 = xa1
    xa1 = x
    x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
    Er = np.abs((x - xa1)/x)
    it = it + 1
  return (x, Er, it)

x0 = 1
x1 = 2
float(x0)
float(x1)
Erro = 5*10**-4
itMax = 10

res = secante(x0, x1, Erro, itMax)

print('O valor da raíz é:', (res[0]))
print('O erro relativo foi:', (res[1]))
print('O número de iterações realizadas foi: ', (res[2]))