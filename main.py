import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Cargar el modelo
model = load_model('keras_model.h5')

# Preparar una nueva imagen (ajustar el tamaño y preprocesamiento según tu modelo)
img = Image.open('nueva_imagen.jpg')
img = img.resize((224, 224))  # Suponiendo que el modelo espera imágenes de 224x224
img_array = np.array(img) / 255.0  # Normalizar los valores de píxel
img_array = np.expand_dims(img_array, axis=0)  # Agregar un eje para representar un batch

# Realizar la predicción
prediction = model.predict(img_array)

# Obtener la clase predicha
class_index = np.argmax(prediction)
classes = ['gato', 'perro']  # Lista de clases
print('Predicción:', classes[class_index])
