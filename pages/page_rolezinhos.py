import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import polyline

API_URL = "http://localhost:8000"
st.title("Pagina: rolezinnhos")
st.write("Aqui se testa funcionlidades de buscas a rolezinhos.")

def show_bars_on_map():
    st.header("Exibir Bares no Mapa")
    response = requests.get(f"{API_URL}/bares/")
    if response.status_code == 200:
        bars = response.json()
        # Criar o mapa centralizado nas coordenadas médias
        if bars:
            first_bar = bars[0]
            map_center = [first_bar['gps']['coordinates'][0], first_bar['gps']['coordinates'][1]]
            m = folium.Map(location=map_center, zoom_start=12)

            # Adicionar os bares ao mapa
            for bar in bars:
                folium.Marker(
                    location=[bar['gps']['coordinates'][0], bar['gps']['coordinates'][1]],
                    popup=f"{bar['nome']}: {bar['descricao']}",
                    tooltip=bar['nome'],
                    icon =folium.Icon(icon="info-sign")
                ).add_to(m)

            # Renderizar o mapa no Streamlit
            st_data = st_folium(m, width=725)
        else:
            st.write("Nenhum bar encontrado.")
    else:
        st.error("Erro ao buscar bares.")

def show_role_geral():
    st.header("Exibir Bares no Mapa")
    response = requests.get(f"{API_URL}/bares/")
    if response.status_code == 200:
        bars = response.json()

        if bars and len(bars) >1:
            first_bar = bars[0]
            last_bar = bars[-1]
            
            c_first_bar = first_bar['gps']['coordinates']
            c_last_bar = last_bar['gps']['coordinates']
            map_center = [(c_first_bar[0] + c_last_bar[0]) / 2, (c_first_bar[1] + c_last_bar[1]) / 2]
            m = folium.Map(location=map_center, zoom_start=12)

            for bar in bars:
                folium.Marker(
                    location=[bar['gps']['coordinates'][0], bar['gps']['coordinates'][1]],
                    popup=f"{bar['nome']}: {bar['descricao']}",
                    tooltip=bar['nome'],
                    icon =folium.Icon(icon="info-sign")
                ).add_to(m)

            point_a = bars[0]['gps']['coordinates']
            for bar_b in bars[2:]:
                # OSRM URL for route calculation
                point_b = bar_b['gps']['coordinates']

                coordinates = f"{point_a[1]},{point_a[0]};{point_b[1]},{point_b[0]}"
                osrm_url = f"http://router.project-osrm.org/route/v1/driving/{coordinates}?overview=full"

                # Get the route from OSRM
                response = requests.get(osrm_url)
                data = response.json()

                if 'routes' in data.keys():
                    route_geometry = data['routes'][0]['geometry']
                    decoded_route = polyline.decode(route_geometry)
                    folium.PolyLine(locations=decoded_route, color="blue", weight=2.5).add_to(m)
                    point_a = point_b

            st_data = st_folium(m, width=725)
        else:
            st.write(f"{len(bars)} encontrado(s).")
    else:
        st.error("Erro ao buscar bares.")



option = st.sidebar.selectbox("Selecione a operação", ["Mapa","Role geral"])

if option == "Role geral":
    show_role_geral()
elif option == "Mapa":
    show_bars_on_map()
