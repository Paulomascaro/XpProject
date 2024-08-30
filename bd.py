from sqlalchemy import create_engine
from main import hist_diario, hist_semanal, hist_mensal, hist_anual


# Configurar a conexão com o banco de dados MySQL
engine = create_engine('mysql+pymysql://root:santos2501@localhost/dbXp')

# Armazenar os dados no MySQL
hist_diario.to_sql('hist_diario', con=engine, if_exists='replace', index=True)
hist_semanal.to_sql('hist_semanal', con=engine, if_exists='replace', index=True)
hist_mensal.to_sql('hist_mensal', con=engine, if_exists='replace', index=True)
hist_anual.to_sql('hist_anual', con=engine, if_exists='replace', index=True)
