import numpy as np

def f(x):
  return 31 - ((9.8*x)/13)*(1. - np.exp(-6.0*(13.0/x)))

def falsaPosicao(a, b, Erro, itMax):
  it = 0
  x = a
  Er = 1
  while(Er >= Erro and  it < itMax):
    xold = x
    x = a - f(a)*(b-a)/(f(b)-f(a))
    Er = np.abs((x - xold)/x)
    if (f(a)*f(x) < 0):
      b = x
    else:
      a = x
    it = it + 1
  return (x, Er, it)

a = 40
b = 60

a = 52
b = 55
Erro = 10**-4
itMax = 6

res = falsaPosicao(a, b, Erro, itMax)

print('O valor da raíz é: %.2f'% (res[0]))
print('O erro relativo foi: %.2f'% (res[1]))
print('O número de iterações realizadas foi: ', res[2])