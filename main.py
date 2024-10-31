import streamlit as st
from streamlit_icons import Icons

# Variables para controlar el estado de las páginas
pagina_actual = "inicio"

def pagina_inicio():
    st.title("Bienvenido a HomeDrive")
    if st.button("Empezar"):
        st.session_state.pagina_actual = "garaje"

def pagina_garaje():
    st.title("Control del Garaje")
    if st.button(Icons.garage):  # Botón con el icono de garaje
        st.write("Garaje abierto")
    if st.button(Icons.door_closed):  # Botón con el icono de puerta cerrada
        st.write("Garaje cerrado")
    if st.button(Icons.lightbulb):  # Botón con el icono de bombilla
        st.session_state.pagina_actual = "luces"

def pagina_luces():
    st.title("Control de Luces")
    if st.button(Icons.lightbulb_on):  # Botón con el icono de bombilla encendida
        st.write("Luces encendidas")
    if st.button(Icons.lightbulb_off):  # Botón con el icono de bombilla apagada
        st.write("Luces apagadas")
    if st.button(Icons.garage):  # Botón con el icono de garaje
        st.session_state.pagina_actual = "garaje"

# Función principal de la aplicación
def main():
    # Utiliza st.session_state para almacenar el estado de la página actual
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Muestra la página correspondiente según el estado
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_ca
