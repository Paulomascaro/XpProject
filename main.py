import yfinance as yf
import pytz  #trabalha com date
import pandas as pd

from analise_diaria import analise_diaria, validar_data
from analise_mensal import analise_mensal
from analise_semanal import analise_semanal

# Definir o fuso horário de Brasília
brasilia_tz = pytz.timezone('Etc/GMT-3')

# Exemplo: Obter dados do Banco Santander
santander = yf.Ticker("SAN.MC")
hist = santander.history(period="5y")

# Converter o índice para timezone-aware no fuso horário de Brasília
hist.index = hist.index.tz_convert(brasilia_tz)

# Definir os timestamps iniciais e finais no fuso horário de Brasília
date_time_inicial = pd.Timestamp('2019-01-01', tz=brasilia_tz)
date_time_final = pd.Timestamp('2024-08-30T12', tz=brasilia_tz)

# # Iterar sobre o dataframe
# for index, row in hist.iterrows():
#     if date_time_inicial < index < date_time_final:
#         print(row)

# Adicionar coluna de variação diária
hist['Daily Change (%)'] = (hist['Close'] - hist['Open']) / hist['Open'] * 100

# Exibir análise diária para um intervalo específico
hist_diario = hist.loc[date_time_inicial:date_time_final]
# print(hist_diario[['Open', 'Close', 'Daily Change (%)', 'Volume']])


# Resample para semanal e calcular variações e volumes
hist_semanal = hist.resample('W').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação semanal
hist_semanal['Weekly Change (%)'] = (hist_semanal['Close'] - hist_semanal['Open']) / hist_semanal['Open'] * 100

# print(hist_semanal[['Open', 'Close', 'Weekly Change (%)', 'Volume']])


# Resample para mensal e calcular variações e volumes
hist_mensal = hist.resample('M').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação mensal
hist_mensal['Monthly Change (%)'] = (hist_mensal['Close'] - hist_mensal['Open']) / hist_mensal['Open'] * 100
# print(hist_mensal[['Open', 'Close', 'Monthly Change (%)', 'Volume']])


# Resample para anual e calcular variações e volumes
hist_anual = hist.resample('A').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação anual
hist_anual['Yearly Change (%)'] = (hist_anual['Close'] - hist_anual['Open']) / hist_anual['Open'] * 100
# print(hist_anual[['Open', 'Close', 'Yearly Change (%)', 'Volume']])

op = -1
while op != 0:
    print("####### MENU #######\n")
    op = int(input("Digite a opção desejada: \n"
             "1 - Analise Diaria: \n"
             "2 - Analise Semanal: \n"
             "3 - Analise Mensal: \n"
             "0 - Sair\n"))
    
    if op == 0:
        break
    
    data_inicio = input('Digite a data de início (YYYY-MM-DD): ')
    data_fim = input('Digite a data de fim (YYYY-MM-DD): ')
    if not (validar_data(data_inicio) and validar_data(data_fim)):
        print("Data inválida. Por favor, use o formato YYYY-MM-DD.")

    if data_inicio > data_fim:
        print("A data de início não pode ser posterior à data de fim.")

    if op == 1:
        analise_diaria(data_inicio, data_fim)

    if op == 2:
        analise_semanal(data_inicio, data_fim)

    if op == 3:
        analise_mensal(data_inicio, data_fim)


