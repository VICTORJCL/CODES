from pathlib import Path
import shutil


# Criando pasta
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'
caminho_pasta_destino.mkdir(exist_ok=True)


# Criando pasta com todos as pastas anteriores necessárias
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino51'
caminho_pasta_destino.mkdir(parents=True)


# Copiando pastas
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'destino5', pasta_atual / 'destino1' / 'destino5')


# Deletando pastas vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino5' / 'destino51'
pasta_remover.rmdir()


# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1'
shutil.rmtree(pasta_remover)