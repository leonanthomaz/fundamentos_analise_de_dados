import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('vendas.csv')

# Exibir os primeiros registros
print("Dados originais:")
print(df)

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
