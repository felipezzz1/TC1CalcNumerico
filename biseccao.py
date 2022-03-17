import numpy as np

def f(x):
  return x**2-5

def bisseccao(a, b, Erro, itMax):
  it = 0
  x = a
  Er = 1
  while(Er >= Erro and  it < itMax):
    xold = x
    x = (a+b)/2
    Er = np.abs((x - xold)/x)
    if (f(a)*f(x) < 0):
      b = x
    else:
      a = x
    it = it + 1
  return (x, Er, it)

a = 2
b = 3
Erro = 10**-2
itMax = 10

res = bisseccao(a, b, Erro, itMax)

print('O valor da raíz é: ', (res[0]))
print('O número de iterações realizadas foi: ', res[2])