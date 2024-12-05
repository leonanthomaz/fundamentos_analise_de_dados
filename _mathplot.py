import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('vendas.csv')

# Processar os dados
df['Valor Total'] = df['Quantidade'] * df['Preço']
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.month

# Total de vendas por mês
vendas_por_mes = df.groupby('Mês')['Valor Total'].sum()

# Produtos mais vendidos
vendas_por_produto = df.groupby('Produto')['Quantidade'].sum()

# Clientes com maiores gastos
gastos_por_cliente = df.groupby('Cliente')['Valor Total'].sum()

# ----- VISUALIZAÇÕES -----

def plot_vendas_por_mes(vendas_por_mes):
    plt.figure(figsize=(8, 5))
    vendas_por_mes.plot(kind='bar', color='skyblue')
    plt.title('Total de Vendas por Mês', fontsize=14)
    plt.xlabel('Mês', fontsize=12)
    plt.ylabel('Valor Total (R$)', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_vendas_por_produto(vendas_por_produto):
    plt.figure(figsize=(8, 5))
    vendas_por_produto.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Distribuição de Vendas por Produto', fontsize=14)
    plt.ylabel('')  # Remover label automático do eixo Y
    plt.show()

def plot_gastos_por_cliente(gastos_por_cliente):
    plt.figure(figsize=(10, 6))
    gastos_por_cliente.sort_values(ascending=False).plot(kind='bar', color='salmon')
    plt.title('Gastos Totais por Cliente', fontsize=14)
    plt.xlabel('Cliente', fontsize=12)
    plt.ylabel('Valor Total (R$)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# ----- CHAMAR FUNÇÕES DE PLOTAGEM -----
plot_vendas_por_mes(vendas_por_mes)
plot_vendas_por_produto(vendas_por_produto)
plot_gastos_por_cliente(gastos_por_cliente)
