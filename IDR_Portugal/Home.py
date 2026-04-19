import streamlit as st

# Configuração geral
st.set_page_config(page_title="Índice Digital Regional (IDR) Portugal", layout="wide", page_icon="💻")

# Estilo Customizado
st.markdown("""
<style>
    .stApp {
        background-color: #F9F9F7;
        color: #1E1E1E;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 {
        color: #2B3A67;
        letter-spacing: -0.5px;
    }
    .header {
        padding: 50px 0 20px 0;
        text-align: center;
    }
    .hero {
        background: linear-gradient(135deg, #6B7DA4 10%, #A9B8D8 90%);
        color: white;
        text-align: center;
        padding: 90px 30px;
        border-radius: 10px;
        margin-bottom: 40px;
    }
    .hero h1 {
        font-size: 64px;
        font-weight: 800;
    }
    .section {
        background: white;
        padding: 40px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Índice Digital Regional<br>Portugal 2026</h1>
    <p><em>A tecnologia ao serviço da coesão territorial.</em></p>
</div>
""", unsafe_allow_html=True)

# Texto institucional
st.markdown("""
<div class="section">
<h2>O que é o IDR?</h2>
<p>O <strong>Índice Digital Regional (IDR)</strong> afirma-se como um instrumento crítico e multidimensional de monitorização da Sociedade da Informação em Portugal, emergindo da necessidade imperativa de quantificar a maturidade tecnológica do território através de uma ótica regionalizada e cientificamente rigorosa.</p>

<p>Num cenário macroeconómico onde a digitalização opera como o principal vetor de convergência e competitividade, este projeto fundamenta a sua existência na análise das assimetrias estruturais que caracterizam o país.</p>

<p>A premissa estratégica do IDR reside na compreensão de que o desenvolvimento nacional não é um fenómeno uniforme, exigindo por isso uma escrutinação detalhada das divisões entre os polos de inovação do litoral e as dinâmicas de transição digital nas regiões do interior, assegurando que a evolução tecnológica seja mapeada com precisão geográfica e sociológica.</p>

<p>A opção pela nomenclatura de unidades territoriais para fins estatísticos (<strong>NUTS II</strong>) — englobando as regiões do Norte, Centro, Área Metropolitana de Lisboa, Alentejo, Algarve e as Regiões Autónomas dos Açores e da Madeira — é central para a validade científica do IDR.</p>

<p>Esta escala de análise garante não só a comparabilidade histórica dos dados, mas também a sua aplicabilidade direta na definição de prioridades para fundos estruturais e políticas de coesão territorial.</p>
</div>
""", unsafe_allow_html=True)
