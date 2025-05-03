import os

# /PYTHON for All/Python Starter/Python Starter/AÇÃO/exercicios/OS EXER

dir_atual=os.chdir('/PYTHON for All/Python Starter/Python Starter/Agir/OS EXER')



cwb=os.getcwd()
full_list=os.listdir()



lstem  = [x for x in full_list if os.path.isfile(x) ]
nova_lis=set([ i.split('.')[-1] for i in lstem])

print (lstem)
def criar_pasta():
    for i in nova_lis:
        os.mkdir(i)



def organizar():
    for i in lstem:
        atual=i
        dest=f"{i.split('.')[-1]}/{i}"
        print(dest)
        os.rename(atual,dest)

for i in lstem:
        atual=i
        dest=f"{i.split('.')[-1]}/{i}"
        print(dest)
        os.rename(dest,atual)












# tete="tes 1.txt"
# dirc= "html/tes1.txt"





    # dest_in_pasta=(f"{os.getcwdb()}/{i.split('.')[-1]}/{i}")

    # atualdir = os.path.join(cwb,i)
    # destin = os.path.join(cwb,i.split('.')[-1],i)

# for i in lstem:
    # os.rename(i,f"/PYTHON for All/Python Starter/Python Starter/AÇÃO/exercicios/OS EXER/{nova_lis[nu]}"/{nova_lis[nu]} )

    # extensao = i.split('.')[-1]
    # destino = f"/PYTHON for All/Python Starter/Python Starter/AÇÃO/exercicios/OS EXER/{extensao}"  # Define o caminho de destino
    # os.rename(i, i/destino) 
    # nu+=1
# for arquivo in lstem:
#     extensao = arquivo.split('.')[-1]  # Obtém a extensão do arquivo
#     destino = os.path.join(extensao, arquivo)  # Define o caminho de destino
#     os.rename(arquivo, destino)  # Move o arquivo
#     print(f"Movido: {arquivo} -> {destino}")