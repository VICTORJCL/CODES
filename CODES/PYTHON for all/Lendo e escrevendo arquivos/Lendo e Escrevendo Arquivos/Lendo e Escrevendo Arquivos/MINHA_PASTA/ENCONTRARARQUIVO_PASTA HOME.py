from pathlib import Path
import os

# resumo = [i for i in caminho.glob('**/*') if i.is_file() and i.stem == 'Avatar verde']
# print(resumo)

caminho = Path.home()
ddisco=Path("E:/")

def encontra (arq):

    
    for i in caminho.glob('**/*'):
        if i.is_file():
            if i.stem == arq:
                print(i)


def encontra_emD (arq):

    tudos = list(ddisco.glob('**/*'))
    for i in tudos:
        if i.stem == arq:
            print(i)



# encontra_emD("Pinguim.S01E06.1080p.WEB-DL.DUAL.5.1.mkv")
encontra('Avatar verde')
