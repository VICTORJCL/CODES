import pandas as pd
import os

def super_organizador_excel(pasta_arquivos, arquivo_saida):
    """
    Uma função mágica que:
    1. Junta todos os arquivos Excel de uma pasta
    2. Limpa os dados
    3. Organiza tudo bonitinho
    4. Salva em um novo arquivo
    """
    # Lista para guardar todos os DataFrames
    lista_df = []
    
    # Procura todos os arquivos Excel na pasta
    for arquivo in os.listdir(pasta_arquivos):
        if arquivo.endswith(('.xlsx', '.xls')):
            caminho = os.path.join(pasta_arquivos, arquivo)
            
            # Lê cada arquivo Excel
            df = pd.read_excel(caminho)
            
            # Adiciona uma coluna dizendo de qual arquivo veio
            df['arquivo_origem'] = arquivo
            
            # Guarda na lista
            lista_df.append(df)
    
    # Junta todos os DataFrames
    df_final = pd.concat(lista_df, ignore_index=True)
    
    # Limpa os dados
    df_final = df_final.dropna(how='all')  # Remove linhas totalmente vazias
    df_final = df_final.fillna('')  # Preenche células vazias com espaço em branco
    
    # Organiza por alguma coluna (exemplo: 'data' se existir)
    if 'data' in df_final.columns:
        df_final['data'] = pd.to_datetime(df_final['data'], errors='ignore')
        df_final = df_final.sort_values('data')
    
    # Salva o arquivo final
    df_final.to_excel(arquivo_saida, index=False)
    
    return df_final

# Exemplo de uso:
pasta = r'C:\Minha_Pasta_Com_Excels'
arquivo_final = 'Todos_Juntos_Organizados.xlsx'
df_organizado = super_organizador_excel(pasta, arquivo_final)