from pathlib import Path
import os
import shutil
import zipfile

pasta_atual = Path('C:/Users/victo/Desktop/ORGANIZADORARQUIVOS/organizada')

arquivos=os.listdir(pasta_atual)

arquivo=str(arquivos[0])
caminho_completo=pasta_atual/arquivo



# Criar arquivo ZIP
# with zipfile.ZipFile('backup.zip', 'w') as zip_file:
#     # Adicionar arquivo ao ZIP
#     zip_file.write(str(caminho_completo ), 'FINALMENTE COMPACTADO!!!!' )


shutil.make_archive(caminho_completo/"pastinha",'zip',pasta_atual)

# shutil.make_archive(
#     base_name=caminho_completo.replace('.csv', ''),  # Nome base sem extensão
#     format='zip',  # Formato de compressão
#     root_dir=pasta_atual  # Diretório raiz a ser compactado
# )

# with zipfile.ZipFile(str(pasta_atual) + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
#     for arquivo in os.listdir(pasta_atual):
#         caminho_arquivo = pasta_atual / arquivo
#         zipf.write(caminho_arquivo, arquivo)