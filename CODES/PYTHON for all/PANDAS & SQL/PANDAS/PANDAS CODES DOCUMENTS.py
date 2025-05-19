import pandas as pd
# ??? Como add valor em cada célula com o data frame ????
try:
    df = pd.read_excel('TesteBrasilmadVBA.xlsx')

    '''PEGANDO SHEETS(tabelas)'''
    sheets_pandas_planílhas=list(df.keys())
    print(sheets_pandas_planílhas)
    df_sheet1=df[sheets_pandas_planílhas[0]]  #sheet1
    df_sheet2=df[sheets_pandas_planílhas[1]]       #sheet3
    df_sheet3=df[sheets_pandas_planílhas[2]]    #sheet3
    print(type(df_sheet1))

    '''MUDAR NOME DE COLUNA'''
    # Modificar o nome da coluna (exemplo: mudar 'coluna_antiga' para 'coluna_nova')
    df.rename(columns={'Unnamed: 1': "TELEFONE",'Unnamed: 2':'EMAIL', 'Unnamed: 3': 'NOME'}, inplace=True)


    ''' RESETAR INDEX'''
    df.reset_index(drop=True)
    df_sheet2=df_sheet2.iloc[5:].reset_index(drop=True) # com drop=True descarta outros índex


    '''PGAR LINHAS E COLUNAS'''
    df.iloc[:, 4]                # ''' : significa todas as linhas O 4 significa "quinta coluna" (começamos contando do 0) '''
    df.loc['linha por nome do índice']
    df[df.iloc[:, 4] == 'valor_filtro']       #  '''Guarda só as linhas que correspondem ao que queremos'''
    colunas = df.iloc[:, [0, 2]]  # Pega a primeira e a terceira coluna
    colunas = df.iloc[:, 1:3]  # Pega da segunda até a terceira coluna
    
    '''COPIANDO DATAFRAME sem alterar o valor do original, se fisser df2 = df1,  o df1 é alterado também'''
    df2=df.copy()
    '''concatenar dataframes'''
    df3=pd.concat([df,df2])

    '''Ver_os_Dados''' 
    display(df)  #  usa no lugar do print para organizar o dataframe
    print(df)  # mostra o df  5 linhas iniciais e 5 linhas finais
    print(df.shape) # mostra DF com as linhas e colunas ao final do DF
    df.head()    # Ver as primeiras 5 linhas
    # Ver as últimas 5 linhas
    df.tail()
    # Ver informações sobre os dados
    df.info()
    ''' Filtragem:'''
    # Pegar linhas onde idade > 10
    df[df['idade'] > 10]
    # Pegar linhas onde nome é 'João'
    df[df['nome'] == 'João']
    '''Ordenação'''
    # Ordenar por idade
    df.sort_values('idade')
    # Ordenar por idade de forma decrescente
    df.sort_values('idade', ascending=False)

    '''Cálculos:'''
    # Média de uma coluna
    df['idade'].mean()
    # Soma de uma coluna
    df['valor'].sum()
    # Contar valores únicos
    df['cor'].value_counts()

    '''Agrupamento:'''
    # Agrupar por cor e calcular média de idade
    df.groupby('cor')['idade'].mean()
    '''Criando novas colunas:'''
    # Criar coluna de dobro da idade
    df['idade_dobro'] = df['idade'] * 2


    '''Limpeza de dados:'''
    # seleciona somente o df que a coluna 'Unnamed: 1' não é nulo 
    df= df[df['Unnamed: 1'].notna()]   
    #  Remove as linhas que a  coluna 'Unnamed: 1' está vazia
    df = df.dropna(subset=['Unnamed: 1'])
    #  REMOVER AS PRIMEIRAS 3000 linhas 
    df = df.drop(range(0, 3001))   #ou
    df = df.iloc[3001:]
    # Remover linhas com valores faltantes
    df.dropna()
    db_sheet2.dropna(axis=1, how='all')  #how='all' quando todas as linhas da coluna forem vazias
    #  remove com pelo menos 2 valores ausentes na coluna
    df.dropna(axis=1,thresh=2)
    # Preencher valores faltantes com 0
    df.fillna(0)
    df.fillna(value='Conteúdo')  #troca os valores NaN por 'Conteúdo'
    # no valor NaN substitui pelo  valor da linha acima
    df.ffill()
    df.bfill()# no valor NaN substitui pelo último valor da coluna

    df['A'].fillna(value=df['A'].mean())

    '''Copiando Dados   _ excel v'''
    # Copiar só algumas colunas que você quer
    colunas_importantes = df[['nome', 'idade', 'cor']]
    # Copiar sem repetir valores
    valores_unicos = df['nome'].unique()

    '''Transformando Dados:'''
    # Trocar todos os valores de uma coluna
    df['idade'] = df['idade'].replace(10, 11)  # Troca todos 10 por 11
    # Aplicar uma mudança em toda coluna
    df['nome'] = df['nome'].str.upper()  # Deixa tudo maiúsculo

    '''Juntando Planilhas '''
    # Juntar lado a lado (merge)
    novo_df = pd.merge('df1', 'df2', on='nome')
    # Empilhar uma em cima da outra (concat)
    df_grandao = pd.concat(['df1', 'df2'])

    '''Trabalhando com Datas'''
    # Transformar texto em data
    df['data'] = pd.to_datetime(df['data'])
    # Pegar só o mês ou ano
    df['mes'] = df['data'].dt.month
    df['ano'] = df['data'].dt.year

    '''Salvando de Formas Diferentes:'''
    # Salvar em Excel bonitinho
    df.to_excel('arquivo_novo.xlsx', index=False)
    # Salvar em CSV
    df.to_csv('arquivo.csv', sep=';')

    # Groupby -----> O método groupby permite agrupar linhas de dados em conjunto e chamar funções agregadas
    df.groupby('Empresa').mean() # mean é média quando agrupa valores
    df.groupby('Empresa').min() # mínimo de cada grupo
    df.groupby('Empresa').max() # máximo de cada grupo
    






    ''' codes: inserir e substituir valores na planílha'''
    # 🔹 Inserir os novos dados diretamente no DataFrame
    linha_inicio = 16  # C17 no Excel (zero-indexado)
    colunas = list(range(2, 12))  # C até L (coluna 2 até 11 no zero-indexado)

    df_excel.iloc[linha_inicio:linha_inicio+len(df_novos_dados), colunas] = df_novos_dados.values

    # 🔹 Salvar de volta no Excel
    df_excel.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")

except:
    pass
