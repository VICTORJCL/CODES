# Obtém o diretório do arquivo atual
import os
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)



#  função para ativar por tempo em minutos
import time
from datetime import datetime, timedelta
def loop_por_tempo():
    # Define o tempo de término (10 minutos a partir de agora)
    tempo_final = datetime.now() + timedelta(minutes=10)
    
    try:
        while datetime.now() < tempo_final:
            #o código vai aqui
            print("Executando...")  # Exemplo
            # Opcional: adicione um pequeno delay para não sobrecarregar o CPU
            time.sleep(1)  # Espera 1 segundo entre execuções .
            
        print("Loop finalizado após 10 minutos!")
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário")


loop_por_tempo()