import os
import shutil
os.chdir("/PYTHON for All/OS/PASTA1")
os.getcwd()
os.listdir()

arquivos=[i for i in os.listdir() if os.path.isfile(i)]

atual_direc = 'php.php'

destino_direc= 'p2/php.php'

# shutil.move(atual_direc,destino_direc)
# os.rename(atual_direc,destino_direc)
os.rename(destino_direc,atual_direc)