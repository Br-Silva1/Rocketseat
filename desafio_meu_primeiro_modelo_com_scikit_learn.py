import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de vendas
dados_vendas = {
    'mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'vendas': [2000, 2200, 2300, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300]
}

# Tratar e formatar os dados
df = pd.DataFrame(dados_vendas)
df['mes_num'] = range(1, 13)  # Adicionando o número do mês para facilitar o treinamento

# Treinar o modelo
X = df[['mes_num']]  # Variável independente (número do mês)
y = df['vendas']  # Variável dependente (vendas)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever as vendas para dezembro
venda_dezembro = modelo.predict([[12]])[0]
print(f"Previsão de vendas para dezembro: {venda_dezembro:.2f}")

# Montar o histograma dos dados
plt.figure(figsize=(8, 5))
plt.hist(df['vendas'], bins=6, color='skyblue', edgecolor='black')
plt.title('Histograma das Vendas')
plt.xlabel('Vendas')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Montar um plot de scatter
plt.figure(figsize=(8, 5))
plt.scatter(df['mes_num'], df['vendas'], color='blue', label='Dados Reais')
plt.plot(df['mes_num'], modelo.predict(X), color='red', linestyle='--', label='Linha de Regressão')
plt.title('Scatter Plot com Regressão Linear')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.legend()
plt.grid(alpha=0.5)
plt.show()
