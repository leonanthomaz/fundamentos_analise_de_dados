import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, Response
import io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # Importando o NumPy
import calendar  # Para obter os nomes dos meses

app = Flask(__name__)

# Caminho para o arquivo CSV
arquivo_csv = 'vendas.csv'

# Carregar os dados do CSV
df = pd.read_csv(arquivo_csv)

# Processar os dados
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.month
df['Valor Total'] = df['Quantidade'] * df['Preço']

# Estatísticas adicionais
media_vendas = np.mean(df['Valor Total'])  # Média de vendas
desvio_padrao_vendas = np.std(df['Valor Total'])  # Desvio padrão de vendas
total_vendas = np.sum(df['Valor Total'])  # Total de vendas

# Vendas por mês
vendas_por_mes = df.groupby('Mês')['Valor Total'].sum()

# Vendas por produto
vendas_por_produto = df.groupby('Produto')['Valor Total'].sum()

# Vendas por cliente
vendas_por_cliente = df.groupby('Cliente')['Valor Total'].sum()

# Função para gerar gráfico de vendas por mês
def gerar_grafico_vendas_mes():
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot')  # Estilo do gráfico
    
    # Mudar os números dos meses para os nomes dos meses
    meses = [calendar.month_name[m] for m in vendas_por_mes.index]
    
    # Criação do gráfico de barras com os nomes dos meses
    plt.bar(meses, vendas_por_mes.values, color='blue')
    
    # Títulos e rótulos com fontes maiores e negrito
    plt.title('Total de Vendas por Mês', fontsize=16, fontweight='bold')
    plt.xlabel('Mês', fontsize=14, fontweight='bold')
    plt.ylabel('Valor Total (R$)', fontsize=14, fontweight='bold')
    
    # Ajustes finais no gráfico
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Função para gerar gráfico de vendas por produto
def gerar_grafico_vendas_produto():
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot')  # Estilo do gráfico
    
    # Criação do gráfico de barras por produto
    plt.bar(vendas_por_produto.index, vendas_por_produto.values, color='green')
    
    # Títulos e rótulos
    plt.title('Vendas por Produto', fontsize=16, fontweight='bold')
    plt.xlabel('Produto', fontsize=14, fontweight='bold')
    plt.ylabel('Valor Total (R$)', fontsize=14, fontweight='bold')
    
    # Ajustes finais no gráfico
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Função para gerar gráfico de vendas por cliente
def gerar_grafico_vendas_cliente():
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot')  # Estilo do gráfico
    
    # Criação do gráfico de barras por cliente
    plt.bar(vendas_por_cliente.index, vendas_por_cliente.values, color='orange')
    
    # Títulos e rótulos
    plt.title('Vendas por Cliente', fontsize=16, fontweight='bold')
    plt.xlabel('Cliente', fontsize=14, fontweight='bold')
    plt.ylabel('Valor Total (R$)', fontsize=14, fontweight='bold')
    
    # Ajustes finais no gráfico
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Função para gerar gráfico de distribuição (histograma) de vendas
def gerar_grafico_distribuicao_vendas():
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot')  # Estilo do gráfico
    
    # Criação do histograma de vendas
    plt.hist(df['Valor Total'], bins=10, color='purple', edgecolor='black')
    
    # Títulos e rótulos
    plt.title('Distribuição de Vendas', fontsize=16, fontweight='bold')
    plt.xlabel('Valor Total (R$)', fontsize=14, fontweight='bold')
    plt.ylabel('Frequência', fontsize=14, fontweight='bold')
    
    # Ajustes finais no gráfico
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Função para gerar gráfico de vendas acumuladas
def gerar_grafico_vendas_acumuladas():
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot')  # Estilo do gráfico
    
    # Criação do gráfico de vendas acumuladas por mês
    vendas_acumuladas = vendas_por_mes.cumsum()
    plt.plot(vendas_acumuladas.index, vendas_acumuladas.values, marker='o', color='red')
    
    # Títulos e rótulos
    plt.title('Vendas Acumuladas por Mês', fontsize=16, fontweight='bold')
    plt.xlabel('Mês', fontsize=14, fontweight='bold')
    plt.ylabel('Valor Total Acumulado (R$)', fontsize=14, fontweight='bold')
    
    # Ajustes finais no gráfico
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Rota para exibir o gráfico de vendas por mês
@app.route('/grafico_mes')
def exibir_grafico_mes():
    img = gerar_grafico_vendas_mes()
    return Response(img, mimetype='image/png')

# Rota para exibir o gráfico de vendas por produto
@app.route('/grafico_produto')
def exibir_grafico_produto():
    img = gerar_grafico_vendas_produto()
    return Response(img, mimetype='image/png')

# Rota para exibir o gráfico de vendas por cliente
@app.route('/grafico_cliente')
def exibir_grafico_cliente():
    img = gerar_grafico_vendas_cliente()
    return Response(img, mimetype='image/png')

# Rota para exibir o gráfico de distribuição de vendas
@app.route('/grafico_distribuicao')
def exibir_grafico_distribuicao():
    img = gerar_grafico_distribuicao_vendas()
    return Response(img, mimetype='image/png')

# Rota para exibir o gráfico de vendas acumuladas
@app.route('/grafico_acumulado')
def exibir_grafico_acumulado():
    img = gerar_grafico_vendas_acumuladas()
    return Response(img, mimetype='image/png')

# Rota principal
@app.route('/')
def home():
    return render_template('index.html', media_vendas=media_vendas, desvio_padrao_vendas=desvio_padrao_vendas, total_vendas=total_vendas)

if __name__ == '__main__':
    app.run(debug=True)
