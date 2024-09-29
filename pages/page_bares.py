import streamlit as st
import requests
from typing import List
import folium
from streamlit_folium import st_folium

API_URL = "http://localhost:8000"  # Mude para a URL da sua API se estiver rodando remotamente

# Página para criar um novo bar
def create_bar():
    st.header("Criar Bar")
    name = st.text_input("Nome do Bar")
    endereco = st.text_input("Endereço do Bar")
    descricao = st.text_area("Descrição do Bar")
    gps_type = st.text_input("Tipo de GPS", value="Point")
    gps_lat = st.number_input("Latitude", format="%f")
    gps_lon = st.number_input("Longitude", format="%f")

    if st.button("Criar"):
        data = {
            "nome": name,
            "endereco": endereco,
            "descricao": descricao,
            "gps": {
                "type": gps_type,
                "coordinates": [gps_lat, gps_lon]
            }
        }
        response = requests.post(f"{API_URL}/bares/novo", json=data)
        if response.status_code == 200:
            st.success("Bar criado com sucesso!")
        else:
            st.error(f"Erro: {response.text}")

# Página para listar todos os bares
def list_bars():
    st.header("Listar Bares")
    response = requests.get(f"{API_URL}/bares/")
    if response.status_code == 200:
        bars = response.json()
        for bar in bars:
            st.write(f"Nome: {bar['nome']}")
            st.write(f"Endereço: {bar['endereco']}")
            st.write(f"Descrição: {bar['descricao']}")
            st.write(f"GPS: Tipo: {bar['gps']['type']}, Coordenadas: {bar['gps']['coordinates']}")
            st.write("---")
    else:
        st.error("Erro ao listar bares")

# Página para ler um bar específico
def get_bar():
    st.header("Ler Bar")
# CRUD bares
import streamlit as st

st.title("Page bares")
import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Mude para a URL da sua API se estiver rodando remotamente

# Página para criar um novo bar
def create_bar():
    st.header("Criar Bar")
    name = st.text_input("Nome do Bar")
    location = st.text_input("Localização do Bar")

    if st.button("Criar"):
        data = {"nome": name, "localizacao": location}
        response = requests.post(f"{API_URL}/bares/novo", json=data)
        if response.status_code == 200:
            st.success("Bar criado com sucesso!")
        else:
            st.error(f"Erro: {response.text}")

# Página para listar todos os bares
def list_bars():
    st.header("Listar Bares")
    response = requests.get(f"{API_URL}/bares/")
    if response.status_code == 200:
        bars = response.json()
        for bar in bars:
            st.write(f"Nome: {bar['nome']}, Localização: {bar['endereco']} + {bar['gps']['coordinates']}")
    else:
        st.error("Erro ao listar bares")

# Página para ler um bar específico
def get_bar():
    st.header("Ler Bar")
    bar_id = st.text_input("ID do Bar", value="66f99eb1409670033e96403a")

    if st.button("Buscar"):
        response = requests.get(f"{API_URL}/bares/{bar_id}")
        if response.status_code == 200:
            bar = response.json()
            st.write(f"Nome: {bar['nome']}")
            st.write(f"Endereço: {bar['endereco']}")
            st.write(f"Descrição: {bar['descricao']}")
            st.write(f"GPS: Tipo: {bar['gps']['type']}, Coordenadas: {bar['gps']['coordinates']}")
        else:
            st.error(f"Erro: {response.text}")

# Página para atualizar um bar
def update_bar():
    st.header("Atualizar Bar")
    bar_id = st.text_input("ID do Bar", value="66f99eb1409670033e96403a")

    if st.button("Buscar"):
        response = requests.get(f"{API_URL}/bares/{bar_id}")
        if response.status_code == 200:
            bar = response.json()
            st.write(f"Nome: {bar['nome']}")
            st.write(f"Endereço: {bar['endereco']}")
            st.write(f"Descrição: {bar['descricao']}")
            st.write(f"GPS: Tipo: {bar['gps']['type']}, Coordenadas: {bar['gps']['coordinates']}")
        else:
            st.error(f"Erro: {response.text}")

# Página para atualizar um bar
def update_bar():
    st.header("Atualizar Bar")
    bar_id = st.text_input("ID do Bar")
    name = st.text_input("Novo Nome")
    endereco = st.text_input("Novo Endereço")
    descricao = st.text_area("Nova Descrição")
    gps_type = st.text_input("Tipo de GPS", value="Point")
    gps_lat = st.number_input("Nova Latitude", format="%f")
    gps_lon = st.number_input("Nova Longitude", format="%f")

    if st.button("Atualizar"):
        data = {
            "nome": name,
            "endereco": endereco,
            "descricao": descricao,
            "gps": {
                "type": gps_type,
                "coordinates": [gps_lat, gps_lon]
            }
        }
        response = requests.put(f"{API_URL}/bares/{bar_id}", json=data)
        if response.status_code == 200:
            st.success("Bar atualizado com sucesso!")
        else:
            st.error(f"Erro: {response.text}")

# Página para deletar um bar
def delete_bar():
    st.header("Deletar Bar")
    bar_id = st.text_input("ID do Bar para Deletar")

    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/bares/{bar_id}")
        if response.status_code == 200:
            st.success("Bar deletado com sucesso!")
        else:
            st.error(f"Erro: {response.text}")



# Menu de navegação
option = st.sidebar.selectbox("Selecione a operação", ["Mapa","Criar Bar", "Listar Bares", "Ler Bar", "Atualizar Bar", "Deletar Bar"])

if option == "Criar Bar":
    create_bar()
elif option == "Listar Bares":
    list_bars()
elif option == "Ler Bar":
    get_bar()
elif option == "Atualizar Bar":
    update_bar()
elif option == "Deletar Bar":
    delete_bar()

