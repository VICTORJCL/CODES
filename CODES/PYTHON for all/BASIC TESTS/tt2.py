import os
# Obtém o diretório do arquivo atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)
print(caminho_atual)
print(str(caminho_atual))
print('aqui')
print(type(caminho_atual))


pessoas = {"Alice": 25, "Bob": 38, "Carlos": 62, "Daniel": 19, "Eva": 45, "Fernando": 31, "Gabriela": 28, "Hugo": 55, "Isabela": 16, "João": 70, "Karina": 22, "Lucas": 35, "Maria": 48, "Nathan": 12, "Olivia": 65, "Pedro": 29, "Raquel": 51, "Sofia": 18, "Thiago": 42, "Ursula": 68}


acima_50 = {x:y for x,y in pessoas.items() if y >=60}

print(acima_50)

# for x in pessoas.items():
    # print(type(x))