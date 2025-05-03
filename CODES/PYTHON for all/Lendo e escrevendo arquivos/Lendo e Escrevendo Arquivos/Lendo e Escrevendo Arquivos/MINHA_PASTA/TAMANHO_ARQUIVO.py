import os
from pathlib import Path

caminho_atual = Path.cwd()
# os.path.getsize(caminho_atual)
# print(os.path.getsize(caminho_atual))

# retorna_tamanho_dos_directorios(Path.home()/'documents', profundidade=1)

# caminho = Path(caminho)
#     resultados = []

#     # Gera padrões de busca para cada nível de profundidade
#     for nivel in range(1, profundidade + 1):
#         padrao_nivel = "/".join(["*"] * nivel)  # Cria o padrão, e.g., *, */*, */*/*, etc.
#         resultados.extend(caminho.glob(padrao_nivel + "/" + padrao))  # Busca arquivos com o padrão

def retorna_tamanho_dos_directorios (caminho, profundidade): 
    pass
ali=5*'/*'
profundidade = 8

profundidades = "/".join(["*"] * profundidade)
pastas = Path().home().glob(profundidades)

# pastas = Path().home().glob('*')



for pasta in pastas:
    
    if pasta.is_dir():
        # print(type())
        print(str(pasta).split("\\")[-1], (os.path.getsize(pasta))/1000, "Mb")

