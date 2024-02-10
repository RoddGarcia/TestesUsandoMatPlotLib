import matplotlib.pyplot as plt
import pandas as pd

# Importar os dados do arquivo CSV
leitura_excel = pd.read_csv("Bank_Stock_Price_10Y.csv")

# Converter a coluna 'Date' para o formato datetime
leitura_excel['Date'] = pd.to_datetime(leitura_excel["Date"])

# Filtrar o DataFrame para mostrar apenas datas após 2018-01-01
data_filtrada = leitura_excel[leitura_excel["Date"] > '2018-01-01']

# Extrair as colunas necessárias
dates = data_filtrada['Date']
high_prices = data_filtrada['High']
low_prices = data_filtrada['Low']
close_prices = data_filtrada['Close']

# Criar o gráfico
plt.figure(figsize=(10, 6))

# Preencher a área entre os preços 'High' e 'Low' com uma cor cinza claro
plt.fill_between(dates, high_prices, low_prices, color='lightgray', label='Intervalo Alto-Baixo')

# Plotar os preços de fechamento
plt.plot(dates, close_prices, color='blue', label='Preço de Fechamento')

# Personalizar o gráfico
plt.title('Fictional Bank Stocks Between 2018-2024')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
