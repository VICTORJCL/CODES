import pandas as pd
import os

# caminho_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir("C:\\CODES\\PYTHON for all\\PANDAS\\tut_youtube")



vendas_df=pd.read_excel('Vendas.xlsx')
print(vendas_df.head(5))

produto_idloja_venda=vendas_df[['Produto', 'ID Loja','Valor Final']]
sproduto_Ilock=vendas_df.iloc[:,[2,3,6]]

asepara_produto = vendas_df.loc[vendas_df.iloc[:, 2] == 'Iguatemi Esplanada', [2, 3, 6]]
asepara_produto = vendas_df.loc[vendas_df.iloc[:, 2] == 'Iguatemi Esplanada', [vendas_df.columns[2], vendas_df.columns[3], vendas_df.columns[6]]]

print(asepara_produto)

asepara_produto= vendas_df.loc[vendas_df.iloc[:,2]=='Iguatemi Esplanada', [2,3,6] ]  
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ["ID Loja", "Produto", "Quantidade"]]


print(sproduto_Ilock)