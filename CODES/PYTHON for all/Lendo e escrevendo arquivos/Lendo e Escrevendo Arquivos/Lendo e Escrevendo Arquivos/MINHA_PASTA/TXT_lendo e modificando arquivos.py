from pathlib import Path


pasta_atual= Path(__file__).parent


with open(pasta_atual/'arqv.txt') as receita:
    # lendo= receita.readlines()
    lendo=[i.replace('\n','') for i in receita.readlines()]
print(lendo)

#  mode='w' reescreve e mode='a' adiciona
# with open(pasta_atual/'arqv.txt', mode='w') as receita:
#     item=["cebola", 'alho', 'beterraba']
#     for itm in item:
#         receita.write(itm + "\n")
#     print(receita)

with open(pasta_atual/'arqv.txt', mode='a') as receita:
    item=["cebola", 'alho', 'beterraba']
    for itm in item:
        receita.writelines(itm + "\n")
    print(receita)
