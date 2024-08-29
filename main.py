import yfinance as yf
import pytz
import pandas as pd

# Definir o fuso horário de Brasília
brasilia_tz = pytz.timezone('Etc/GMT-3')

# Exemplo: Obter dados do Banco Santander
santander = yf.Ticker("SAN.MC")
hist = santander.history(period="5y")

# Converter o índice para timezone-aware no fuso horário de Brasília
hist.index = hist.index.tz_convert(brasilia_tz)

# Definir os timestamps iniciais e finais no fuso horário de Brasília
date_time_inicial = pd.Timestamp('2020-01-06', tz=brasilia_tz)
date_time_final = pd.Timestamp('2020-12-31T12', tz=brasilia_tz)

# Iterar sobre o dataframe
for index, row in hist.iterrows():
    if date_time_inicial < index < date_time_final:
        print(row)

# Adicionar coluna de variação diária
hist['Daily Change (%)'] = (hist['Close'] - hist['Open']) / hist['Open'] * 100

# Exibir análise diária para um intervalo específico
daily_analysis = hist.loc[date_time_inicial:date_time_final]
print(daily_analysis[['Open', 'Close', 'Daily Change (%)', 'Volume']])


# Resample para semanal e calcular variações e volumes
weekly_analysis = hist.resample('W').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação semanal
weekly_analysis['Weekly Change (%)'] = (weekly_analysis['Close'] - weekly_analysis['Open']) / weekly_analysis['Open'] * 100

print(weekly_analysis[['Open', 'Close', 'Weekly Change (%)', 'Volume']])


# Resample para mensal e calcular variações e volumes
monthly_analysis = hist.resample('M').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação mensal
monthly_analysis['Monthly Change (%)'] = (monthly_analysis['Close'] - monthly_analysis['Open']) / monthly_analysis['Open'] * 100
print(monthly_analysis[['Open', 'Close', 'Monthly Change (%)', 'Volume']])


# Resample para anual e calcular variações e volumes
annual_analysis = hist.resample('A').agg({
    'Open': 'first',
    'Close': 'last',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})

# Calcular variação anual
annual_analysis['Yearly Change (%)'] = (annual_analysis['Close'] - annual_analysis['Open']) / annual_analysis['Open'] * 100

print(annual_analysis[['Open', 'Close', 'Yearly Change (%)', 'Volume']])



