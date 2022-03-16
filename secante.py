import numpy as np

def f(x):
  return x**2 +x-6

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

x0 = 1.5
x1 = 1.7
float(x0)
float(x1)
Erro = 10**-4
itMax = 6

res = secante(x0, x1, Erro, itMax)

print('O valor da raíz é: %.2f'% (res[0]))
print('O erro relativo foi: %.2f'% (res[1]))
print('O número de iterações realizadas foi: ', (res[2]-1))