from PyPDF2 import PdfReader

pdf = PdfReader('C:\\Users\\victo\\Desktop\\TESTES\\029 - COMO SE COMPORTAR EM UMA ENTREVISTA DE EMPREGO [PRETO E BRANCO].PDF')
texto = ""



linhas_a_pegar = 5  # número de linhas que quer pegar depois

for pagina in pdf.pages:
   linhas = pagina.extract_text().split('\n')
   
   for i, linha in enumerate(linhas):
       if linha.startswith("Deixe claro as razões"):  # substitua pelo seu critério
           print(f"Linha encontrada: {linha}")
           print("\nPróximas 5 linhas:")
           for j in range(1, linhas_a_pegar + 1):
               if i + j < len(linhas):
                   print(linhas[i + j])