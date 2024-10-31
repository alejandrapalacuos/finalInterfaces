import streamlit as st
from modules import garage_control, gesture_recognition, voice_control
from streamlit_webrtc import webrtc_streamer
import threading

st.title("Automatización del Hogar")

# Botón para reconocimiento de gestos y abrir garaje
if st.button("Abrir Garaje (Reconocimiento de Gestos)"):
    threading.Thread(target=gesture_recognition.recognize_gesture).start()

# Botón para cerrar garaje
if st.button("Cerrar Garaje"):
    garage_control.close_garage()

# Botón para encender luces con comando de voz
if st.button("Encender Luces (Reconocimiento de Voz)"):
    threading.Thread(target=voice_control.listen_for_lights_command).start()
