import re
import os

# ----------------------------------------------------------------------------------
# SOBRESCREVE O ARQUIVO PRINCIPAL MAS QUANDO CHAMA A VARIÁVEL ELE NÃO PEGA ATUALIZADO, 
# PEGA SEMPRE O VALOR DA SOBRESCRITA ANTIGA
# ---> ÚTIL PARA UM CONTADOR QUE PRECISA SER ARMAZENADO O RESULTADO ANTERIOR
# ----------------------------------------------------------------------------------

var = 22

def modify_var(new_value):
    file_path = __file__
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    pattern = re.compile(r'^var\s*=\s*')
    for i, line in enumerate(lines):
        if pattern.match(line.strip()):
            lines[i] = f'var = {repr(new_value)}\n'
            break
    
    with open(file_path, 'w') as f:
        f.writelines(lines)

# Exemplo de uso:
modify_var(22)



os.chdir(os.path.dirname(os.path.abspath(__file__)))
from time import sleep


# ----------------------------------------------------------------------------------
#  arquivo cria um arquivo secundário e lê ele depois de ser criado
# w -> cria e sobrescreve o arquivo
# w+ -> abre para escrita e leitura, cria o arquivo se não existir, e trunca (apaga) o conteúdo existente
# r+ -> lê e escreve sem sobrescrever mas não cria o arquivo
# ----------------------------------------------------------------------------------
with open('main.py','w') as w:
    w.write(f'alimentos="tutuu tuuu tutuu"')

sleep(2)
# lê o arquivo e variável mesmo se não existir
from main import alimentos
# print(alimentos)
# print('deu certo mesmo com erro')



# ----------------------------------------------------------------------------------
# lê todas das linhas do arquivo e coloca em cada uma lista readlines()
# escreve todo conteúdo e com \n add cada uma em uma linha
with open('main.py','r+') as w:
    a=w.readlines()
    print(a)
    w.writelines (['\nasd=23','\naaa=222','\nbbb=333'])
sleep(2)