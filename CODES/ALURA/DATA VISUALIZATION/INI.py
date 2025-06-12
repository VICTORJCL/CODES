import pandas as pd
import matplotlib.pyplot as plt



lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}




df= pd.DataFrame(vendas_2022)
df.T
df.index.name='mês'
df.columns
df.iloc['mês']
# df.reset_index()


fig, axs = plt.subplot(2,2, figsize=(10,6))

axs[0,0].plot(df.loc['A'])
axs[0,0]








# Criando a figura
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# Ajustando o espaçamento
fig.subplots_adjust(hspace=0.5, wspace=0.3)

# Subplots
axs[0, 0].plot(df.loc['0'],lojas)
axs[0, 0].set_title('loja A')

axs[0, 1].plot(df.loc['1', lojas])
axs[0, 1].set_title('B')

axs[1, 0].plot(df.loc['2', lojas])
axs[1, 0].set_title('C')

axs[1, 1].plot(df.loc['3', lojas])
axs[1, 1].set_title('D')

# Alterando a frequência dos ticks do eixo X em todos os subplots
for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# Adicionando rótulos para os eixos X e Y
for ax in axs.flat:
    ax.set_xlabel('Ano')
    ax.set_ylabel('Número de imigrantes')

# Definindo a mesma escala no eixo Y em todos os subplots
ymin = 0
ymax = 7000
for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)

plt.show()

