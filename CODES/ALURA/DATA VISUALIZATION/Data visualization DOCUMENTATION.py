import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/content/imigrantes_canada.csv')

''' CONVERTENDO DADOS PARA DF'''
#  convertendo dados para dataframe
anos = list(map(str, range(1980, 2014)))
brasil = df.loc['Brasil', anos]
brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)

''' ESCONDER META DADOS  E MOSTRAR SOMENTE O GRÁFICO'''
# A função plt.show() é utilizada para exibir o gráfico que foi criado com o Matplotlib. 
# Quando você chama essa função, apenas o gráfico é mostrado na tela, sem as
# informações adicionais que aparecem durante a execução do código. É importante lembrar que, após usar plt.show(),
#  nenhum código abaixo dessa linha será executado, pois a execução do Python é interrompida.
plt.show()   # Esconde abaixo dele também


'''PLOTAR GRÁFICO DE LINHAS (SEM FIGURA)'''
plt.figure(figsize=(8,4))
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
#  TÍTULO
plt.title('Imigração do Brasil para o Canadá')
#  LEGENDA X E Y
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
# INTERVALO RANGE X
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.show()