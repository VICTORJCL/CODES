import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja.head()
llojas_lista=[loja,loja2,loja3,loja4]

lojas=['loja_1','loja_2','loja_3','loja_4']


loja2.columns

loja.columns.values
# colunas=['Produto', 'Categoria do Produto', 'Preço', 'Frete',
#        'Data da Compra', 'Vendedor', 'Local da compra',
#        'Avaliação da compra', 'Tipo de pagamento',
#        'Quantidade de parcelas', 'lat', 'lon']

# categorias_únicas=set(loja['Categoria do Produto'].values)  #todas as categorias de produtos

# média de avaliação
media_avaliação_1=loja['Avaliação da compra'].mean()  
media_avaliação_2=loja2['Avaliação da compra'].mean()  
media_avaliação_3=loja3['Avaliação da compra'].mean()  
media_avaliação_4=loja4['Avaliação da compra'].mean() 

medias_2decimais=[float(str(x)[:4]) for x in [media_avaliação_1,media_avaliação_2,media_avaliação_3,media_avaliação_4]] # converte para 2 casas decimais
medias_2decimais

plt.bar_label(plt.bar(lojas,medias_2decimais))
plt.ylabel('Média de Avaliação')
plt.xlabel('Lojas')
plt.tight_layout()


# análise do faturamento
plt.bar_label(plt.bar(lojas, (loja['Preço'].sum(),loja2['Preço'].sum(),loja3['Preço'].sum(),loja4['Preço'].sum())), fmt='%.2f')  # Formato com 2 casas decimais
plt.ylabel('Faturamento milhões')
plt.tight_layout()



'''Lucro (faturamento -  frete)'''
plt.bar_label(plt.bar(lojas, (loja['Preço'].sum() - loja['Frete'].sum(),loja2['Preço'].sum() - loja2['Frete'].sum(),loja3['Preço'].sum() - loja3['Frete'].sum(),loja4['Preço'].sum() - loja4['Frete'].sum())), fmt='%.2f')  # Formato com 2 casas decimais
plt.ylabel('Faturamento milhões')
plt.tight_layout()



# vendas por categoria

vendas_por_categoria_loja1 = loja['Categoria do Produto'].value_counts()
vendas_por_categoria_loja2 = loja2['Categoria do Produto'].value_counts()
vendas_por_categoria_loja3 = loja3['Categoria do Produto'].value_counts()
vendas_por_categoria_loja4 = loja4['Categoria do Produto'].value_counts()


vvendas_cat=vendas_por_categoria_loja1,vendas_por_categoria_loja2,vendas_por_categoria_loja3, vendas_por_categoria_loja4

plt.pie(vvendas_cat[0], labels=vvendas_cat[0].index, autopct='%1.1f%%')
plt.title('Vendas por Categoria')




# produtos mais e menos vendidos

for i in range(len(llojas_lista)):
    print(f'---{lojas[i]}---\n')

    top_mais = llojas_lista[i]['Produto'].value_counts().head(5)
    top_menos = llojas_lista[i]['Produto'].value_counts().tail(5)

    print("MAIS VENDIDOS:\n", top_mais)
    print("\nMENOS VENDIDOS:\n", top_menos,"\n\n")



# frete médio por loja

frete_l1=loja['Frete'].mean()
frete_l2=loja2['Frete'].mean()
frete_l3=loja3['Frete'].mean()
frete_l4=loja4['Frete'].mean()
fretes = [frete_l1, frete_l2, frete_l3, frete_l4]

plt.figure(figsize=(10, 6))
plt.plot(lojas, fretes, 'o-', linewidth=2, markersize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Comparação de Fretes por Loja')
plt.ylabel('Valor do Frete')
plt.show()