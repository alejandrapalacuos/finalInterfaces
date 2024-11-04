import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

import platform


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
        model = load_model('keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        st.title("Reconocimiento de Imágenes")
        #st.write("Versión de Python:", platform.python_version())
        image = Image.open('OIG5.jpg')
        st.image(image, width=350)
        with st.sidebar:
            st.subheader("Usando un modelo entrenado en teachable Machine puedes Usarlo en esta app para identificar")
        img_file_buffer = st.camera_input("Toma una Foto")

        if img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
           #To read image file buffer as a PIL Image:
            img = Image.open(img_file_buffer)

            newsize = (224, 224)
            img = img.resize(newsize)
            # To convert PIL Image to numpy array:
            img_array = np.array(img)

            # Normalize the image
            normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)
            print(prediction)
            if prediction[0][0]>0.5:
              st.header('Izquierda, con Probabilidad: '+str( prediction[0][0]) )
            if prediction[0][1]>0.5:
              st.header('Arriba, con Probabilidad: '+str( prediction[0][1]))
            #if prediction[0][2]>0.5:
            # st.header('Derecha, con Probabilidad: '+str( prediction[0][2]))
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
