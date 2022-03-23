import numpy as np


def f(x): #define a funçao f(x) que sera utilizada
    return x**3 - 9*x + 3


def df(x): #define a funçao f'(x) que sera utilizada
    return 2*x**3-3/3*x**2-9


def newton(x0, precisao, itMax): #funçao do metodo de newton
    it = 0 #inicia a variavel it que serve para guardar o nº de iteraçoes
    Er = 1 #inicia a variavel Er que serve para guardar o valor calculado do erro
    x = x0 #inicia a variavel x que recebe x0
    while(Er >= precisao and it < itMax):
        #enquanto Er for maior ou igual a precisao ou it ultrapassar o valor maximo de iteraçoes
        xold = x 
        x = x - f(x)/df(x)
        Er = np.abs((x - xold)/x)
        it = it + 1
    return (x, it) #retorna o valor de x que sera o valor da raiz e it o valor de iteraçoes realizadas


x0 = float(input("Digite a aproximação inicial de x0: ")) #input float para x0
precisao = float(input("Digite a precisao: ")) #input float para precisao
itMax = int(input("Digite a quantidade de iterações: ")) #input int para itMax

res = newton(x0, precisao, itMax)  #inicia a variavel res que recebera a funçao newton com os valores acima inseridos

print('O valor da raíz é: ', (res[0])) # imprime o valor da raiz
print('O número de iterações realizadas foi: ', res[1]) # imprime o nº de iteraçoes realizadas
