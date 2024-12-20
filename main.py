
import streamlit as st
from PIL import Image


def pagina_inicio():
    image = Image.open('homedrive.png')
    st.image(image, width=350)
    if st.button("Empezar"):
        st.session_state.pagina_actual = "elegir_accion"
    else:
        st.write("Haz clic en 'Empezar' para continuar.")

def pagina_elegir_accion():
    st.title("Selecciona una acción")
    if st.button("Garaje"):
        st.session_state.pagina_actual = "garaje"
    if st.button("Luces"):
        st.session_state.pagina_actual = "luces"

def pagina_garaje():
    st.title("Control del Garaje")
    st.link_button("Abrir", "https://abrirgaraje.streamlit.app/") 
    if st.button("Volver"):
        st.session_state.pagina_actual = "elegir_accion"

def pagina_luces():
    st.title("Control de Luces")
    st.link_button("Encender luces", "https://contolvoz-8rmjmhldtnyfzartcqykwy.streamlit.app/")
    st.link_button("Apagar luces", "https://lucesboton.streamlit.app/")
    
    if st.button("Volver"):
        st.session_state.pagina_actual = "elegir_accion"
        

def main():
    # Inicializa el estado de la sesión si no existe
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Muestra la página correspondiente según el estado actual
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'elegir_accion':
        pagina_elegir_accion()
    elif st.session_state.pagina_actual == 'garaje':
        pagina_garaje()
    elif st.session_state.pagina_actual == 'luces':
        pagina_luces()

if __name__ == "__main__":
    main()
