import pandas as pd
from datetime import datetime, timedelta

class ControladorEstudos:
    def __init__(self):
        try:
            self.df = pd.read_excel('controle_estudos.xlsx')
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=[
                'Data', 'Matéria', 'Assunto', 'Tempo_Estudado_Min',
                'Questões_Resolvidas', 'Acertos', 'Nota_Compreensão',
                'Revisão_Necessária', 'Observações'
            ])
    
    def adicionar_sessao(self, materia, assunto, tempo_min, questoes, acertos, 
                        nota_compreensao, revisao=False, observacoes=""):
        """Adiciona uma nova sessão de estudos"""
        nova_sessao = {
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Matéria': materia,
            'Assunto': assunto,
            'Tempo_Estudado_Min': tempo_min,
            'Questões_Resolvidas': questoes,
            'Acertos': acertos,
            'Nota_Compreensão': nota_compreensao,
            'Revisão_Necessária': revisao,
            'Observações': observacoes
        }
        self.df = pd.concat([self.df, pd.DataFrame([nova_sessao])], ignore_index=True)
        self.salvar()
    
    def gerar_estatisticas(self):
        """Gera estatísticas dos estudos"""
        stats = {
            'Total_Horas_Estudadas': self.df['Tempo_Estudado_Min'].sum() / 60,
            'Media_Acertos': (self.df['Acertos'] / self.df['Questões_Resolvidas']).mean() * 100,
            'Materias_Mais_Estudadas': self.df['Matéria'].value_counts().head(),
            'Assuntos_Para_Revisar': self.df[self.df['Revisão_Necessária'] == True]['Assunto'].tolist()
        }
        return stats
    
    def gerar_relatorio_semanal(self):
        """Gera um relatório da última semana de estudos"""
        uma_semana_atras = datetime.now() - timedelta(days=7)
        self.df['Data'] = pd.to_datetime(self.df['Data'], format='%d/%m/%Y')
        df_semana = self.df[self.df['Data'] >= uma_semana_atras]
        
        relatorio = {
            'Horas_Semana': df_semana['Tempo_Estudado_Min'].sum() / 60,
            'Materias_Estudadas': df_semana['Matéria'].unique().tolist(),
            'Total_Questoes': df_semana['Questões_Resolvidas'].sum(),
            'Media_Acertos_Semana': (df_semana['Acertos'] / df_semana['Questões_Resolvidas']).mean() * 100
        }
        return relatorio
    
    def salvar(self):
        """Salva a planilha em um arquivo Excel"""
        self.df.to_excel('controle_estudos.xlsx', index=False)

# Exemplo de uso
if __name__ == "__main__":
    controlador = ControladorEstudos()
    
    # Adicionar uma sessão de estudos
    controlador.adicionar_sessao(
        materia="Matemática",
        assunto="Funções Quadráticas",
        tempo_min=120,
        questoes=20,
        acertos=15,
        nota_compreensao=8,
        revisao=False,
        observacoes="Foco em gráficos e vértices"
    )
    
    # Gerar e mostrar estatísticas
    stats = controlador.gerar_estatisticas()
    print("\nEstatísticas Gerais:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Gerar e mostrar relatório semanal
    relatorio = controlador.gerar_relatorio_semanal()
    print("\nRelatório Semanal:")
    for key, value in relatorio.items():
        print(f"{key}: {value}")
