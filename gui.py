import streamlit as st
import requests

# Set up FastAPI URL
api_url = "http://localhost:8000/items/"

st.set_page_config(page_title="Meu app para testar a API de rolezinhos")

st.title("Teste de rolezinhos")

st.write("Use o menu para escolher o que testar.")


