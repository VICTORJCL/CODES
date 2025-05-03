
# nome = input("qual seu nome completo?")
# cumprimento = nome.split()
# print('olá', cumprimento[0], " seja muito bem vindo!")

# email = input("qual o seu email?")
# domi = email.split("@")
# print("o domínio informado foi {}".format(domi[-1]))

### Exercício 4 
# Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar, e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor. Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.
#  1l > 3m2    1l = 18l   1l = 80
# Você deseja arredondar um número de ponto flutuante (float) para cima, ou seja, para o próximo inteiro, sempre que a parte decimal desse número for maior que zero.
# Solução Usando a Função math.ceil():
# A função mais adequada para essa tarefa em Python é o math.ceil(). Ela retorna o menor inteiro maior ou igual ao número fornecido.
import math
m2 = float(input("quantos metros quadrados deseja pintar?")) 
latas = (m2/3)/18
latas = math.ceil(latas)
preco = latas * 80
print( "você deve comprar {}" .format(latas),"lata /n", "o preço vai custar {}".format(preco),"reais")