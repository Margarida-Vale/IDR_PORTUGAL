import streamlit as st

st.set_page_config(page_title="Contactos", layout="wide")
st.title(" Contactos")

st.write("Se pretendes contactar a equipa do projeto IDR:")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Equipa Técnica:**  
    idr.portugal@exemplo.pt  
    **Endereço:**  
    Lisboa, Portugal  
    """)
with col2:
    st.text_input("Nome")
    st.text_input("Email")
    st.text_area("Mensagem")
    st.button("Enviar")
