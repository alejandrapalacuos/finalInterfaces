import streamlit as st
from streamlit_icons import Icons

# Variables for controlling the state of the pages
pagina_actual = "inicio"

def pagina_inicio():
    st.title("Bienvenido a HomeDrive")
    if st.button("Empezar"):
        st.session_state.pagina_actual = "garaje"

def pagina_garaje():
    st.title("Control del Garaje")
    if st.button(Icons.garage):  # Button with garage icon
        st.write("Garaje abierto")
    if st.button(Icons.door_closed):  # Button with closed door icon
        st.write("Garaje cerrado")
    if st.button(Icons.lightbulb):  # Button with light bulb icon
        st.session_state.pagina_actual = "luces"

def pagina_luces():
    st.title("Control de Luces")
    if st.button(Icons.lightbulb_on):  # Button with light bulb on icon
        st.write("Luces encendidas")
    if st.button(Icons.lightbulb_off):  # Button with light bulb off icon
        st.write("Luces apagadas")
    if st.button(Icons.garage):  # Button with garage icon
        st.session_state.pagina_actual = "garaje"

# Main function of the application
def main():
    # Use st.session_state to store the current page state
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Show the corresponding page based on the state
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'garaje':
        pagina_garaje()
    elif st.session_state.pagina_actual == 'luces':
        pagina_luces()

if __name__ == "__main__":
    main()
