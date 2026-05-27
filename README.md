# 📊 Análise Exploratória e Regressão: Índices de Homicídios Globais (UNODC)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Data_App-FF4B4B.svg)](https://streamlit.io/)

Este repositório contém o projeto prático desenvolvido para a disciplina de **ECO0063 – Tópicos Especiais em Computação I** do curso de Engenharia de Computação da Universidade Federal do Ceará (UFC) - Campus Sobral, sob orientação do Prof. Iális Cavalcante.

## 🎯 Objetivo do Projeto

O trabalho utiliza a base de dados pública do **Escritório das Nações Unidas sobre Drogas e Crime (UNODC)** para mapear e entender os cenários de violência global. O escopo do projeto está apoiado em três pilares:

1. **Análise Exploratória de Dados (EDA):** Extração de _insights_ e estatísticas através do Pandas para responder a 10 questionamentos específicos.
2. **Modelo Preditivo:** Implementação de um algoritmo de Regressão Linear para projetar as taxas de homicídios nos anos seguintes (2023 a 2026).
3. **Data App:** Construção de um painel interativo (dashboard) apresentando as projeções do modelo.

---

## 🔍 Perguntas Respondidas na Análise

Durante a etapa de EDA, o notebook soluciona as seguintes questões de negócio e demografia:

1. Quais países apresentam os 10 maiores índices de homicídios nos últimos 5 anos?
2. Quais países apresentam os 10 maiores índices de homicídios de mulheres em 2022?
3. Quais as regiões com mais homicídios?
4. Quais países têm o menor número de homicídios em cada sub-região?
5. Quais países têm o menor número de morte de mulheres?
6. Quais as sub-regiões com maior número de homicídios?
7. Qual o país com maior número de homicídios em cada continente no ano isolado de 2020?
8. Qual o país mais violento para as mulheres em 2021?
9. Qual o país com o maior valor histórico acumulado do indicador 'Victims of intentional homicide'?
10. Qual a média de homicídios no Brasil nos últimos 10 anos?

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando o seguinte ecossistema de dados em Python:

- **[Jupyter Notebook / Google Colab](https://colab.research.google.com/):** Ambiente de desenvolvimento e documentação da análise.
- **[Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/):** Tratamento, limpeza, agrupamento e manipulação dos dados.
- **[Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/):** Visualização de dados e geração de gráficos estatísticos.
- **[Scikit-Learn](https://scikit-learn.org/):** Criação e treinamento do modelo de Regressão.
- **[Streamlit](https://streamlit.io/):** Criação e deploy do Data App interativo.

---

## 🚀 Como Executar o Data App Localmente

Siga os passos abaixo para clonar o repositório, instalar as dependências e rodar a aplicação em sua máquina.

### 1. Clonar o Repositório

Abra o terminal do seu computador e execute os comandos:

```bash
git clone https://github.com/priscilaaquila/analise-exploratoria-regressao-indice-homicidios.git
```

### 2. Criar e Ativar um Ambiente Virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Os:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 4. Executar o App:

```bash
streamlit run data-app.py
```

## 👥 Equipe Desenvolvedora:

- Breno Caxias
- Priscila Áquila
- Mackena Teófilo
- João Marcos
- Agmy Lima
- Igor Cosmo
- Maria Camily
