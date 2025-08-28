# Fundamentos de Análise de Dados

Projeto em **Python e Flask** para análise de dados de vendas, utilizando **pandas**, **NumPy** e **matplotlib**. Permite visualizar métricas de vendas por mês, produto e cliente, com gráficos interativos via web.

---

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- `.gitignore` – arquivos e pastas ignorados pelo Git  
- `app.py` – aplicação Flask principal  
- `vendas.csv` – dados de vendas  
- `_mathplot.py`, `_mathplot_web.py` – scripts de visualização  
- `_numpy.py`, `_pandas.py` – scripts de análise de dados  
- `LICENSE` – licença do projeto  
- `README.md` – este arquivo  
- `requirements.txt` – dependências do projeto  
- `templates/index.html` – template HTML da interface web  

---

## Tecnologias Utilizadas

- Python – Linguagem principal do projeto  
- Flask – Framework web para criação de interface e rotas  
- pandas – Manipulação e análise de dados  
- NumPy – Cálculos estatísticos e matemáticos  
- matplotlib – Geração de gráficos  
- HTML – Interface web básica  

---

## Funcionalidades

- Carregar e processar dados de um arquivo CSV  
- Calcular estatísticas básicas (média, desvio padrão, total de vendas)  
- Gerar gráficos:  
  - Total de vendas por mês  
  - Vendas por produto  
  - Vendas por cliente  
  - Distribuição de vendas (histograma)  
  - Vendas acumuladas  
- Exibir gráficos via interface web em Flask  

---

## Como Instalar

1. Clone o repositório: 

```
git clone <URL_DO_REPOSITORIO>
cd fundamentos_analise_de_dados

```

2. Crie um ambiente virtual (opcional, mas recomendado):  

```
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux / Mac

```

3. Instale as dependências:  

```
pip install -r requirements.txt

```

4. Execute a aplicação Flask:  

```
python app.py

```

5. Acesse no navegador:  

```
http://127.0.0.1:5000

```

---

## Estatísticas e Análises Incluídas

- Média, desvio padrão e total de vendas gerais  
- Total de vendas por mês  
- Produto mais vendido  
- Cliente com maior gasto  
- Gráficos de distribuição e vendas acumuladas  

---

## Licença

Este projeto está sob a **MIT License** – veja `LICENSE` para detalhes.
