# 📊 Aprendendo a Visualizar Dados com Python

<p align="center">
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="Status">
</p>

Este repositório foi criado para documentar minha jornada de aprendizado em ciência de dados, focando na coleta, limpeza, tratamento e visualização de dados utilizando a linguagem Python.

---

## 📂 Estrutura do Projeto

O projeto está organizado com scripts de automação de dados e arquivos de armazenamento (CSV):

### 🐍 Scripts Python (`.py`)
* **`coletabasica.py`** / **`coletadado_api.py`** / **`coletadados_web.py`**: Scripts focados na captura e extração de dados de diferentes fontes e APIs.
* **`scrapingbooks_site.py`**: Web scraping estruturado para coleta de dados de páginas web.
* **`gerar_dados.py`**: Criação de datasets sintéticos para simulações de análise.
* **`inconsistencias.py`** / **`limpeza_dados.py`**: Identificação de falhas estruturais, dados nulos e preparação das bases.
* **`outliers.py`**: Detecção e tratamento de anomalias estatísticas nos dados coletados.
* **`tratamento_dados_basico.py`** / **`estudo_dataframe.py`**: Manipulação de dados com foco em estruturas do Pandas DataFrames.

### 💾 Bases de Dados (`.csv`)
* **`clientes.csv`**: Dados brutos iniciais coletados.
* **`clientes_limpos.csv`**: Base de clientes tratada, sem valores nulos ou duplicados.
* **`clientes_remove_outliers.csv`**: Dados finais prontos para análise estatística e visualização.
* **`dados_pessoas.csv`**: Dataset complementar utilizado nos estudos.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

Abaixo estão listadas as ferramentas fundamentais que pretendo explorar ou que já utilizo neste ecossistema:

* **[Python](https://python.org)** — Linguagem base do projeto.
* **[Pandas](https://pydata.org)** — Manipulação e análise de dados estruturados.
* **[NumPy](https://numpy.org)** — Computação matemática e tratamento de matrizes.
* **[Matplotlib](https://matplotlib.org)** / **[Seaborn](https://pydata.org)** — Criação de gráficos estáticos, informativos e estatísticos.
* **[Requests](https://readthedocs.io)** / **[BeautifulSoup4](https://crummy.com)** — Consumo de APIs e raspagem de dados web.

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd visualizacaoDados
```

### 2. Criar e Ativar Ambiente Virtual (Recomendado)
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Windows (Git Bash)
source venv/Scripts/activate
```

### 3. Instalar Dependências Básicas
```bash
pip install pandas numpy matplotlib seaborn requests beautifulsoup4
```

---

## ✒️ Autora

* **Yara** — [@yarxcat](https://github.com/yarxcat)