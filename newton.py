import numpy as np

def f(x):
  return 31 - ((9.8*x)/13)*(1. - np.exp(-6.0*(13.0/x)))

def df(x):
  return np.exp(-78.0/x)*(9.8/13.0 + 58.8/x) - 9.8/13.0

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

x0 = 54
Erro = 10**-4
itMax = 6

res = newton(x0, Erro, itMax)

print('O valor da raíz é: %.2f'% (res[0]))
print('O erro relativo foi: %.2f'% (res[1]))
print('O número de iterações realizadas foi: ', res[2])