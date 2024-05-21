# gasolina.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura dos dados
df = pd.read_csv('gasolina.csv')

# Criação do gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')
plt.title('Preço Médio da Gasolina em São Paulo - Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.savefig('gasolina.png')
plt.show()
