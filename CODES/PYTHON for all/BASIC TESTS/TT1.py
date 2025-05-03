def verifica_diferenca(lista):
    armazena=[]
    for i in lista:
        if i not in armazena:
            armazena.append(i)
        else:
            print("A lista possui valores iguais.")
    if armazena == lista:
        print("A lista possui apenas valores únicos.")

        
    print(armazena)
    print(lista)


verifica_diferenca([1, 5, 9, 8,1, 7, 10])



def verifica_diferenca(lista):
    conjunto = set(lista)
    print(conjunto)
    print(lista)
    if len(conjunto)!= len(lista):
        print("A lista possui valores iguais.")
    else:
        print("A lista possui apenas valores únicos.")