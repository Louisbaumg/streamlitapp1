import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title('Application Streamlit de Démonstration')

# Afficher un message de bienvenue
st.write("Bienvenue dans cette simple application Streamlit!")

# Entrée utilisateur pour générer des données
user_input = st.slider('Combien de points de données voulez-vous générer?', min_value=10, max_value=1000, value=100)

# Générer des données aléatoires
data = pd.DataFrame({
  'x': range(user_input),
  'y': np.random.randn(user_input).cumsum()
})

# Créer un graphique de ligne simple
st.line_chart(data)

# Interactivité : champ de texte pour saisir un message
user_message = st.text_input('Entrez un message que vous souhaitez afficher :')
if st.button('Afficher le Message'):
    st.write(user_message)

