import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título do app
st.set_page_config(page_title="Classificador de Planetas", layout="centered")
st.title("🪐 Classificador de Planetas")

# Carregar modelo
model = load_model('model/planet_model.keras')  # ou .h5 se preferir

# Classes
class_names = ['earth', 'mars', 'jupiter', 'venus', 'saturn', 'neptune', 'uranus', 'mercury']

# Upload da imagem
uploaded_file = st.file_uploader("Envie uma imagem de planeta", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Carregar imagem
    img = image.load_img(uploaded_file, target_size=(128, 128))
    st.image(img, caption='Imagem carregada')

    # Pré-processamento
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Previsão
    prediction = model.predict(img_array)[0]
    predicted_class = class_names[np.argmax(prediction)]

    # Mostrar resultado
    st.markdown(f"### 🌍 Planeta previsto: **{predicted_class}**")

    # Gráfico de barras com escala de probabilidade
    probabilities = dict(zip(class_names, prediction))
    sorted_probs = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=list(sorted_probs.values()), y=list(sorted_probs.keys()), palette='Blues_r', ax=ax)
    ax.set_title('🔭 Probabilidade por Planeta')
    ax.set_xlabel('Probabilidade')
    ax.set_xlim(0, 1)
    st.pyplot(fig)
