import streamlit as st

# Define el estilo CSS para el fondo
custom_css = """
<style>
body {
    background-color: #FEFAE0;
    margin: 0;
    padding: 0;
}
</style>
"""

# Inserta el estilo CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Agrega contenido básico para verificar el fondo
st.title("Prueba de Fondo")
st.write("Este es un fondo de prueba. Si ves este color, el CSS está funcionando correctamente.")
