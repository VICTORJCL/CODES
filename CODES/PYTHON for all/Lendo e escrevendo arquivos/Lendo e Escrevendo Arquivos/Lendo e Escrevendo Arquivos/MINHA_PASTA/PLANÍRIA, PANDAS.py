from pathlib import Path
import pandas as pd
import os
Pasta_local = Path(__file__).parent
arq_completo= Pasta_local/"planilhas"/"clientes.xlsx"
planilha_separada= Pasta_local/"planilhas"/"planilhas_separadas"
# print(os.listdir(arq_completo))

#  leitura:
 
#  cria um dicionário com sheet_name=None  e Tabela_clientes.items()
Tabela_clientes =  pd.read_excel(arq_completo, sheet_name=None)


#  criando planírias separadas:
def separadas():
    for key, value in Tabela_clientes.items():
        value.to_excel(planilha_separada/f'{key}.xlsx', index=False)

#  consolidando planíria:

# planilha_separada
with pd.ExcelWriter (planilha_separada/"planíria_completa.xlsx") as consolidada:
    for planilhas in planilha_separada.glob("*.xlsx"):
            tabela_clientes = pd.read_excel(planilhas)
            tabela_clientes.to_excel(consolidada, sheet_name=planilhas.stem, index=False)

# tabela_clientes = pd.read_excel(caminho_planilha, sheet_name=None)

# for key, value in tabela_clientes.items():
#     value.to_excel(pasta_atual / 'planilhas' / 'planilhas_separadas' / f'{key}.xlsx', index=False)

















    # Tabela_clientes_RS =  pd.read_excel(arq_completo, sheet_name='RS', index_col=0)
# Tabela_clientes_SC =  pd.read_excel(arq_completo, sheet_name='SC', index_col=0)
# Tabela_clientes_PR =  pd.read_excel(arq_completo, sheet_name='PR', index_col=0)
# Tabela_clientes_SP =  pd.read_excel(arq_completo, sheet_name='SP', index_col=0)


# Tabela_clientes_PR.to_excel(planilha_separada/"clientes_PR.xlsx")
# # print(Tabela_clientes_PR.head(100000))

# print(pd.read_excel(planilha_separada/"clientes_PR.xlsx"))

# with pd.ExcelWriter(Tabela_clientes) as writer:  
#     Tabela_clientes_PR.to_excel(writer, sheet_name='PR')
#     Tabela_clientes_RS.to_excel(writer, sheet_name='RS')