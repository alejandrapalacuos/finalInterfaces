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

# ... y así sucesivamente para cada página

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
    # ... y así sucesivamente para cada página

if __name__ == "__main__":
    main()import streamlit as st

# Variables para controlar el estado de las pantallas
mostrar_garaje = False

st.title("Bienvenido a HomeDrive")

if st.button("Empezar"):
    mostrar_garaje = True

if mostrar_garaje:
    st.sidebar.title("Controles")
    
    # Pantalla de garaje
    st.sidebar.header("Garaje")
    if st.sidebar.button("Abrir"):
        st.write("Garaje abierto")
    if st.sidebar.button("Cerrar"):
        st.write("Garaje cerrado")
    
    # Pantalla de luces (la agregamos aquí para que solo se muestre si el garaje está visible)
    st.sidebar.header("Luces")
    if st.sidebar.button("Encender"):
        st.write("Luces encendidas")

# Personalizar el diseño (ejemplo)
st.write("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)
