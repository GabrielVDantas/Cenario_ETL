import pandas as pd

# Extraindo dados do csv:
vendas_csv = pd.read_csv('ETL_csv.csv')

# Valor total das vendas de cada produto:
vendas_csv['Valor TOTAL'] = vendas_csv['Quantidade Vendida'] * vendas_csv['Preço Unitário']

# Visualizando dados:
print('DADOS EM CSV DA FILIAL:')
print(vendas_csv.head())

# Extraindo dados do xlsx:
vendas_xlsx = pd.read_excel('ETL_xlsx.xlsx')

# Valor total das vendas de cada produto:
vendas_xlsx['Valor TOTAL'] = vendas_xlsx['Quantidade Vendida'] * vendas_xlsx['Preço Unitário']

# Visualizando dados:
print('DADOS EM XLSX DA FILIAL:')
print(vendas_xlsx.head())

import sqlite3

conn = sqlite3.connect('banco_de_dados.db')

# Inserindo os dados no SQLite:
vendas_csv.to_sql('vendas_csv', conn, if_exists='replace', index=False)
vendas_xlsx.to_sql('vendas_xlsx', conn, if_exists='replace', index=False)

conn.close()