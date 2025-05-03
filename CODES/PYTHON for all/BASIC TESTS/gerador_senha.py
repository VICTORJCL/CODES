import random

def gerar_senha():
    mi = "abcdefghijklmnopqrstuvwxyz"
    num = '123456789'
    ma = mi.upper()
    tudo = mi + ma + num
    
    # Gera senha inicial
    senha = ''.join(random.choices(tudo, k=8))
    
    # Garante pelo menos um de cada tipo
    tem_minuscula = any(c in mi for c in senha)
    tem_maiuscula = any(c in ma for c in senha)
    tem_numero = any(c in num for c in senha)
    
    # Se faltar algum requisito, substitui caracteres aleatórios
    senha_lista = list(senha)  # Converte para lista para poder modificar
    
    if not tem_minuscula:
        senha_lista[random.randint(0, 7)] = random.choice(mi)
    if not tem_maiuscula:
        senha_lista[random.randint(0, 7)] = random.choice(ma)
    if not tem_numero:
        senha_lista[random.randint(0, 7)] = random.choice(num)
    
    senha_final = ''.join(senha_lista)
    return senha_final

# Teste a função
senha = gerar_senha()
print(senha)