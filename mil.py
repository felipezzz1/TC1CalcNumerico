import numpy as np


def f(x): #define a funçao f(x) que sera utilizada
    return x**3-9*x+3


def df(x): #define a funçao ϕ(x) que sera utilizada
    return x**3/9 + 1/3


def mil(x0, precisao, itMax): #funçao MIL ou ponto fixo
    it = 0 #inicia a variavel it que serve para guardar o nº de iteraçoes
    x1 = 0 #inicia a variavel x1 que serve para guardar o valor de ϕ(x0) no inicio do while
    while (np.abs(f(x1)) >= precisao and it < itMax): 
        #enquanto f(x1) em modulo for maior ou igual a precisao ou it ultrapassar o valor maximo de iteraçoes
        x1 = df(x0)
        x0 = x1
        it += 1
    return(x0, it) #retorna o valor de x0 que sera o valor da raiz e it o valor de iteraçoes realizadas


x0 = float(input("Digite a aproximação inicial x0: ")) # input float para x0
precisao = float(input("Digite a precisao: ")) # input float para o valor da precisao
itMax = int(input("Digite a quantidade de iterações: ")) # input int para a quantidade maxima de iteraçoes

res = mil(x0, precisao, itMax) #inicia a variavel res que recebera a funçao mil com os valores acima inseridos

print('O valor da raíz é: ', (res[0])) # imprime o valor da raiz
print('O número de iterações realizadas foi: ', res[1]) # imprime o nº de iteraçoes realizadas
