#  ENCONTRAR ARQUIVOS 

from pathlib import Path
import os

print(Path('Python Starter'))

atual= Path.cwd()
outrocaminho= (Path(__file__))

print(outrocaminho)

print(Path(__file__))
caminho =Path.home()
print(caminho)

# Path.glob('**/*')
# for arq in Path.home().glob('**/*'):
#     if arq.is_file():
#         print(arq)

#  falta pesquisar em todo directório  qual é a pasta inicial?
#  falta pesquisar o nome do arquivo detalhe
#  transforme em uma função   detalhe
#  path.home pode ser o caminho inicial de procura  detalhe
#  quando achar, mostra o caminho completo do arquivo    nome da função