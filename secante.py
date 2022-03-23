import numpy as np


def f(x): #define a funçao f(x) que sera utilizada
    return x**3-9*x+3


def secante(x0, x1, precisao, itMax): #funçao do metodo da secante
    it = 0 #inicia a variavel it que serve para guardar o nº de iteraçoes
    Er = 1 #inicia a variavel Er que serve para guardar o valor calculado do erro
    xa1 = x0 #inicia o valor xa1 que recebera o valor de x0
    x = x1 #inicia o valor x que recebera o valor de x1
    while(Er >= precisao and it < itMax):
        #enquanto Er for maior ou igual a precisao ou it ultrapassar o valor maximo de iteraçoes
        xa2 = xa1
        xa1 = x
        x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
        Er = np.abs((x - xa1)/x)
        it = it + 1
    return (x, it) #retorna o valor de x que sera o valor da raiz e it o valor de iteraçoes realizadas


x0 = float(input("Digite a aproximação inicial de x0: ")) #input float para o valor de x0
x1 = float(input("Digite a aproximação inicial de x1: ")) #input float para o valor de x1
precisao = float(input("Digite a precisao : ")) #input float para o valor da precisao
itMax = int(input("Digite a quantidade de iterações: ")) #input int para o valor maximo de iteraçoes

res = secante(x0, x1, precisao, itMax) #inicia a variavel res que recebera a funçao regulaFalsi com os valores acima inseridos

print('O valor da raíz é: ', (res[0])) # imprime o valor da raiz
print('O número de iterações realizadas foi: ', res[1]) # imprime o nº de iteraçoes realizadas
