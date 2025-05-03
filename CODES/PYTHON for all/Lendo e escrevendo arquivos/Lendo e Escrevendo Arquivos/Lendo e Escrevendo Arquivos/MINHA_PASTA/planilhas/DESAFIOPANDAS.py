from pathlib import Path
import pandas as pd
import os
Pasta_local = Path(__file__).parent
arq_completo= Pasta_local/"planilhas"/"clientes.xlsx"
planilha_separada= Pasta_local/"planilhas"/"planilhas_separadas"
# print(os.listdir(arq_completo))

#  leitura:
 
Tabela_clientes =  pd.read_excel(arq_completo)
print(Tabela_clientes.head())