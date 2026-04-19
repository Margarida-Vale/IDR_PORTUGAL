import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="IDR · Análises", layout="wide", initial_sidebar_state="collapsed")

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
header, #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stSidebarCollapsedControl"] { visibility: hidden !important; display: none !important; }
html, body, .stApp { background: #F5F2C8 !important; font-family: 'DM Sans', sans-serif; color: #1A1714; }
[data-testid="stAppViewContainer"] { padding: 0 !important; }
[data-testid="block-container"] { padding: 60px !important; max-width: 100% !important; }
.idr-nav { display:flex; justify-content:space-between; align-items:center; padding:28px 60px; border-bottom:1px solid rgba(26,23,20,0.15); position:sticky; top:0; background:#F5F2C8; z-index:100; margin:-60px -60px 60px -60px; }
.idr-nav-logo { font-family:'DM Serif Display',serif; font-size:22px; letter-spacing:0.04em; color:#1A1714; text-decoration:none; }
.idr-nav-links { display:flex; gap:48px; list-style:none; }
.idr-nav-links a { font-size:15px; font-weight:400; letter-spacing:0.08em; text-transform:uppercase; color:#1A1714; text-decoration:none; opacity:0.5; transition:opacity 0.2s; }
.idr-nav-links a:hover, .idr-nav-links a.active { opacity:1; }
h1 { font-family:'DM Serif Display',serif; font-size:clamp(48px,6vw,80px); font-weight:400; letter-spacing:-0.01em; color:#1A1714; margin-bottom:12px; line-height:1.05; }
h2 { font-family:'DM Serif Display',serif; font-size:clamp(28px,3vw,40px); font-weight:400; color:#1A1714; margin:48px 0 24px; }
.idr-eyebrow { font-size:13px; letter-spacing:0.14em; text-transform:uppercase; color:#6A6460; margin-bottom:16px; }
.idr-lead { font-size:clamp(17px,1.8vw,21px); line-height:1.75; color:#4A4540; font-weight:300; max-width:700px; margin-bottom:56px; }
.idr-divider { border:none; border-top:1px solid rgba(26,23,20,0.15); margin:56px 0; }
[data-testid="stSelectbox"] label, [data-testid="stMultiSelect"] label {
    font-size:13px !important; letter-spacing:0.08em !important; text-transform:uppercase !important;
    color:#6A6460 !important; font-weight:500 !important; font-family:'DM Sans',sans-serif !important;
}
[data-testid="stSelectbox"] > div > div, [data-testid="stMultiSelect"] > div > div {
    background:#F5F2C8 !important; border:1px solid rgba(26,23,20,0.2) !important;
    border-radius:4px !important; font-family:'DM Sans',sans-serif !important; font-size:15px !important;
}
"""

st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)

st.markdown("""
<nav class="idr-nav">
    <a class="idr-nav-logo" href="/" target="_self">IDR.PT</a>
    <ul class="idr-nav-links">
        <li><a href="/" target="_self">Início</a></li>
        <li><a href="/1_Graficos" class="active">Análises</a></li>
        <li><a href="/Sobre_o_projeto" target="_self">Projeto</a></li>
        <li><a href="/Contactos" target="_self">Contacto</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

st.markdown('<p class="idr-eyebrow">Observatório · Portugal Digital</p>', unsafe_allow_html=True)
st.markdown('<h1>Análises</h1>', unsafe_allow_html=True)
st.markdown('<p class="idr-lead">Explore os indicadores do Índice Digital Regional, compare regiões e acompanhe a evolução da maturidade digital em Portugal.</p>', unsafe_allow_html=True)

# ── Dados de exemplo ──
regioes = ["Norte", "Centro", "Oeste e V. Tejo", "Grande Lisboa", "P. Setúbal", "Alentejo", "Algarve", "R.A. Açores", "R.A. Madeira"]

df_indice = pd.DataFrame({
    "Região": regioes,
    "IDR 2022": [52, 44, 48, 71, 63, 38, 55, 42, 46],
    "IDR 2023": [55, 46, 51, 74, 66, 40, 58, 44, 49],
    "IDR 2024": [58, 49, 54, 77, 69, 43, 61, 47, 52],
})

df_eixos = pd.DataFrame({
    "Região": regioes,
    "Contexto":     [60, 50, 52, 78, 70, 42, 60, 48, 53],
    "Utilização":   [56, 47, 53, 76, 68, 41, 62, 45, 51],
    "Oferta":       [58, 50, 57, 77, 69, 46, 61, 48, 52],
    "Impacto":      [55, 48, 54, 75, 67, 42, 59, 46, 50],
})

st.markdown('<hr class="idr-divider">', unsafe_allow_html=True)
st.markdown('<h2>Índice Global por Região</h2>', unsafe_allow_html=True)

ano = st.selectbox("Ano de referência", ["IDR 2024", "IDR 2023", "IDR 2022"])
df_sorted = df_indice[["Região", ano]].sort_values(ano, ascending=True)

cor_map = {r: "#1A1714" if r != "Grande Lisboa" else "#2A52A0" for r in regioes}
cores = [cor_map[r] for r in df_sorted["Região"]]

fig1 = px.bar(
    df_sorted, x=ano, y="Região", orientation="h",
    color="Região", color_discrete_sequence=cores,
    text=ano,
)
fig1.update_traces(textposition="outside", textfont_size=14, marker_line_width=0)
fig1.update_layout(
    plot_bgcolor="#F5F2C8", paper_bgcolor="#F5F2C8",
    showlegend=False, margin=dict(l=0, r=40, t=10, b=10),
    xaxis=dict(range=[0,100], showgrid=True, gridcolor="rgba(26,23,20,0.08)", tickfont_size=13),
    yaxis=dict(showgrid=False, tickfont_size=14),
    height=420, font_family="DM Sans",
)
st.plotly_chart(fig1, use_container_width=True)

st.markdown('<hr class="idr-divider">', unsafe_allow_html=True)
st.markdown('<h2>Evolução Temporal</h2>', unsafe_allow_html=True)

regioes_sel = st.multiselect(
    "Selecione regiões",
    regioes,
    default=["Norte", "Grande Lisboa", "Alentejo"]
)

df_melt = df_indice.melt(id_vars="Região", var_name="Ano", value_name="IDR")
df_melt["Ano"] = df_melt["Ano"].str.replace("IDR ", "")
df_linha = df_melt[df_melt["Região"].isin(regioes_sel)]

fig2 = px.line(
    df_linha, x="Ano", y="IDR", color="Região",
    markers=True,
    color_discrete_sequence=["#1A1714","#2A52A0","#8A9490","#C4A882","#6A6460","#3A6440"],
)
fig2.update_traces(line_width=2.5, marker_size=8)
fig2.update_layout(
    plot_bgcolor="#F5F2C8", paper_bgcolor="#F5F2C8",
    margin=dict(l=0, r=20, t=10, b=10),
    xaxis=dict(showgrid=False, tickfont_size=13),
    yaxis=dict(range=[30,90], showgrid=True, gridcolor="rgba(26,23,20,0.08)", tickfont_size=13),
    height=380, font_family="DM Sans", legend_font_size=14,
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown('<hr class="idr-divider">', unsafe_allow_html=True)
st.markdown('<h2>Decomposição por Eixo</h2>', unsafe_allow_html=True)

regiao_sel = st.selectbox("Selecione uma região", regioes)
df_r = df_eixos[df_eixos["Região"] == regiao_sel].melt(id_vars="Região", var_name="Eixo", value_name="Score")

fig3 = px.bar(
    df_r, x="Eixo", y="Score",
    color="Eixo",
    color_discrete_sequence=["#1A1714","#2A52A0","#8A9490","#C4A882"],
    text="Score",
)
fig3.update_traces(textposition="outside", textfont_size=15, marker_line_width=0)
fig3.update_layout(
    plot_bgcolor="#F5F2C8", paper_bgcolor="#F5F2C8",
    showlegend=False, margin=dict(l=0, r=20, t=10, b=10),
    xaxis=dict(showgrid=False, tickfont_size=15),
    yaxis=dict(range=[0,100], showgrid=True, gridcolor="rgba(26,23,20,0.08)", tickfont_size=13),
    height=360, font_family="DM Sans",
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<footer style="margin-top:80px;padding:36px 0;border-top:1px solid rgba(26,23,20,0.15);display:flex;justify-content:space-between;">
    <p style="font-size:14px;color:#9A9490;">© 2025 Índice Digital Regional · Portugal</p>
    <p style="font-size:14px;color:#9A9490;">Dados: INE · PORDATA · Eurostat</p>
</footer>
""", unsafe_allow_html=True)
