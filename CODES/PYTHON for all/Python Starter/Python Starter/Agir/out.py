import os

# Obtém o diretório atual
os.chdir('/PYTHON for All/Python Starter/Python Starter/Agir/OS EXER')
cwd = os.getcwd()

# Lista apenas as pastas no diretório atual
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, i))]

# Itera sobre cada pasta
for folder in folder_list:
    path = os.path.join(cwd, folder)  # Caminho completo da pasta

    # Lista os arquivos dentro da pasta
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # Move cada arquivo para o diretório principal
    for file in files:
        from_path = os.path.join(path, file)  # Caminho completo do arquivo na subpasta
        to_path = os.path.join(cwd, file)  # Caminho final no diretório principal
        
        # Verifica se o arquivo já existe no destino
        if not os.path.exists(to_path):
            os.replace(from_path, to_path)
            print(f"Movido: {from_path} -> {to_path}")
        else:
            print(f"Arquivo já existe no destino: {to_path}")
    os.rmdir(path)



























# import os

# cwd=os.getcwd()

# folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

# for folder in folder_list:
#     path=os.path.join(cwd,folder)

#     files=os.listdir(path) 
#     for file in files:
#         from_path = os.path.join(path,file)
#         to_path=os.path.join(cwd,file)
#         os.replace(from_path,to_path)

