import yfinance as yf
import pytz
import pandas as pd

# Definir o fuso horário de Brasília
brasilia_tz = pytz.timezone('Etc/GMT-3')

# Configurar a localização do cache para o fuso horário de Brasília
yf.set_tz_cache_location(brasilia_tz)

# Exemplo: Obter dados do Banco Santander
santander = yf.Ticker("SAN.MC")
hist = santander.history(period="5y")

# Converter o índice para timezone-aware no fuso horário de Brasília
hist.index = hist.index.tz_convert(brasilia_tz)

# Definir os timestamps iniciais e finais no fuso horário de Brasília
date_time_inicial = pd.Timestamp('2020-01-06', tz=brasilia_tz)
date_time_final = pd.Timestamp('2020-01-10T12', tz=brasilia_tz)

# Iterar sobre o dataframe
for index, row in hist.iterrows():
    if date_time_inicial < index < date_time_final:
        print(row)



  # hist[date_time_inicial].open
# hist[date_time_final].close
# hist[


