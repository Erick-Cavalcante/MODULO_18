  # gasolina.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
  # Leitura dos dados
df = pd.read_csv('gasolina.csv')
  
  # Criação do gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')
plt.title('média do preço da Gasolina em São Paulo - Julho de 2021')
plt.xlabel('Day')
plt.ylabel('gasoline price')
plt.grid(True)
plt.savefig('gasoline.png')
