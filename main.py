import streamlit as st

def pagina_inicio():
    st.title("Bienvenido a HomeDrive")
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
    if st.button("Abrir"):
        st.write("Garaje abierto")
    if st.button("Cerrar"):
        st.write("Garaje cerrado")
    if st.button("Volver al inicio"):
        st.session_state.pagina_actual = "inicio"

def pagina_luces():
    st.title("Control de Luces")
    if st.button("Encender"):
        st.write("Luces encendidas")
    if st.button("Apagar"):
        st.write("Luces apagadas")
    if st.button("Volver al inicio"):
        st.session_state.pagina_actual = "inicio"

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
