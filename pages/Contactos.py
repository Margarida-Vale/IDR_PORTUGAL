import streamlit as st

st.set_page_config(page_title="IDR · Contacto", layout="wide", initial_sidebar_state="collapsed")

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
header, #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stSidebarCollapsedControl"] { visibility: hidden !important; display: none !important; }
html, body, .stApp { background: #F5F2C8 !important; font-family: 'DM Sans', sans-serif; color: #1A1714; }
[data-testid="stAppViewContainer"] { padding: 0 !important; }
[data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
.stColumns { gap: 0 !important; }
.idr-nav { display:flex; justify-content:space-between; align-items:center; padding:28px 60px; border-bottom:1px solid rgba(26,23,20,0.15); position:sticky; top:0; background:#F5F2C8; z-index:100; }
.idr-nav-logo { font-family:'DM Serif Display',serif; font-size:22px; letter-spacing:0.04em; color:#1A1714; text-decoration:none; }
.idr-nav-links { display:flex; gap:48px; list-style:none; }
.idr-nav-links a { font-size:15px; font-weight:400; letter-spacing:0.08em; text-transform:uppercase; color:#1A1714; text-decoration:none; opacity:0.5; transition:opacity 0.2s; }
.idr-nav-links a:hover, .idr-nav-links a.active { opacity:1; }
.col-left { padding:90px 60px; border-right:1px solid rgba(26,23,20,0.15); height:100%; display:flex; flex-direction:column; justify-content:space-between; }
.eyebrow { font-size:13px; letter-spacing:0.14em; text-transform:uppercase; color:#6A6460; margin-bottom:20px; }
.title { font-family:'DM Serif Display',serif; font-size:clamp(48px,6vw,72px); line-height:1.05; color:#1A1714; margin-bottom:32px; }
.title em { font-style:italic; }
.lead { font-size:clamp(16px,1.6vw,19px); line-height:1.8; color:#4A4540; font-weight:300; max-width:440px; margin-bottom:56px; }
.infos { display:flex; flex-direction:column; gap:36px; }
.info-label { font-size:12px; letter-spacing:0.12em; text-transform:uppercase; color:#9A9490; font-weight:500; margin-bottom:6px; }
.info-val { font-size:16px; color:#1A1714; }
.info-val a { color:#1A1714; text-decoration:underline; }
.bottom-note { margin-top:56px; padding-top:36px; border-top:1px solid rgba(26,23,20,0.15); font-size:14px; line-height:1.65; color:#9A9490; }
.col-right { padding:90px 60px; background:#EDE9BC; }
.form-title { font-family:'DM Serif Display',serif; font-size:clamp(28px,3vw,40px); color:#1A1714; margin-bottom:44px; }
.form-title em { font-style:italic; }
[data-testid="stTextInput"] label, [data-testid="stTextArea"] label, [data-testid="stSelectbox"] label {
    font-size:13px !important; letter-spacing:0.08em !important; text-transform:uppercase !important;
    color:#6A6460 !important; font-weight:500 !important; font-family:'DM Sans',sans-serif !important;
}
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background:#F5F2C8 !important; border:1px solid rgba(26,23,20,0.2) !important;
    border-radius:4px !important; font-family:'DM Sans',sans-serif !important;
    font-size:16px !important; color:#1A1714 !important; padding:14px 16px !important;
}
[data-testid="stSelectbox"] > div > div {
    background:#F5F2C8 !important; border:1px solid rgba(26,23,20,0.2) !important;
    border-radius:4px !important; font-size:16px !important;
}
[data-testid="stTextArea"] textarea { min-height:140px !important; }
.stButton button {
    font-family:'DM Sans',sans-serif !important; font-size:15px !important;
    font-weight:500 !important; letter-spacing:0.08em !important; text-transform:uppercase !important;
    padding:16px 36px !important; background:#1A1714 !important; color:#F5F2C8 !important;
    border:none !important; border-radius:4px !important; width:100% !important;
    transition:background 0.2s !important;
}
.stButton button:hover { background:#2A52A0 !important; }
"""

st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)

st.markdown("""
<nav class="idr-nav">
    <a class="idr-nav-logo" href="/" target="_self">IDR.PT</a>
    <ul class="idr-nav-links">
        <li><a href="/" target="_self">Início</a></li>
        <li><a href="/1_Graficos" target="_self">Análises</a></li>
        <li><a href="/Sobre_o_projeto" target="_self">Projeto</a></li>
        <li><a href="/Contactos" class="active">Contacto</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

col_esq, col_dir = st.columns(2)

with col_esq:
    st.markdown("""
    <div class="col-left">
        <div>
            <p class="eyebrow">Fale connosco</p>
            <h1 class="title">Entre em<br><em>Contacto</em></h1>
            <p class="lead">Tem questões sobre a metodologia, quer aceder aos dados brutos ou propor colaboração? Estamos disponíveis.</p>
            <div class="infos">
                <div><div class="info-label">Email</div><div class="info-val"><a href="mailto:idr.portugal@exemplo.pt">idr.portugal@exemplo.pt</a></div></div>
                <div><div class="info-label">Localização</div><div class="info-val">Lisboa, Portugal</div></div>
                <div><div class="info-label">Publicação</div><div class="info-val">Relatório anual · Edição 2024</div></div>
            </div>
        </div>
        <div class="bottom-note">Os dados do IDR são de acesso livre e podem ser utilizados para fins académicos, jornalísticos e de política pública com devida atribuição.</div>
    </div>
    """, unsafe_allow_html=True)

with col_dir:
    st.markdown('<div class="col-right">', unsafe_allow_html=True)
    st.markdown('<h2 class="form-title">Envie uma <em>mensagem</em></h2>', unsafe_allow_html=True)

    assunto = st.selectbox("Assunto", ["Questão metodológica","Acesso aos dados","Proposta de colaboração","Imprensa / Media","Outro"])
    col_n, col_e = st.columns(2)
    with col_n: nome = st.text_input("Nome")
    with col_e: email = st.text_input("Email")
    mensagem = st.text_area("Mensagem", height=150)

    if st.button("Enviar mensagem →"):
        if nome and email and mensagem:
            st.success("Mensagem enviada. Responderemos brevemente.")
        else:
            st.warning("Por favor preencha todos os campos.")

    st.markdown('</div>', unsafe_allow_html=True)
