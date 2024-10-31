import streamlit as st

# Variables for page control
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

# ... and so on for other pages

# Main function
def main():
    # Use st.session_state to store current page state
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Show the corresponding page based on state
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'garaje':
        pagina_garaje()
    # ... and so on for other pages

if __name__ == "__main__":
    main()
