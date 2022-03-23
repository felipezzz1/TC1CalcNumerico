import numpy as np;

def f(x):
    return x**3-9*x+3

def df(x):
    return x**3/9 + 1/3

def mil(x0, precisao, itMax):
        it = 0
        x1 = 0
        while (np.abs(f(x1)) >= precisao and it < itMax):
                x1 = df(x0)
                x0 = x1
                it += 1
        return(x0, it)

x0 = float(input("Digite a aproximação inicial x0: "))
precisao= float(input("Digite a precisao: "))
itMax = int(input("Digite a quantidade de iterações: "))

res = mil(x0, precisao, itMax)

print('O valor da raíz é: ', (res[0]))
print('O número de iterações realizadas foi: ', res[1])

