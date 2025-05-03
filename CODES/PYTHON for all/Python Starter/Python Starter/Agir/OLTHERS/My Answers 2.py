#  nota avaliação
# nota1 = float(input("digite uma nota de 1 a 10  "))
# nota2 = float(input("digite uma nota de 1 a 10  "))
# média= nota1+nota2
# def avalia (x): 
#     if x >=7:
#         print('aprovado')
#     elif x == 10:
#         print('aprovado com Distinção')
#     else:
#         print( 'reprovado')
# avalia(média)

# 2 leia 3 números e retorne o maior entre eles

# n1 = float(input("digite um número  "))
# n2 = float(input("digite um número  "))
# n3 = float(input("digite um número  "))

# lis= [n1,n2,n3]
# lis.sort()
# print("o maior número é {} e o menor número é {}".format(lis[-1],lis[0]))

# nome vertical em escada

# nome = input("digite um nome ")
# nome = "fulano"
# st=[""]
# st=""
# for w in nome :
#     st=st + w
#     print(st)

# ou >>>>>

# nome = input("digite um nome ")
# for i in range(len(nome)+1):
#     print(nome[:i])

# FIBONACCI

# nfinal= int(input("digite quantos laços a sequência de Fibonacci vai chegar  "))
# def fibonacci(x):
#     fibo=[1,1]
#     for i in range(x):
#         fibo.append(fibo[-1] +fibo[-2])
#     print(fibo)
# fibonacci(nfinal)


# nom=str(input('dugite seu nome:  '))
# ida=int(input('dugite seu sua idade:  '))
# salar=float(input('dugite seu salário:  '))
# morf=str(input('seu gênero é masculino (m) ou feminino(f)? :  '))
# estad=str(input('qual seu estado civil? casado (c), solteiro (s), divorciado (d) ou viuvo (v) :  '))
# morf.lower
# estad.lower

# test # nome=[""]
# while (nome[0]!="m"):
    # nome=str(input("digite m"))   # a string não pode estar vazia pois o nome[0] requer um elemento mas você pode colocar em lista
    

# nom=str("")
# ida=0
# salar=0
# morf=input("seu gênero é masculino (m) ou feminino(f)? : ")
# while(len(nom)<3):
#     nom=str(input('dugite seu nome:  '))
# while(ida<0 or ida>150):
#     ida=int(input('dugite seu sua idade:  '))  
# while(salar<=0):
#     salar=float(input('dugite seu salário mensal:  '))
# while morf not in ["m","f"]:
    # morf=input("seu gênero é masculino (m) ou feminino(f)? : ")

# estad= input('qual seu estado civil? casado (c), solteiro (s), divorciado (d) ou viuvo (v) :  ')
# while estad not in ["c","s","d","v"]:
    # estad=input("qual seu estado civil? casado (c), solteiro (s), divorciado (d) ou viuvo (v) :  ")
# while(estad!="c" or estad!="s" or estad!="d" or estad!="v"):
#     estad=str(input('qual seu estado civil? casado (c), solteiro (s), divorciado (d) ou viuvo (v) :  '))


# é primo ou não?

num= int(input("digite um número"))
for i in range(2,num):
    if num%i==0:
        cont=0
        break
    else:
        cont=1

if cont==1:
    print("é primo")
else:
    print("não é primo")
    
