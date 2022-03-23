import numpy as np


def f(x):
    return x**3 - 9*x + 3

def df(x):
    return 2*x**3-3/3*x**2-9


def newton(x0, precisao, itMax):
    it = 0
    Er = 1
    x = x0
    while(Er >= precisao and it < itMax):
        xold = x
        x = x - f(x)/df(x)
        Er = np.abs((x - xold)/x)
        it = it + 1
    return (x, it)


x0 = float(input("Digite a aproximação inicial de x0: "))
precisao= float(input("Digite a precisao: "))
itMax = int(input("Digite a quantidade de iterações: "))

res = newton(x0, precisao, itMax)

print('O valor da raíz é: ', (res[0]))
print('O número de iterações realizadas foi: ', res[1])
