import pandas as pd
import numpy as np

# Ler o arquivo CSV
df = pd.read_csv('vendas.csv')

# Exibir os primeiros registros
print("Dados originais:")
print(df.head())

# Adicionar uma coluna de valor total (Quantidade x Preço)
df['Valor Total'] = df['Quantidade'] * df['Preço']

# Total de vendas por mês
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.month
vendas_por_mes = df.groupby('Mês')['Valor Total'].sum()
print("\nTotal de vendas por mês:")
print(vendas_por_mes)

# Produto mais vendido
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print(f"\nProduto mais vendido: {produto_mais_vendido}")

# Cliente com maior gasto
cliente_top = df.groupby('Cliente')['Valor Total'].sum().idxmax()
print(f"\nCliente com maior gasto: {cliente_top}")

# Adicionar estatísticas usando NumPy
print("\nEstatísticas adicionais usando NumPy:")

# Média de vendas por produto
media_vendas_produto = df.groupby('Produto')['Valor Total'].mean()
print("\nMédia de vendas por produto:")
print(media_vendas_produto)

# Desvio padrão das vendas por produto
desvio_padrao_vendas_produto = df.groupby('Produto')['Valor Total'].std(ddof=0)
print("\nDesvio padrão das vendas por produto:")
print(desvio_padrao_vendas_produto)

# Mediana das vendas por mês
mediana_vendas_mes = df.groupby('Mês')['Valor Total'].median()
print("\nMediana das vendas por mês:")
print(mediana_vendas_mes)

# Usando NumPy para cálculos diretos
total_vendas = np.sum(df['Valor Total'])
media_geral_vendas = np.mean(df['Valor Total'])
desvio_padrao_geral_vendas = np.std(df['Valor Total'])

print(f"\nTotal geral de vendas: {total_vendas:.2f}")
print(f"Média geral de vendas: {media_geral_vendas:.2f}")
print(f"Desvio padrão geral de vendas: {desvio_padrao_geral_vendas:.2f}")
