import numpy as np

def f(x):
  return x**3-9*x+3

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

a = 0
b = 1
Erro = 0.0005
itMax = 100

res = falsaPosicao(a, b, Erro, itMax)

print('O valor da raíz é: %.2f'% (res[0]))
print('O erro relativo foi: %.2f'% (res[1]))
print('O número de iterações realizadas foi: ', res[2])