import numpy as np


def f(x):
    return x**3-9*x+3


def falsaPosicao(a, b, precisao, itMax):
    it = 0
    x = a
    Er = 1
    while(Er >= precisao and it < itMax):
        xold = x
        x = a - f(a)*(b-a)/(f(b)-f(a))
        Er = np.abs((x - xold)/x)
        if (f(a)*f(x) < 0):
            b = x
        else:
            a = x
        it = it + 1
    return (x, it)


a = float(input("Digite a aproximação inicial de a: "))
b = float(input("Digite a aproximação inicial de b: "))
precisao= float(input("Digite a precisao : "))
itMax = int(input("Digite a quantidade de iterações: "))

res = falsaPosicao(a, b, precisao, itMax)

print('O valor da raíz é: ', (res[0]))
print('O número de iterações realizadas foi: ', res[1])
