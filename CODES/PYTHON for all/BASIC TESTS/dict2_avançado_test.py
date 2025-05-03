pessoas = {"Alice": 25, "Bob": 38, "Carlos": 62, "Daniel": 19, "Eva": 45, "Fernando": 31, "Gabriela": 28, "Hugo": 55, "Isabela": 16, "João": 70, "Karina": 22, "Lucas": 35, "Maria": 48, "Nathan": 12, "Olivia": 65, "Pedro": 29, "Raquel": 51, "Sofia": 18, "Thiago": 42, "Ursula": 68}


# efficient métod
acima_50 = {x:y for x,y in pessoas.items() if y >=50}
acima_60 = {x:y for x,y in pessoas.items() if y >=60 and x.startswith('C')}

print('pessoas acimda de 50  ',acima_50)
print('pessoas acimda de 60 começando com C ',acima_60)










print(list(pessoas.items())[-1])

pessoas_maiores30=[x for x in pessoas.items() if list(x)[-1]>30]
print(dict(pessoas_maiores30))

valores_iniciais=('E','A','B','Ga', 'Ha')
print(type(valores_iniciais))
nomes_iniciam_A=[x for x in pessoas.items() if list(x)[0].startswith(valores_iniciais)]
print(dict(nomes_iniciam_A))

# x: nome_dict_variável[x] for x   mesma coisa e economizando código  
nomes_filtrados = {x: pessoas[x] for x in pessoas if x.startswith(valores_iniciais)}
print(nomes_filtrados)

def filtrar_nomes_INICIANDO_COM(letra):
    return print({x: pessoas[x] for x in pessoas if x.startswith(tuple(x.upper() for x in letra))})
    # TRANSFORMA LETRA EM TUPRA, PARA CADA ELEMENTO TRANSFORMA EM MAIÚSCULA. PEGA CADA ELEMENTO ITEM ONDE KEY QUE INICIA COM ALGUM DA VARIÁVEL LETRA E RETORNA UM DICIONÁRIO
filtrar_nomes_INICIANDO_COM('rtuga')

def filtrar_por_idade(numero):
    return print({x: pessoas[x] for x in pessoas if str(pessoas[x]).startswith(str(numero))})
filtrar_por_idade(4)

numero=2
ra={x: pessoas[x] for x in pessoas if str(pessoas[x]).startswith(str(numero))}

print(ra)




