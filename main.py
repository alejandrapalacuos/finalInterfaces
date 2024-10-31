import streamlit as st

# Variables para controlar el estado de las páginas
pagina_actual = "inicio"

def pagina_inicio():
    st.title("Bienvenido a HomeDrive")
    if st.button("Empezar"):
        st.session_state.pagina_actual = "garaje"

def pagina_garaje():
    st.title("Control del Garaje")
    if st.button("Abrir"):
        st.write("Garaje abierto")
    if st.button("Cerrar"):
        st.write("Garaje cerrado")
    if st.button("Ir a Luces"):
        st.session_state.pagina_actual = "luces"

def pagina_luces():
    st.title("Control de Luces")
    if st.button("Encender"):
        st.write("Luces encendidas")
    if st.button("Apagar"):
        st.write("Luces apagadas")
    if st.button("Volver al Garaje"):
        st.session_state.pagina_actual = "garaje"

# Función principal de la aplicación
def main():
    # Utiliza st.session_state para almacenar el estado de la página actual
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Muestra la página correspondiente según el estado
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'garaje':
        pagina_garaje()
    elif st.session_state.pagina_actual == 'luces':
        pagina_luces()

if __name__ == "__main__":
    main()
