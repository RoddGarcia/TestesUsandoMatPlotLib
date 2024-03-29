# Matplotlib e sua Importância na Análise de Dados

## O que é Matplotlib?

Matplotlib é uma biblioteca em Python utilizada para criar visualizações de dados, como gráficos, histogramas, gráficos de barras, dispersão, entre outros. Ela oferece uma ampla variedade de opções para customização dos gráficos, permitindo aos usuários criar visualizações atraentes e informativas.

## Importância na Análise de Dados

A visualização de dados desempenha um papel crucial na análise de dados, pois permite que os analistas comuniquem informações de forma clara e eficaz. Matplotlib é uma ferramenta essencial para análise de dados por várias razões:

1. **Comunicação Visual:** Gráficos bem construídos tornam a interpretação dos dados mais intuitiva e acessível para uma ampla audiência.

2. **Exploração de Dados:** Antes de realizar análises mais avançadas, é útil visualizar os dados de maneira rápida e interativa, o que pode ser facilmente feito com Matplotlib.

3. **Identificação de Padrões e Tendências:** Gráficos permitem identificar padrões, tendências e anomalias nos dados, ajudando na tomada de decisões informadas.

4. **Validação de Modelos:** Ao visualizar os resultados de modelos estatísticos ou de aprendizado de máquina, é possível validar se os modelos estão se comportando conforme o esperado.

5. **Relatórios e Apresentações:** Gráficos criados com Matplotlib podem ser incorporados em relatórios ou apresentações para comunicar resultados de análises de dados de forma clara e impactante.

## Explicação dos Códigos

### highlow.py

```python
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
```

Neste código, é criado um gráfico que mostra o intervalo de preços alto-baixo ('High' e 'Low') preenchido com uma cor cinza claro e o preço de fechamento ('Close') plotado em azul ao longo do tempo.

![image](https://github.com/RoddGarcia/TestesUsandoMatPlotLib/assets/85592905/1c596188-0540-441c-8ab8-5a0e002e9e96)

![image](https://github.com/RoddGarcia/TestesUsandoMatPlotLib/assets/85592905/f759baeb-4dd9-469b-8049-b9f76b0bf8f3)

### adjClose.py

```python
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
```

Neste código, é criado um gráfico que mostra os preços de fechamento ajustados ('Adj Close') ao longo do tempo para datas após 2018-01-01. Os preços de fechamento ajustados são plotados em azul com marcadores e linha pontilhada.

![image](https://github.com/RoddGarcia/TestesUsandoMatPlotLib/assets/85592905/6c32774d-d642-47b1-b38d-ba11c1c7cefa)
