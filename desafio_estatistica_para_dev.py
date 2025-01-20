import pandas as pd
import matplotlib.pyplot as plt

dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
    ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
    ]
}

df = pd.DataFrame(dict_faturamento)

df['data_ref'] = pd.to_datetime(df['data_ref'])

# Média das vendas
media_vendas = df['valor'].mean()
print(f"Média das vendas: R${media_vendas:.2f}")

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['data_ref'].dt.strftime('%Y-%m'), df['valor'], color='skyblue')
plt.title('Faturamento Mensal - Gráfico de Barras')
plt.xlabel('Mês de Referência')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(df['data_ref'].dt.strftime('%Y-%m'), df['valor'], marker='o', color='green', linestyle='-')
plt.title('Faturamento Mensal - Gráfico de Linhas')
plt.xlabel('Mês de Referência')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
