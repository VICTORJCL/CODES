import pandas as pd
import openpyxl as op
# ??? falta estudar mais o regex,  manipulação de datas  e banco de dados????
try:

    '''Carregamento'''
    df = pd.read_excel('TesteBrasilmadVBA.xlsx', sheet_name='Sheet1')
    dados = pd.read_excel('TesteBrasilmadVBA.xlsx', sheet_name='Sheet1')
    dados_ponto_virgula = pd.read_csv(url_2, sep = ';')   # sep = ';' muda o separador de colunas csv, o padrão é virgula
    #  carregamento selecionando o intevalo de colunas do excel usecols= 'A:D' e o número de linhas nrows=10
    intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols= 'A:D', nrows=10)
    #  carregar somente usando certas colunas
    dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])   # ou
    dados_selecao = pd.read_csv(url, usecols=[0,1,4])
    #  NORMALIZANDO ARQUIVOS JSON
    df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])

    ''' INVERTE LINHAS PARA COLUNAS .T'''
    df= df.T
   
    ''' CONVERTER COLUNA DE DADOS'''
    import  numpy as np
    dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)
    #  para várias colunas:
    col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']
    dados[col_numericas] = dados[col_numericas].astype(np.float64)

    '''PEGANDO SHEETS(tabelas)'''
    arquivo=pd.ExcelFile('Desafio_Brasilmad\TesteBrasilmadVBA.xlsx')
    sheets=arquivo.sheet_names
    #  outra forma
    sheets_pandas_planílhas=list(df.keys())
    print(sheets_pandas_planílhas)
    df_sheet1=df[sheets_pandas_planílhas[0]]  #sheet1


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
    df = df.iloc[3001:] # sobrescrever o df pelas linhas selecionadas

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

    '''TRANSFORMAR DADOS PARA DATA'''
    # Transformar texto em data
    df['data'] = pd.to_datetime(df['data'])
    df['data'].dt.strftime('%Y-%m')
    # Pegar só o mês ou ano
    df['mes'] = df['data'].dt.month
    df['ano'] = df['data'].dt.year
    # MANIPULAÇÃO DE DATA
    #### O resultado final será uma série que mostra quantas vagas estavam disponíveis em cada mês do ano
    df.groupby(df['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()

    '''Juntando Planilhas '''
    # Juntar lado a lado (merge)
    novo_df = pd.merge('df1', 'df2', on='nome')
    # Empilhar uma em cima da outra (concat)
    df_grandao = pd.concat(['df1', 'df2'])

    '''Salvando de Formas Diferentes:'''
    # Salvar em Excel bonitinho
    df.to_excel('arquivo_novo.xlsx', index=False)   #salva sem a coluna index
    # Salvar em CSV
    df.to_csv('arquivo.csv', sep=';')

    # Groupby -----> O método groupby permite agrupar linhas de dados em conjunto e chamar funções agregadas
    df.groupby('Empresa').mean() # mean é média quando agrupa valores
    df.groupby('Empresa').min() # mínimo de cada grupo
    df.groupby('Empresa').max() # máximo de cada grupo
    
    """carregamento no google colab via google planílhas link"""
    ulr_bruta= 'https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/edit?usp=sharing'
    sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
    sheet_name = 'fontes'
    url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    fontes_sheets = pd.read_csv(url_fontes)

    ''' DESAGRUPAR dados .json'''
    dados = dados.explode(colunas[3:])
    dados.reset_index(inplace=True, drop=True) # resetar index e excluir as colunas antigas



    ''' codes: inserir e substituir valores na planílha'''
    # 🔹 Inserir os novos dados diretamente no DataFrame
    linha_inicio = 16  # C17 no Excel (zero-indexado)
    colunas = list(range(2, 12))  # C até L (coluna 2 até 11 no zero-indexado)

    df_excel.iloc[linha_inicio:linha_inicio+len(df_novos_dados), colunas] = df_novos_dados.values

    # 🔹 Salvar de volta no Excel
    df_excel.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")

    # REGEX manipulando strings
    dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True)
    # remover os hifens que não estejam conectando palavras compostas ***(?<!\w): uma "lookbehind" negativa que verifica se há um caractere de palavra antes do hífen ou se há apenas um espaço em branco, resultando em "verdadeiro" se não houver nada
    dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', '', regex=True)  #(?!\w): uma lookahead negativa que verifica se há um caractere de palavra depois do hífen.
    dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"','',regex=True)

    ''' CRIAR UM BANCO DE DADOS sqlite E ADD TABELA '''
    #  O COMANDO  reate_engine('sqlite:///:memory:') cria o banco de dados
    import sqlalchemy
    from sqlalchemy import create_engine, MetaData, Table, inspect
    engine = create_engine('sqlite:///:memory:')
    # ADD A TABELA NO BANCO DE DADOS:
    df.to_sql('clientes', engine, index=False)
    #  INSPECIONAR AS TABELAS NO BANCO DE DADOS
    inspector = inspect(engine)
    print(inspector.get_table_names())
    #  FILTRAR A TABELA COM SQL COM read_sql()
    query = 'SELECT * FROM clientes WHERE Categoria_de_renda="Empregado"'
    empregados = pd.read_sql(query, engine)
    #  SALVAR A TABELA FILTRADA COMO UMA NOVA TABELA NO BANCO DE DADOS
    empregados.to_sql('empregados', con=engine, index=False)
    #  PARA LER A TABELA DO BANCO DE DADOS
    pd.read_sql_table('empregados', engine)
    # LER A TABELA SELECIONANDO AS COLUNAS
    pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])
    '''read_sql é utilizado para executar uma consulta SQL e retornar os resultados dessa consulta. Ou seja, 
    você pode filtrar e selecionar apenas as informações que deseja.'''
    '''read_sql_table, por outro lado, é usado para ler uma tabela inteira do banco de dados. Com ele, você acessa todos os dados
      daquela tabela sem precisar fazer uma consulta específica.'''
    # ATUALIZANDO um banco de dados

    query = 'UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
    with engine.connect() as conn:
        conn.execute(query)
    pd.read_sql_table('clientes', engine)
except:
    pass
