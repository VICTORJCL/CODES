
import os
def espadiv ():
    print('\n' + "-"*20 + '\n')
def clear():
    os.system("cls")
def port():
    print("Bem vindo ao portifólio \n    >>Escolha um carro<<")
    count=0
    for i in carros:
        print(count,i)
        count+=1
clear()
espadiv()
# navega = int(input("digite uma opção 0, 1 ou 2"))
aluguel=None
interacao = None

carros = [
["chevolet tracker", 120],
["onix", 90],
["spin",150],
["HB20",85 ],
["tucson", 120 ],
["uno",60],
["mobi",70],
["pulse",130],
]
# carros.pop('k7')   ou del carros["k{}".format(codigo_carro)]
def home():
    clear()
    print('bem vindo ao aluguél de carros')
    print('o que você deseja fazer?')

def valid_valor():
     while True:
        try:
            opcao = int(input("Digite uma opção (0, 1 ou 2): "))
            if opcao in (0, 1, 2):
                return opcao
            else:
                print("Valor inválido! Digite um valor entre 0, 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_carro():
     while True:
        try:
            opcao = int(input("Digite uma opção de 0 a 8: "))
            if opcao in (0,1,2,3,4,5,6,7):
                return opcao
            else:
                print("Valor inválido! Digite um valor entre 0 a 8.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_dias():
     while True:
        try:
            opcao = int(input("Quantos dias deseja alugar? \n Digite uma opção de 1 a 360: "))
            if opcao in range(1,361):
                return opcao
            else:
                print("Valor inválido! Digite um valor entre 1 a 360.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_yesornot():
     while True:
        try:
            opcao = int(input("1 - SIM 2- NÃO"))
            if opcao in (1,2):
                return opcao
            else:
                print("Valor inválido! Digite um valor de 1 a 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_yes():
     while True:
        try:
            opcao = int(input("1 - SAIR"))
            if opcao ==1:
                return opcao
            else:
                print("Valor inválido! Digite um valor de 1 a 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_break():
     while True:
        try:
            opcao = int(input("Digite 1 - Sair"))
            if opcao in (1,2):
                return opcao
            else:
                print("Valor inválido! Digite um valor de 1 a 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

option = valid_valor()
codigo_carro = valid_carro()
dias=valid_dias()
yes_or_not = valid_yesornot()
yes_yes = valid_yes()

aluguel = carros[codigo_carro][1]*dias


valorremove=[]
# valorremove=[carros.pop(codigo_carro)]

while True :
    home()
    print("0- ver portifólio 1- alugar um carro   2-devolver um carro")
    valid_valor()
    if option == 0:
        clear()
        port()
        print('O que você deseja fazer? \n 1- alugar um carro   2-devolver um carro')
        valid_valor()
    elif option==1:
        clear()
        print("Você escolheu alugar um carro \n >> Escolha um carro e digite o código do carro <<")
        port()
        valid_carro()
        valid_dias()
        clear()
        print("Você escolheu {} por {} dias. \n".format(carros[codigo_carro][0],dias),  "o aluguél totaliza: ", aluguel, "quer continuar?" )
        yes_or_not()
        if yes_or_not == 1:
            clear()
            print("Parabéns, você alugou um carro \n Aperte [1] para sair ")
            valorremove=[carros.pop(codigo_carro)]
            yes_or_not()
            if yes_or_not == 1:
                continue
        elif yes_or_not == 2:
            continue
    elif option==2:
        if len(valorremove)==0:
            print("você não tem carros para devolver \n aperte qualquer tecla para sair:  ")
            input()
            continue
        else:
            print(valorremove)
            print("Aperte [1] para confirmar a devolução ou [2] para cancelar e sair \n deseja confirmar?")
            yes_or_not()
            if yes_or_not == 1:
                carros.extend(valorremove)
                del valorremove
                print("Devolução confirmada \n aperte qualquer tecla para sair:   ")
                input()
                continue
            elif yes_or_not == 2:
                continue

            
# print(carros)