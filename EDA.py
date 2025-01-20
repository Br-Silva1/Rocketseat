import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
file_path = '/mnt/data/netflix daily top 10.csv'
data = pd.read_csv(file_path)

# Visualizar e entender os dados
print(data.head())
print(data.dtypes)

# Tamanho do dataset
print(f"Tamanho do dataset: {data.shape[0]} linhas e {data.shape[1]} colunas")

# Período da análise
data['As of'] = pd.to_datetime(data['As of'], errors='coerce')
date_range = (data['As of'].min(), data['As of'].max())
print(f"Período da análise: {date_range[0]} a {date_range[1]}")

# Verificar dados nulos
null_values = data.isnull().sum()
print("Dados nulos por coluna:")
print(null_values)

# Análise estatística e outliers
# Estatísticas descritivas
print("Estatísticas - Dias no Top 10:")
print(data['Days In Top 10'].describe())
print("Estatísticas - Pontuação de audiência:")
print(data['Viewership Score'].describe())

# Visualização de outliers com boxplots
plt.figure(figsize=(10, 5))
plt.boxplot(data['Days In Top 10'], vert=False, patch_artist=True)
plt.title('Outliers: Days In Top 10')
plt.xlabel('Dias')
plt.show()

plt.figure(figsize=(10, 5))
plt.boxplot(data['Viewership Score'], vert=False, patch_artist=True)
plt.title('Outliers: Viewership Score')
plt.xlabel('Pontuação')
plt.show()
