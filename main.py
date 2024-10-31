import streamlit as st

st.title("Bienvenido a HomeDrive")

if st.button("Empezar"):
    st.sidebar.title("Controles")
    
    # Pantalla de garaje
    st.sidebar.header("Garaje")
    if st.sidebar.button("Abrir"):
        st.write("Garaje abierto")
    if st.sidebar.button("Cerrar"):
        st.write("Garaje cerrado")
    
    # Pantalla de luces
    st.sidebar.header("Luces")
    if st.sidebar.button("Encender"):
        st.write("Luces encendidas")

# Personalizar el diseño (ejemplo)
st.write("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)
