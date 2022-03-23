import numpy as np


def f(x):
    return x**3-9*x+3


def secante(x0, x1, precisao, itMax):
    it = 0
    Er = 1
    xa1 = x0
    x = x1
    while(Er >= precisao and it < itMax):
        xa2 = xa1
        xa1 = x
        x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
        Er = np.abs((x - xa1)/x)
        it = it + 1
    return (x, it)


x0 = float(input("Digite a aproximação inicial de x0: "))
x1 = float(input("Digite a aproximação inicial de x1: "))
precisao= float(input("Digite a precisao : "))
itMax = int(input("Digite a quantidade de iterações: "))

res = secante(x0, x1, precisao, itMax)

print('O valor da raíz é: ', (res[0]))
print('O número de iterações realizadas foi: ', (res[1]))
