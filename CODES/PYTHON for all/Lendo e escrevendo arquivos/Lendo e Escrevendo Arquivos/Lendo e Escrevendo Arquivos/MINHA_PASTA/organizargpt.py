from pathlib import Path
import shutil
import datetime

# Definindo os caminhos
pasta_atual = Path('C:/Users/victo/Desktop/DATA/OS/PASTA1')
# pasta_atual = pasta_atual.parent


pasta_a_organizar = pasta_atual / 'arquivos_desafio'
pasta_backups = pasta_atual / 'backups'

# Verificar se a pasta de backups existe, caso contrário criar
if not pasta_backups.exists():
    pasta_backups.mkdir()

# Criando um diretório temporário para organizar os arquivos
pasta_temp = pasta_atual / 'temp_organizada'

# Garantir que a pasta temporária não exista e criar uma nova
if pasta_temp.exists():
    shutil.rmtree(pasta_temp)
pasta_temp.mkdir()

# Organizando os arquivos por extensão dentro da pasta temporária
for arquivo in pasta_a_organizar.glob('**/*'):
    if arquivo.is_file():  # Verificando se é um arquivo (não pasta)
        pasta_com_extensao = pasta_temp / arquivo.suffix.replace('.', '')
        
        # Criando a pasta para a extensão, caso não exista
        if not pasta_com_extensao.exists():
            pasta_com_extensao.mkdir()
        
        # Copiar o arquivo para a pasta correspondente à extensão
        shutil.copy(arquivo, pasta_com_extensao)

    elif arquivo.is_dir():  # Se for uma pasta, copiar diretamente
        pasta_com_extensao = pasta_temp / arquivo.name
        shutil.copytree(arquivo, pasta_com_extensao)

# Criando o backup com data atual, sem a pasta "organizada"
nome_backup = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(pasta_backups / nome_backup, 'zip', pasta_temp)

# Remover a pasta temporária após o backup
shutil.rmtree(pasta_temp)
