from flask import Flask, render_template, Response
import io
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

# Dados simulados (você pode ler de um CSV como antes)
data = {
    "Data": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "Quantidade": [10, 15, 7],
    "Preço": [20.5, 30.0, 25.0],
    "Produto": ["Produto A", "Produto B", "Produto A"],
    "Cliente": ["Cliente 1", "Cliente 2", "Cliente 1"]
}
df = pd.DataFrame(data)

# Processar os dados
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.month
df['Valor Total'] = df['Quantidade'] * df['Preço']
vendas_por_mes = df.groupby('Mês')['Valor Total'].sum()

# Função para gerar gráfico
def gerar_grafico():
    plt.figure(figsize=(8, 5))
    plt.bar(vendas_por_mes.index, vendas_por_mes.values, color='blue')
    plt.title('Total de Vendas por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Valor Total')
    plt.tight_layout()

    # Salvar o gráfico como imagem em memória
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Voltar ao início do arquivo para leitura
    plt.close()
    return img

# Rota para exibir o gráfico
@app.route('/grafico')
def exibir_grafico():
    img = gerar_grafico()
    return Response(img, mimetype='image/png')

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
