
lista = ["Olá", "mundo", "como", "vai", "você?"]
# Usando join para concatenar os itens da lista em uma única string
string_resultante = " ".join(lista)

lista = [1, 2, 3, 4, 5]
# Convertendo cada item para string e concatenando
string_resultante = " ".join(str(item) for item in lista)


# 2
paragrafo='sakdjklsf'
texto=paragrafo
if texto:  # Verifica se o texto não está vazio
    paragrafo.get_text().strip()   #strip() remove espaços em branco


'''conjuntos set()  não aceita valores repetidos, não tem ordem não funciona o conj[0], 
não aceita lista mas aceita tupra {1,2,(5,6)} Executa código mais rápido que listas'''
mlista=[1,2,2,3,3,5,5,4,4,1]
sem_repet=list(set(mlista))  #converte em conjunto, retira valores repetidos e converte em lista
conj={1, 2, 3, 4, 5}
a={1, 2, 3, 4}
b={4,5,6,7,8}
ab=a.union(b)  #união de conjuntos
ab=a|b  #união de conjuntos
acb= a.intersection(b)  #intersecão de conjuntos
acb= a & b #intersecão de conjuntos
a_b= a-b  #diferença
a_b= a.difference(b)  #diferença
aPb= a.symmetric_difference(b)  #tira intersecção e faz união

"dicionário forma resumida com for e if "
dic_valor_s5= {valor:valor+2 for valor in mlista if valor>2} # tradicional da lista mas com valor:valor_diferente
valores_em_dolares = {'leite': 0.78,'carne': 4.60,'maçã': 0.35,}
fator_conversao = 4.93
valores_em_reais = { #.items() necessário apra interar sobre chaves e valores 
produto: round(preco * fator_conversao, 2) for (produto, preco) in valores_em_dolares.items()
} 


''' match  == if else   // mas pode verificar o tipo de dado'''
op = '1'
match op:
    case int(op):
        print('int')
    case str(op):
        print('str')
    case _:
        print('outro')


''' outros divisores: /-> divisor normal   //-> divisor inteiro  %->  resto do divisor'''
65 / 60
65 // 60
65 % 60
res= f" {65//60 } minutos e {65%60} segundos"

''' if e else em uma linha no retorno de função, listas, dicionários...'''
# '''operadores ternários'''
def pegar_cor(valor):
    return 'vermelho' if valor < 0 else 'azul'
for valor in [10, -2, 3]:
    print(pegar_cor(valor))

numeros = [1, 2, 3, 4]
pares_quadrados = [ n**2 if n % 2 == 0 else n for n in numeros
]
#  ou 
pares_quadrados = [
n**2
if n % 2 == 0
else n
for n in numeros
]

novos_num=[ x**3 if x<3 else x-2 for x in numeros]

''' is   operador  para ver se é mesmo objeto'''
a=[1,2]
b=[1,2]
a==b  # True
a is b  # false,  por mais que sejam mesmos valores, o objeto é diferente

''' operador morsa :=  reduz 2 linhas em uma'''
n=5
while (n := n-1) >=0: # while n>0:   n-1
    print(n)
