ani= 'abcdefghijklmnopqrstuvkxyv'


my_d = dict(ani=25, rafa=35, meli=40, jana=30, roberta=10, lisa=10)

my_d['isa']= 18
my_d.pop('isa')

my_d['lisa']= 20

acima_30=[x for x in my_d]
print(acima_30)

# my_d.clear()
print(my_d)

print(len(my_d))
print(list(my_d.items())[-1])
print(list(my_d.keys())[-1])
print(list(my_d.values())[-1])

my_d[list(my_d.keys())[-1]] = 30

print(my_d)


ccdic={ani[i]:i for i in range(len(ani))}




mind= [x for x in my_d.items()]
print(mind[-3])

print(mind)






# cond= {x for x in my_d if x.value > 30}

# dddic={my_d[]:i for i in range(len(my_d))}


# print(ccdic)
# print(dddic)


'''
 Método 2: Usando list() (menos eficiente para dicionários grandes)
ultimo_par = list(dicionario.items())[-1]
print(ultimo_par)  # Saída: ('d', 4)

# Método 3: Para pegar só a última chave
ultima_chave = list(dicionario.keys())[-1]
print(ultima_chave)  # Saída: 'd'

# Método 4: Para pegar só o último valor
ultimo_valor = list(dicionario.values())[-1]

'''