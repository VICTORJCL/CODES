import pandas as pd
import os
import openpyxl as op

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# cami='C:\CODES\PYTHON for all\PANDAS\Desafio_Brasilmad\início pandas'.replace('\\','/')
# os.chdir(cami)
caminho_arquivo='TesteBrasilmadVBA.xlsx'
# openpyxl
wb=op.load_workbook('TesteBrasilmadVBA.xlsx')
# pandas
db=pd.read_excel('TesteBrasilmadVBA.xlsx', sheet_name=None)

# selecionar sheets pd
sheets_pandas_planílhas=list(db.keys())
print(sheets_pandas_planílhas)
db_sheet0=db[sheets_pandas_planílhas[0]]
db_sheet1=db[sheets_pandas_planílhas[1]]
db_sheet2=db[sheets_pandas_planílhas[2]]
print(type(db_sheet1))

# selecionar sheets openpyxl
sheets_wb=wb.sheetnames
sheet0_wb_openpy= wb[sheets_wb[0]]

'''variáveis busca filtro'''
DataNF_inicial_filtro=sheet0_wb_openpy['C18'].value
DataNF_final_filtro=sheet0_wb_openpy['E18'].value
NumNF_filtro=sheet0_wb_openpy['C19'].value
sit_filtro=sheet0_wb_openpy['C20'].value
Nome_do_Fornecedor_filtro=sheet0_wb_openpy['C21'].value

type(NumNF_filtro)
type(sit_filtro)

# print(db_sheet2.head(20))
# tratando dados planílhas SHEET2
col=db_sheet1.columns = db_sheet1.iloc[4].values
db_sheet1=db_sheet1.iloc[5:].reset_index(drop=True)
# print(col)
# print(db_sheet1)

col=db_sheet2.columns=db_sheet2.iloc[3].values
db_sheet2=db_sheet2.iloc[7:].reset_index(drop=True)

''' drop valores vazios de todas as linhas da coluna'''
db_sheet2=db_sheet2.dropna(axis=1, how='all')
# db_sheet2=db_sheet2 = db_sheet2.drop(columns=db_sheet2.columns[0])


db_sheet0
db_sheet1
db_sheet2





df_filtrado = db_sheet2
'''tabela de print
startrow=17 corresponde à linha 18 (pois começa em 0)
startcol=7 corresponde à coluna H (pois começa em 0)
header=False para não incluir os nomes das colunas do DataFrame
index=False para não incluir o índice do DataFrame
'''

# Criar um objeto ExcelWriter usando o arquivo existente
writer = pd.ExcelWriter(caminho_arquivo, engine='openpyxl')
writer.book = wb
# Escrever o DataFrame na posição específica (H18)
df_filtrado.to_excel(writer, sheet_name='TesteBrasilmadVBA.xlsx', startrow=17, startcol=7, 
                    header=False, index=False)
