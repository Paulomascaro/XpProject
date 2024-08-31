import re
import pandas as pd
from sqlalchemy import create_engine

# Função para validar a data com regex
def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(padrao, data) is not None

# Função para calcular a proporção de dias bons em relação ao total de dias
def analise_semanal(data_inicio, data_fim):
    # Configurar a conexão com o banco de dados MySQL
    engine = create_engine('mysql+pymysql://root:santos2501@localhost/dbXp')

    try:
        # Consultar o hist_diario no banco de dados para o intervalo de datas especificado
        query = f"""
        SELECT * FROM hist_semanal 
        WHERE `Date` >= '{data_inicio}' AND `Date` <= '{data_fim}';
        """
        print(f"Executando consulta: {query}")  # Impressão para depuração
        hist_semanal = pd.read_sql(query, con=engine, index_col='Date')

        # Verificar e imprimir o DataFrame carregado
        print("Dados carregados do banco de dados:")
        print(hist_semanal.head())  # Imprimir as primeiras linhas para verificar os dados

        # Verificar se o DataFrame contém dados
        if hist_semanal.empty:
            print("Nenhum dado encontrado para o intervalo especificado.")
            return

        # Filtrar dias bons (variação diária positiva)
        dias_bons = hist_semanal[hist_semanal['Weekly Change (%)'] > 0].shape[0]
        total_dias = hist_semanal.shape[0]

        # Verificar e imprimir a contagem de dias bons e total de dias
        print(f"Total de dias no intervalo: {total_dias}")
        print(f"Dias bons (variação positiva): {dias_bons}")

        # Calcular e imprimir a proporção de dias bons
        proporcao_dias_bons = dias_bons / total_dias if total_dias > 0 else 0
        print(f"Proporção de dias bons entre {data_inicio} e {data_fim}: {proporcao_dias_bons:.2%}")

    finally:
        # Garantir que a conexão com o banco de dados seja fechada
        engine.dispose()