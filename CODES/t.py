# import os
# # Obtém o diretório do arquivo atual
# caminho_atual = os.path.dirname(os.path.abspath(__file__))
# # Define o diretório de trabalho como o diretório do arquivoo
# os.chdir(caminho_atual)



def reverte_palavra(palavra):
    palavra_reverse=palavra[::-1]
    return print(palavra_reverse)

reverte_palavra('senhor')


''' 
# fatorial em python
cont=5
for i in range(2,cont):
    cont*=i
'''




import pandas as pd
# https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/edit?usp=sharing
id='1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw'


url_completa='https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/gviz/tq?tqx=out:csv&sheet'
df=pd.read_csv(url_completa)
df

