import numpy as np


def f(x): #define a funçao f(x) que sera utilizada
    return x**3-9*x+3


def regulaFalsi(a, b, precisao, itMax): #metodo da falsa posiçao ou regula falsi
    it = 0 #inicia a variavel it que serve para guardar o nº de iteraçoes
    x = a #inicia a variavel x que recebe o valor de a
    Er = 1 #inicia a variavel Er que serve para guardar o valor calculado do erro
    while(Er >= precisao and it < itMax):
        #enquanto Er for maior ou igual a precisao ou it ultrapassar o valor maximo de iteraçoes
        xold = x
        x = a - f(a)*(b-a)/(f(b)-f(a))
        Er = np.abs((x - xold)/x)
        if (f(a)*f(x) < 0):
            b = x
        else:
            a = x
        it = it + 1
    return (x, it)  #retorna o valor de x que sera o valor da raiz e it o valor de iteraçoes realizadas


a = float(input("Digite a aproximação inicial de a: ")) # input float para a
b = float(input("Digite a aproximação inicial de b: ")) # input float para b
precisao = float(input("Digite a precisao : ")) # input float para precisao
itMax = int(input("Digite a quantidade de iterações: ")) # input int para o valor maximo de iteraçoes

res = regulaFalsi(a, b, precisao, itMax) #inicia a variavel res que recebera a funçao regulaFalsi com os valores acima inseridos

print('O valor da raíz é: ', (res[0])) # imprime o valor da raiz
print('O número de iterações realizadas foi: ', res[1]) # imprime o nº de iteraçoes realizadas
