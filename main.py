import streamlit as st
# Cargar la imagen
background_img = st.image("fondo.jpg")

# Aplicar la imagen como fondo (CSS)
st.markdown("""
<style>
.stApp {
  background-image: url("fondo.jpg");
  background-size: cover;
}
</style>
""", unsafe_allow_html=True)



def pagina_inicio():
    st.title("Bienvenido a HomeDrive")
    if st.button("Empezar"):
        st.session_state.pagina_actual = "elegir_accion"

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
    if st.button("Volver"):
        st.session_state.pagina_actual = "elegir_accion"

def pagina_luces():
    st.title("Control de Luces")
    if st.button("Encender"):
        st.write("Luces encendidas")
    if st.button("Apagar"):
        st.write("Luces apagadas")
    if st.button("Volver"):
        st.session_state.pagina_actual = "elegir_accion"

if __name__ == "__main__":
    main()
