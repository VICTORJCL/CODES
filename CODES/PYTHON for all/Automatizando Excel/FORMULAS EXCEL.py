import os
os.chdir('C:/PYTHON for All/Automatizando Excel/')
from openpyxl import Workbook
wb=Workbook()
# cria uma instância com wb.active DE UM ARQUIVO AINDA NÃO EXISTENTE
sheet= wb.active

sheet['A1'].value=100
sheet['A2'].value=400
#  cria a fórmula exata
sheet['A3'].value="=SUM(A1:A2)"

minha_formula="=SUM(A1:A2)"
# copia uma fórmula e aplica nas outras células
from openpyxl.formula.translate import Translator
sheet["B1"].value=300
sheet["B2"].value=500
sheet["B3"] = Translator(minha_formula, origin="A3").translate_formula("B3")



wb.save("formula.xlsx")

# VERIFICA TODAS AS FÓRMULAS DE EXCEL
from openpyxl.utils import FORMULAE
print(FORMULAE)
