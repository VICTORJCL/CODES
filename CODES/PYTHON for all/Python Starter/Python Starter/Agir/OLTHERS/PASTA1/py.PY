import os
# mostra o que tem dentro
os.getcwd()
os.listdir()
# mostra directório

# muda ação para directório
# os.chdir('C:\Users\victo\Desktop\DATA\OS\PASTA1')

atualdir=os.getcwd()

os.chdir('D:/PYTHON for All/OS/pasta1')
print(os.getcwd())

# os.mkdir("pasta 3.0")

# os.rename("pasta os12","pasta 2.0" )

# pega pasta 3 e coloca dentro da 2
# os.rename("pasta 3.0","pasta 2.0/pasta 3.0" )

# os.remove('js.js')
# os.remove('js.js')

os.rmdir('pasta os12')
