def calcular_juros_compostos(aporte_mensal, taxa_anual, periodo_meses, imposto_renda):
    """
    Calcula juros compostos com aportes mensais e desconto de imposto de renda
    
    Parâmetros:
    aporte_mensal: valor do aporte mensal
    taxa_anual: taxa de juros anual em porcentagem
    periodo_meses: período total em meses
    imposto_renda: percentual de imposto de renda
    
    Retorna: lista com os valores mensais acumulados e total de imposto
    """
    
    # Converter taxa anual para mensal
    taxa_mensal = (1 + taxa_anual/100) ** (1/12) - 1
    
    # Lista para armazenar o valor acumulado em cada mês
    valores_mensais = []
    
    # Valor inicial
    montante = 0
    montante_antes_ir = 0
    imposto_total = 0
    
    # Calcular para cada mês
    for mes in range(1, periodo_meses + 1):
        montante_anterior = montante
        
        # Adiciona o aporte mensal
        montante += aporte_mensal
        
        # Aplica o juros mensal
        montante *= (1 + taxa_mensal)
        
        # Calcula o lucro do mês
        lucro_mes = montante - montante_anterior - aporte_mensal
        
        # Calcula e deduz o imposto sobre o lucro
        imposto_mes = lucro_mes * (imposto_renda/100)
        montante -= imposto_mes
        imposto_total += imposto_mes
        
        # Armazena o valor do mês
        valores_mensais.append(round(montante, 2))
        
        print(f"Mês {mes}:")
        print(f"Montante: R$ {montante:,.2f}")
        print(f"Imposto pago no mês: R$ {imposto_mes:,.2f}\n")
    
    return valores_mensais, imposto_total

# Execução do programa
aporte = 1200      # R$ por mês
taxa = 12          # 12% ao ano
meses = 12*8        # período de 12 meses
imposto = 19       # 17% de IR

print("\nSimulação de investimento:")
print(f"Aporte mensal: R$ {aporte:,.2f}")
print(f"Taxa de juros: {taxa}% ao ano")
print(f"Período: {meses} meses")
print(f"Imposto de Renda: {imposto}%\n")

resultados, imposto_total = calcular_juros_compostos(aporte, taxa, meses, imposto)

# Cálculo do total investido e juros ganhos
total_investido = aporte * meses
juros_ganhos = resultados[-1] - total_investido

print(f"\nResultados finais:")
print(f"Total investido: R$ {total_investido:,.2f}")
print(f"Montante final: R$ {resultados[-1]:,.2f}")
print(f"Juros ganhos (líquido): R$ {juros_ganhos:,.2f}")
print(f"Total de imposto pago: R$ {imposto_total:,.2f}")
print(f"Juros ganhos (bruto): R$ {juros_ganhos + imposto_total:,.2f}")