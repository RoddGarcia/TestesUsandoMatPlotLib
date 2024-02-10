import matplotlib.pyplot as plt
import pandas as pd

leitura_excel = pd.read_csv("Bank_Stock_Price_10Y.csv")

leitura_excel['Date'] = pd.to_datetime(leitura_excel["Date"])

data_filtrada =leitura_excel[leitura_excel["Date"]> '2018-01-01']


plt.figure(figsize=(10, 6))
plt.plot(data_filtrada['Date'], data_filtrada['Adj Close'], marker='.', linestyle=':', label="Adj Close", color="blue")
plt.title('Fictional Bank Adj. Close 2018-2024')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()