import os

def espadiv():
    print('\n' + "-" * 20 + '\n')
def clear_tela():
    os.system("cls" if os.name == "nt" else "clear")
def port():
    print("Bem-vindo ao portfólio \n>> Escolha um carro <<")
    for count, carro in enumerate(carros):
        print(f"{count} - {carro[0]} (R$ {carro[1]}/dia)")

# valid
def valid_valor():
    while True:
        try:
            opcao = int(input("Digite uma opção (0, 1, 2 ou 3): "))
            if opcao in (0, 1, 2, 3):
                return opcao
            else:
                print("Valor inválido! Digite um valor entre 0 e 3.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_carro():
    while True:
        try:
            opcao = int(input(f"Digite uma opção de 0 a {len(carros) - 1}: "))
            if 0 <= opcao < len(carros):
                return opcao
            else:
                print(f"Valor inválido! Digite um valor entre 0 e {len(carros) - 1}.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_dias():
    while True:
        try:
            opcao = int(input("Quantos dias deseja alugar? (1 a 360): "))
            if 1 <= opcao <= 360:
                return opcao
            else:
                print("Valor inválido! Digite um valor entre 1 e 360.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
def valid_yesornot():
    while True:
        try:
            opcao = int(input("1 - SIM | 2 - NÃO: "))
            if opcao in (1, 2):
                return opcao
            else:
                print("Valor inválido! Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def home():
    clear_tela()
    print("Bem-vindo ao aluguel de carros")
    print("O que você deseja fazer?")
    print("0 - Ver portfólio")
    print("1 - Alugar um carro")
    print("2 - Devolver um carro")
    print("3 - Sair")




carros = [
    ["Chevrolet Tracker", 120],
    ["Onix", 90],
    ["Spin", 150],
    ["HB20", 85],
    ["Tucson", 120],
    ["Uno", 60],
    ["Mobi", 70],
    ["Pulse", 130],
]

valorremove = []


while True:
    home()
    option = valid_valor()

    if option == 0:  # Ver portfólio
        clear_tela()
        port()
        input("\nPressione Enter para voltar ao menu principal...")

    elif option == 1:  # Alugar um carro
        clear_tela()
        print("Você escolheu alugar um carro. \n>> Escolha um carro e digite o código correspondente <<")
        port()
        codigo_carro = valid_carro()
        dias = valid_dias()
        aluguel = carros[codigo_carro][1] * dias
        clear_tela()
        print(f"Você escolheu {carros[codigo_carro][0]} por {dias} dias.")
        print(f"O valor total do aluguel será: R$ {aluguel:.2f}")
        print("Deseja confirmar o aluguel?")
        yes_or_not = valid_yesornot()
        if yes_or_not == 1:
            valorremove.append(carros.pop(codigo_carro))
            print("\nParabéns, você alugou o carro!")
        else:
            print("\nAluguel cancelado.")
        input("\nPressione Enter para voltar ao menu principal...")

    elif option == 2:  # Devolver um carro
        clear_tela()
        if not valorremove:
            print("Você não tem carros para devolver.")
        else:
            print("Carros alugados:")
            for i, carro in enumerate(valorremove):
                print(f"{i} - {carro[0]}")
            print("\nDeseja confirmar a devolução?")
            yes_or_not = valid_yesornot()
            if yes_or_not == 1:
                carros.extend(valorremove)
                valorremove.clear()
                print("\nDevolução confirmada!")
            else:
                print("\nDevolução cancelada.")
        input("\nPressione Enter para voltar ao menu principal...")

    elif option == 3:  # Sair
        print("Obrigado por usar o sistema de aluguel de carros. Até a próxima!")
        break
