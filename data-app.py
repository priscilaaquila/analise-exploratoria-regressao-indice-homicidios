# Run with: python -m streamlit run .\data-app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Trabalho 01 - Homicídios", layout="wide")
st.title("Análise e Regressão: Homicídios (UNODC)")


# CARREGAR OS DADOS
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data_cts_intentional_homicide.csv")
    df = df.drop_duplicates()

    df["VALUE"] = df["VALUE"].astype(str).str.strip().str.replace(",", ".", regex=False)
    df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")

    return df

df_completo = carregar_dados()

# Homicídios totais entre 2013 e 2022
homicidios = df_completo[
    (df_completo["Indicator"] == "Victims of intentional homicide") &
    (df_completo["Sex"] == "Total") &
    (df_completo["Unit of measurement"] == "Rate per 100,000 population") &
    (df_completo["Year"] >= 2013) &
    (df_completo["Year"] <= 2022)
]

st.write("### Visualização dos Dados Brutos")
st.dataframe(homicidios.head())


# ANÁLISE EXPLORATÓRIA

st.write("---")
st.header("Análise Exploratória")


opcoes_graficos = [
    "Distribuição das Taxas de Homicídio (2013-2022)",
    "Evolução Média das Taxas (2013-2022)",
    "Top 10 Países com Maiores Médias (2013-2022)",
    "1- Top 10 Países com Maiores Taxas (2018-2022)",
    "2- Top 10 Países: Homicídio de Mulheres (2022)",
    "3- Média das Taxas de Homicídio por Região",
    "4- Menores Taxas Médias por Sub-região (2013-2022)",
    "5- Top 10 Países: Menores Taxas (Mulheres)",
    "6- Sub-regiões com Maior Número de Homicídios",
    "7- Países com Maior Taxa por Continente (2020)",
    "8- Top 10 Países: Vítimas Femininas (2021)",
    "10- Evolução dos Homicídios no Brasil"
]

opcao_grafico = st.selectbox("Selecione o gráfico que deseja visualizar:", opcoes_graficos)

if opcao_grafico == "Distribuição das Taxas de Homicídio (2013-2022)":
    fig = px.histogram(homicidios, x="VALUE", nbins=40, title="Distribuição das Taxas de Homicídio (2013-2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "Evolução Média das Taxas (2013-2022)":
    tabela = homicidios.groupby("Year")["VALUE"].mean().reset_index()
    fig = px.line(tabela, x="Year", y="VALUE", title="Evolução Média das Taxas de Homicídio (2013-2022)", markers=True)
    fig.update_xaxes(dtick=1)
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "Top 10 Países com Maiores Médias (2013-2022)":
    tabela = homicidios.groupby("Country")["VALUE"].mean().reset_index().sort_values("VALUE", ascending=False).head(10)
    fig = px.bar(tabela, x="Country", y="VALUE", title="Top 10 Países com Maiores Médias (2013-2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "1- Top 10 Países com Maiores Taxas (2018-2022)":
    tabela = homicidios[homicidios["Year"] >= 2018].groupby("Country")["VALUE"].mean().reset_index().sort_values("VALUE", ascending=False).head(10)
    fig = px.bar(tabela, x="Country", y="VALUE", title="Top 10 Países com Maiores Taxas (2018-2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "2- Top 10 Países: Homicídio de Mulheres (2022)":
    mulheres_2022 = df_completo[
        (df_completo["Indicator"] == "Victims of intentional homicide") &
        (df_completo["Sex"] == "Female") &
        (df_completo["Unit of measurement"] == "Rate per 100,000 population") &
        (df_completo["Year"] == 2022)
    ]
    tabela = mulheres_2022.groupby("Country")["VALUE"].mean().reset_index().sort_values("VALUE", ascending=False).head(10)
    fig = px.bar(tabela, x="Country", y="VALUE", title="Top 10 Países: Homicídio de Mulheres (2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "3- Média das Taxas de Homicídio por Região":
    tabela = homicidios.groupby("Region")["VALUE"].mean().reset_index().sort_values("VALUE", ascending=False)
    fig = px.bar(tabela, x="Region", y="VALUE", title="Média das Taxas de Homicídio por Região")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "4- Menores Taxas Médias por Sub-região (2013-2022)":
    df_total = df_completo[(df_completo["Sex"].str.strip().str.lower() == "total") & (df_completo["Year"].between(2013, 2022))]
    df_total = df_total[~df_total["Country"].str.contains("All|World", case=False, na=False)]

    tabela = df_total.groupby(["Subregion", "Country"])["VALUE"].mean().reset_index()
    tabela = tabela.sort_values(["Subregion", "VALUE"]).groupby("Subregion").first().reset_index()
    tabela["Rotulo"] = tabela["Country"] + " (" + tabela["Subregion"] + ")"
    tabela = tabela.sort_values("VALUE", ascending=True)

    fig = px.bar(tabela, x="Rotulo", y="VALUE", title="Menores Taxas Médias por Sub-região (2013-2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "5- Top 10 Países: Menores Taxas (Mulheres)":
    mulheres = df_completo[(df_completo["Sex"] == "Female")]
    tabela = mulheres.groupby("Country")["VALUE"].sum().reset_index().sort_values("VALUE", ascending=True).head(10)
    fig = px.bar(tabela, x="Country", y="VALUE", title="Top 10 Países: Menores Taxas (Homicídio de Mulheres)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "6- Sub-regiões com Maior Número de Homicídios":
    df_total = df_completo[(df_completo["Sex"].str.strip().str.lower() == "total") & (df_completo["Year"].between(2013, 2022))]
    tabela = df_total.groupby("Subregion")["VALUE"].mean().reset_index().sort_values("VALUE", ascending=False).head(10)

    fig = px.bar(tabela, x="VALUE", y="Subregion", orientation='h', title="Sub-regiões com o Maior Número de Homicídios (2013-2022)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "7- Países com Maior Taxa por Continente (2020)":
    df_2020 = df_completo[(df_completo["Sex"].str.strip().str.lower() == "total") & (df_completo["Year"] == 2020)]
    df_2020 = df_2020[~df_2020["Country"].isin(df_2020["Region"].unique())]

    tabela = df_2020.groupby(["Region", "Country"])["VALUE"].sum().reset_index()
    tabela = tabela.sort_values(["Region", "VALUE"], ascending=[True, False]).groupby("Region").first().reset_index()
    tabela["Rotulo"] = tabela["Country"] + " (" + tabela["Region"] + ")"
    tabela = tabela.sort_values("VALUE", ascending=False)

    fig = px.bar(tabela, x="VALUE", y="Rotulo", orientation='h', title="Maior Taxa de Homicídios por Continente (2020)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "8- Top 10 Países: Vítimas Femininas (2021)":
    df_fem = df_completo[df_completo["Sex"].str.strip().str.lower() == "female"]
    df_fem = df_fem[~df_fem["Country"].str.contains("All|World", case=False, na=False)]
    df_fem_2021 = df_fem[df_fem["Year"] == 2021]

    tabela = df_fem_2021.groupby("Country")["VALUE"].sum().reset_index().sort_values("VALUE", ascending=False).head(10)
    fig = px.bar(tabela, x="VALUE", y="Country", orientation='h', title="10 Países com o Maior Número de Vítimas Femininas (2021)")
    st.plotly_chart(fig, use_container_width=True)

elif opcao_grafico == "10- Evolução dos Homicídios no Brasil":
    df_total = df_completo[df_completo["Sex"].str.strip().str.lower() == "total"]
    df_brasil = df_total[df_total["Country"].str.strip().str.lower() == "brazil"]

    tabela = df_brasil.groupby("Year")["VALUE"].sum().reset_index()
    media_br = tabela["VALUE"].mean()

    fig = px.line(tabela, x="Year", y="VALUE", markers=True, title="Evolução dos Homicídios no Brasil")
    fig.add_hline(y=media_br, line_dash="dash", line_color="red", annotation_text=f"Média: {media_br:.0f}")
    fig.update_xaxes(dtick=1)
    st.plotly_chart(fig, use_container_width=True)


# MODELO DE REGRESSÃO

st.write("---")
st.header("Predição com Regressão Linear")

homicidios_all_range = df_completo[
    (df_completo["Sex"] == "Total") &
    (df_completo["Unit of measurement"] == "Rate per 100,000 population")
]

tabela_ano = homicidios_all_range.groupby("Year")["VALUE"].sum().reset_index()

X = tabela_ano[["Year"]]
y = tabela_ano["VALUE"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=996)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# ENTRADA DO UTILIZADOR E RESULTADO

ano_desejado = st.number_input("Digite o ano para a predição:", value=2024, step=1)

botao = st.button("Fazer Predição")

if botao:
    dado_futuro = pd.DataFrame({"Year": [ano_desejado]})
    predicao = modelo.predict(dado_futuro)[0]

    st.success(f"A taxa média global prevista para o ano {ano_desejado} é de: {predicao:.4f} por 100 mil habitantes.")