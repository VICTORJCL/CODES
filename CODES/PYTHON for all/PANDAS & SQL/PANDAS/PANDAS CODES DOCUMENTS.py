import pandas as pd
# ??? Como add valor em cada célula com o data frame ????
try:
    '''Carregamento'''
    df = pd.read_excel('TesteBrasilmadVBA.xlsx')
    #  sep=';' significa separador por ; então identifica as colunas do csv que tem esse separador
    dados = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv', sep=';')


    '''PEGANDO SHEETS(tabelas)'''
    sheets_pandas_planílhas=list(df.keys())
    print(sheets_pandas_planílhas)
    df_sheet1=df[sheets_pandas_planílhas[0]]  #sheet1
    df_sheet2=df[sheets_pandas_planílhas[1]]       #sheet3
    df_sheet3=df[sheets_pandas_planílhas[2]]    #sheet3
    print(type(df_sheet1))

    ''' RESETAR INDEX'''
    df.reset_index(drop=True)
    df_sheet2=df_sheet2.iloc[5:].reset_index(drop=True) # com drop=True descarta outros índex
    
    '''CRIAR NOVAS COLUNAS:'''
    # Criar coluna de dobro da idade
    df['idade_dobro'] = df['idade'] * 2


    '''PGAR LINHAS E COLUNAS'''
    df.iloc[:, 4]                # ''' : significa todas as linhas O 4 significa "quinta coluna" (começamos contando do 0) '''
    df.loc['linha por nome do índice']
    df[df.iloc[:, 4] == 'valor_filtro']       #  '''Guarda só as linhas que correspondem ao que queremos'''
    colunas = df.iloc[:, [0, 2]]  # Pega a primeira e a terceira coluna
    colunas = df.iloc[:, 1:3]  # Pega da segunda até a terceira coluna
    
    '''COPIANDO DATAFRAME sem alterar o valor do original, se fisser df2 = df1,  o df1 é alterado também'''
    df2=df.copy()
    '''CONCATENAR dataframes'''
    df3=pd.concat([df,df2])

    '''Ver_os_Dados''' 
    df.info() # Ver informações sobre os TIPOS DE DADOS
    df.shape # QUANTIDADE DE LINHAS E COLUNAS
    df.tail() # Ver as últimas 5 linhas
    df.head()    # Ver as primeiras 5 linhas
     
    '''SUBSTITUIR VALORES  .replace() .apply(lambda...)'''
    df['Notas'] = df['Notas'].replace(7, 8) 
    # LAMBDA substitur valores por uma filtrabem
    df["Aprovado_final"] = df['Notas_finais'].apply(lambda x: True if x >=6 else False)  # troca para True se o valor é maior que 6 caso contrário fica False

    ''' FILTRAGEM:'''
    # Filtrar df de forma diferente de query: 
    selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
    # Pegar linhas onde idade > 10
    df[df['idade'] > 10]
    # Pegar linhas onde nome é 'João'
    df[df['nome'] == 'João']

    # FILTRAGEM DE VALORES QUE APARECEM UMA ÚNICA VEZ
    bairros_unicos = df[ df['Bairro'].map(df['Bairro'].value_counts() ==1)]
    bairros_unicos['Bairro'].unique()

    # selecionar UM DF com COLUNAS SELECIONADAS
    valores_df= df[["Idade","Notas"]]

    '''FILTRAGEM POR TIPO         query() e groupby() '''
    dados.query('@imoveis_comerciais in Tipo')
    df.query('Aprovado==False & Aprovado_final ==True')
    df.groupby(['Animal', 'Cor'])[['Quantidade']].sum()

    '''Agrupamento                  groupby()'''
    # Agrupar por cor e calcular média de idade
    df.groupby('cor')['idade'].mean()
    df.groupby(['Animal', 'Cor'])[['Quantidade']].sum()  # ORDENA POR ANIMAL, cor e soma a quantidade
    # média dos bairros que possuem média de aluguel mais elevada
    df.groupby(['Bairro'])[['Valor']].mean().sort_values("Valor",ascending=False).head(10)

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

    '''Limpeza de dados:'''
    # remover registros: drop() requer o index para remover tipo : [7, 8]
    df.drop(df.query('Nome == "Alice" | Nome == "Carlos"' ).index, axis=0, inplace=True)

    # Remover linhas com valores faltantes
    df.dropna()
    df.dropna(axis=1, how='all')  #how='all' quando todas as linhas da coluna forem vazias
    #  remove colunas com pelo menos 2 valores ausentes na coluna
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

    '''CRIANDO GRÁFICOS COM PLOT DIRETAMENTE''' #.plot(kind='bar', figsize=(10, 5), title='Top 5 ')
    df.groupby(['Bairro'])[['Valor']].mean().sort_values("Valor", ascending=False).head(5).plot(kind='bar', figsize=(10, 5), title='Top 5 Bairros com Maior Valor Médio')


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