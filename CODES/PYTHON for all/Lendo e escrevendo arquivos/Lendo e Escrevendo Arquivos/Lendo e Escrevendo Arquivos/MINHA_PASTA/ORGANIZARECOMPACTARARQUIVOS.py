from pathlib import Path
import shutil

# Define o caminho base onde os arquivos estão
pasta_base = pasta_atual = Path('C:/Users/victo/Desktop/DATA/OS/PASTA1')

# Lista todos os arquivos na pasta base
todos_arq_lista = [arq for arq in pasta_base.glob('*') if arq.is_file()]

# Para cada arquivo encontrado, organiza por extensão
for arquivo in todos_arq_lista:
    # Obtém a extensão do arquivo (sem o ponto inicial)
    sufixo = arquivo.suffix.lstrip('.')
    
    # Se não houver extensão, pula para o próximo arquivo
    if not sufixo:
        continue

    # Cria uma pasta com o nome da extensão, se não existir
    nova_pasta = pasta_base / sufixo
    nova_pasta.mkdir(exist_ok=True)

    # Move o arquivo para a pasta correspondente
    destino = nova_pasta / arquivo.name
    shutil.move(str(arquivo), str(destino))

# Cria uma pasta de backup
backup_pasta = pasta_base / "backup"
backup_pasta.mkdir(exist_ok=True)

# Copia todas as pastas (exceto a de backup) para a pasta de backup
for dir_pasta in pasta_base.glob('*/'):
    if dir_pasta != backup_pasta:
        destino_backup_pasta = backup_pasta / dir_pasta.name
        shutil.copytree(str(dir_pasta), str(destino_backup_pasta), dirs_exist_ok=True)
        print(f"Pasta copiada para o backup: {dir_pasta}")

# Compacta cada pasta dentro do backup
for comp in backup_pasta.glob('*/'):
    # Define o caminho para o arquivo ZIP que será criado
    para_pasta = backup_pasta / comp.name

    # Cria o arquivo ZIP da pasta atual
    shutil.make_archive(str(para_pasta.with_suffix('')), 'zip', root_dir=str(comp))
    print(f"Arquivo ZIP criado: {para_pasta.with_suffix('.zip')}")
