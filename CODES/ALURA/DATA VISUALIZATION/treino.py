import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# df=pd.read_csv('canadian_immegration_data.csv')

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

df =pd.DataFrame(vendas_2022)
df=df.T
df.columns=lojas
df['A']
# plt.plot(df)
df.columns
plt.plot(df.index, df['A'])
plt.plot(df['B'])
plt.plot(df['C'])
plt.plot(df['D'])

# Desafio 2/3

fig, axs = plt.subplots(2, 2, figsize=(10,6))
# titilo
fig.suptitle('Tendências de Venda por loja')

# espaçamento
fig.subplots_adjust(hspace=0.5,wspace=0.3)

axs[0, 0].plot(df.index, df['A'])
axs[0, 0].set_title('Loja A')


axs[0, 1].plot(df.index, df['B'])
axs[0, 1].set_title('Loja B')

axs[1, 0].plot(df.index, df['C'])
axs[1, 0].set_title('Loja C')

axs[1, 1].plot(df.index, df['D'])
axs[1, 1].set_title('Loja D')


for ax in axs.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adicionando rótulos para os eixos X e Y
for ax in axs.flat:
    ax.set_xlabel('MÊS')
    ax.set_ylabel('Quantia de Venda')


# Definindo a mesma escala no eixo Y em todos os subplots
ymin = 0
ymax = 400
for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)

plt.show()