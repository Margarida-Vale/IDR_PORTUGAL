import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gráficos IDR", layout="wide")

st.title(" Análises e Visualizações Regionais")

try:
    df = pd.read_json("Dados_IDR_Portugal.json")
except Exception as e:
    st.error("Erro ao carregar dados: " + str(e))
    st.stop()

# — Filtros dinâmicos
col1, col2 = st.columns(2)
indicador = col1.selectbox("Indicador", sorted(df["indicador"].unique()))
ano = col2.selectbox("Ano", sorted(df["ano"].unique(), reverse=True))

df_filtered = df[(df["indicador"] == indicador) & (df["ano"] == ano)]

# Placeholder para NUTS II (quando agregares)
# por enquanto, agrupamos genericamente por "regiao"
df_plot = df_filtered.groupby("regiao", as_index=False)["valor"].mean()

if df_plot.empty:
    st.warning("Sem dados disponíveis para esta seleção.")
else:
    fig = px.bar(
        df_plot,
        x="regiao",
        y="valor",
        color_discrete_sequence=["#6B7DA4"],
        title=f"Média por Região - {indicador} ({ano})"
    )
    st.plotly_chart(fig, use_container_width=True)
