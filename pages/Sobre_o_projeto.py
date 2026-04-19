import streamlit as st

st.set_page_config(page_title="IDR · Projeto", layout="wide", initial_sidebar_state="collapsed")

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
header, #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stSidebarCollapsedControl"] { visibility: hidden !important; display: none !important; }
html, body, .stApp { background: #F5F2C8 !important; font-family: 'DM Sans', sans-serif; color: #1A1714; }
[data-testid="stAppViewContainer"] { padding: 0 !important; }
[data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
.idr-nav { display:flex; justify-content:space-between; align-items:center; padding:28px 60px; border-bottom:1px solid rgba(26,23,20,0.15); position:sticky; top:0; background:#F5F2C8; z-index:100; }
.idr-nav-logo { font-family:'DM Serif Display',serif; font-size:22px; letter-spacing:0.04em; color:#1A1714; text-decoration:none; }
.idr-nav-links { display:flex; gap:48px; list-style:none; }
.idr-nav-links a { font-size:15px; font-weight:400; letter-spacing:0.08em; text-transform:uppercase; color:#1A1714; text-decoration:none; opacity:0.5; transition:opacity 0.2s; }
.idr-nav-links a:hover, .idr-nav-links a.active { opacity:1; }

.hero { display:grid; grid-template-columns:1fr 1fr; min-height:480px; border-bottom:1px solid rgba(26,23,20,0.15); }
.hero-left { padding:90px 60px; border-right:1px solid rgba(26,23,20,0.15); }
.eyebrow { font-size:13px; letter-spacing:0.14em; text-transform:uppercase; color:#6A6460; margin-bottom:20px; }
.hero-title { font-family:'DM Serif Display',serif; font-size:clamp(48px,6vw,72px); line-height:1.05; color:#1A1714; margin-bottom:32px; }
.hero-title em { font-style:italic; }
.hero-lead { font-size:clamp(17px,1.7vw,20px); line-height:1.8; color:#4A4540; font-weight:300; }
.hero-right { padding:90px 60px; background:#1A1714; display:flex; flex-direction:column; justify-content:flex-end; }
.quote { font-family:'DM Serif Display',serif; font-size:clamp(20px,2.2vw,28px); line-height:1.55; color:rgba(245,242,200,0.85); font-style:italic; margin-bottom:28px; }
.quote-src { font-size:13px; letter-spacing:0.1em; text-transform:uppercase; color:rgba(245,242,200,0.35); }

.eixos-section { padding:90px 60px; border-bottom:1px solid rgba(26,23,20,0.15); }
.section-label { font-size:13px; letter-spacing:0.14em; text-transform:uppercase; color:#6A6460; margin-bottom:52px; }
.eixos-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:1px; background:rgba(26,23,20,0.15); border:1px solid rgba(26,23,20,0.15); border-radius:4px; overflow:hidden; }
.eixo-card { background:#F5F2C8; padding:52px 44px; transition:background 0.2s; }
.eixo-card:hover { background:#EDE9BC; }
.eixo-num { font-family:'DM Serif Display',serif; font-size:60px; color:rgba(26,23,20,0.12); line-height:1; margin-bottom:24px; }
.eixo-title { font-family:'DM Serif Display',serif; font-size:28px; color:#1A1714; margin-bottom:18px; }
.eixo-body { font-size:15px; line-height:1.8; color:#6A6460; font-weight:300; }
.eixo-tags { display:flex; flex-wrap:wrap; gap:8px; margin-top:28px; }
.tag { font-size:11px; letter-spacing:0.08em; text-transform:uppercase; padding:5px 12px; border:1px solid rgba(26,23,20,0.25); border-radius:100px; color:#4A4540; }

.met { display:grid; grid-template-columns:1fr 2fr; border-bottom:1px solid rgba(26,23,20,0.15); }
.met-left { padding:90px 60px; border-right:1px solid rgba(26,23,20,0.15); display:flex; flex-direction:column; justify-content:center; }
.met-left h2 { font-family:'DM Serif Display',serif; font-size:clamp(32px,3.5vw,44px); line-height:1.2; color:#1A1714; margin-bottom:20px; }
.met-left h2 em { font-style:italic; }
.met-left p { font-size:15px; line-height:1.75; color:#6A6460; font-weight:300; }
.met-right { padding:90px 60px; }
.step { display:flex; gap:28px; margin-bottom:48px; padding-bottom:48px; border-bottom:1px solid rgba(26,23,20,0.1); }
.step:last-child { border-bottom:none; margin-bottom:0; padding-bottom:0; }
.step-num { font-family:'DM Serif Display',serif; font-size:36px; color:rgba(26,23,20,0.18); line-height:1; flex-shrink:0; width:44px; }
.step h4 { font-size:18px; font-weight:500; color:#1A1714; margin-bottom:10px; }
.step p { font-size:15px; line-height:1.75; color:#6A6460; font-weight:300; }

.fontes { padding:72px 60px; background:#EDE9BC; border-bottom:1px solid rgba(26,23,20,0.15); }
.fontes h3 { font-family:'DM Serif Display',serif; font-size:34px; color:#1A1714; margin-bottom:36px; }
.fontes-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }
.fonte-card { background:#F5F2C8; padding:28px; border-radius:4px; border:1px solid rgba(26,23,20,0.12); }
.fonte-name { font-size:16px; font-weight:500; color:#1A1714; margin-bottom:8px; }
.fonte-desc { font-size:13px; color:#9A9490; line-height:1.55; }

.idr-footer { padding:36px 60px; display:flex; justify-content:space-between; border-top:1px solid rgba(26,23,20,0.15); }
.idr-footer p { font-size:14px; color:#9A9490; }
"""

st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)

st.markdown("""
<nav class="idr-nav">
    <a class="idr-nav-logo" href="/" target="_self">IDR.PT</a>
    <ul class="idr-nav-links">
        <li><a href="/" target="_self">Início</a></li>
        <li><a href="/1_Graficos" target="_self">Análises</a></li>
        <li><a href="/Sobre_o_projeto" class="active">Projeto</a></li>
        <li><a href="/Contactos" target="_self">Contacto</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
<section class="hero">
    <div class="hero-left">
        <p class="eyebrow">O Projeto</p>
        <h1 class="hero-title">Sobre o <em>IDR</em></h1>
        <p class="hero-lead">O Índice Digital Regional é um instrumento multidimensional de monitorização da Sociedade da Informação em Portugal, construído para quantificar a maturidade tecnológica do território sob uma ótica regionalizada e cientificamente rigorosa.</p>
    </div>
    <div class="hero-right">
        <p class="quote">"A transformação digital não acontece em todo o território ao mesmo ritmo — o IDR torna essa assimetria visível e mensurável."</p>
        <p class="quote-src">Índice Digital Regional · Metodologia 2024</p>
    </div>
</section>

<section class="eixos-section">
    <p class="section-label">Quatro eixos de análise</p>
    <div class="eixos-grid">
        <div class="eixo-card">
            <div class="eixo-num">01</div>
            <h3 class="eixo-title">Contexto</h3>
            <p class="eixo-body">Analisa as condições estruturais e socioeconómicas que moldam a realidade digital de cada região. Inclui variáveis demográficas, educacionais e económicas.</p>
            <div class="eixo-tags"><span class="tag">Escolaridade</span><span class="tag">Demografia</span><span class="tag">PIB per capita</span></div>
        </div>
        <div class="eixo-card">
            <div class="eixo-num">02</div>
            <h3 class="eixo-title">Infraestrutura</h3>
            <p class="eixo-body">Avalia a infraestrutura tecnológica disponível, a cobertura de redes de alta velocidade e o investimento público em digitalização.</p>
            <div class="eixo-tags"><span class="tag">Fibra óptica</span><span class="tag">Cobertura 5G</span><span class="tag">Investimento</span></div>
        </div>
        <div class="eixo-card">
            <div class="eixo-num">03</div>
            <h3 class="eixo-title">Utilização</h3>
            <p class="eixo-body">Observa o comportamento digital efetivo de cidadãos e empresas — desde a utilização de serviços online à literacia digital da população.</p>
            <div class="eixo-tags"><span class="tag">Serviços online</span><span class="tag">E-commerce</span><span class="tag">Literacia digital</span></div>
        </div>
        <div class="eixo-card">
            <div class="eixo-num">04</div>
            <h3 class="eixo-title">Impacto</h3>
            <p class="eixo-body">Mede os efeitos reais da digitalização no território — produtividade, qualidade de vida, acesso a serviços públicos e redução de assimetrias.</p>
            <div class="eixo-tags"><span class="tag">Produtividade</span><span class="tag">Serviços públicos</span><span class="tag">Coesão</span></div>
        </div>
    </div>
</section>

<section class="met">
    <div class="met-left">
        <h2>Como é construído o <em>índice?</em></h2>
        <p>O IDR agrega indicadores de múltiplas fontes oficiais num score composto, normalizado e comparável entre regiões e ao longo do tempo.</p>
    </div>
    <div class="met-right">
        <div class="step"><div class="step-num">1</div><div><h4>Recolha de dados</h4><p>Extração via APIs do INE, PORDATA e Eurostat. Os dados são recolhidos anualmente e validados antes de integrarem o índice.</p></div></div>
        <div class="step"><div class="step-num">2</div><div><h4>Normalização</h4><p>Os valores de cada indicador são normalizados numa escala 0–1 para garantir comparabilidade entre variáveis de natureza e escala distintas.</p></div></div>
        <div class="step"><div class="step-num">3</div><div><h4>Ponderação e agregação</h4><p>Os indicadores são ponderados dentro de cada eixo e os eixos são agregados num score final por região NUTS II.</p></div></div>
        <div class="step"><div class="step-num">4</div><div><h4>Visualização e publicação</h4><p>Os resultados são disponibilizados com visualizações interativas que permitem explorar as assimetrias territoriais.</p></div></div>
    </div>
</section>

<section class="fontes">
    <h3>Fontes de dados</h3>
    <div class="fontes-grid">
        <div class="fonte-card"><div class="fonte-name">INE</div><div class="fonte-desc">Instituto Nacional de Estatística · Inquéritos à utilização de TIC</div></div>
        <div class="fonte-card"><div class="fonte-name">PORDATA</div><div class="fonte-desc">Base de dados Portugal Contemporâneo · Séries históricas regionais</div></div>
        <div class="fonte-card"><div class="fonte-name">Eurostat</div><div class="fonte-desc">Estatísticas da União Europeia · Comparação europeia NUTS II</div></div>
        <div class="fonte-card"><div class="fonte-name">ANACOM</div><div class="fonte-desc">Autoridade Nacional de Comunicações · Dados de infraestrutura e cobertura</div></div>
    </div>
</section>

<footer class="idr-footer">
    <p>© 2025 Índice Digital Regional · Portugal</p>
    <p>Dados: INE · PORDATA · Eurostat</p>
</footer>
""", unsafe_allow_html=True)
