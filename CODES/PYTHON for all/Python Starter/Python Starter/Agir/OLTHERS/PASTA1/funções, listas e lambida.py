def par (x):
    pass

lista1= [w for w in range(5,21,5) if w%2==0]
print(lista1)

l=lambda x: x%2==0
print(l(21) )

def valido (x):
    if x==2:
        print("válido")
    elif x==6:
        print("válido")
    elif x==8:
        print("válido")
    else: 
        print("Inválido")

valido(6)
