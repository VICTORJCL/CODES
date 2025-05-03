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
                

# Chamar a função e armazenar o resultado na variável interacao
opção = valid_valor()
print(f"O valor de interação é: {opção}")