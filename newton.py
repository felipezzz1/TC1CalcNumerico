import numpy as np

def f(x):
  return x**2-5

def df(x):
  return 2*x

def newton(x0, Erro, itMax):
  it = 0
  Er = 1
  x = x0
  while(Er >= Erro and it < itMax):
    xold = x
    x = x - f(x)/df(x)
    Er = np.abs((x - xold)/x)
    it = it + 1
  return (x, Er, it)

x0 = 1
Erro = 10**-4
itMax = 6

res = newton(x0, Erro, itMax)

print('O valor da raíz é: ', res[0])
print('O número de iterações realizadas foi: ', res[2])