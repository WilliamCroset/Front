import streamlit as st
import requests
import base64
import json

API_URL = "https://back-079x.onrender.com/analyze"  # ⛔️ À adapter à ton backend

st.title("🔍 Analyse intelligente d’annonce immobilière")

st.markdown("### 📥 Choisissez une méthode d'entrée")

input_mode = st.radio("Type d’entrée", ["Fichier", "Texte libre", "Lien URL"])

if input_mode == "Fichier":
    uploaded_file = st.file_uploader("Déposez un fichier (PDF, image, HTML, ZIP)", type=["pdf", "jpg", "jpeg", "png", "html", "zip"])
    if uploaded_file and st.button("Analyser"):
        # Encodage du fichier en base64
        file_content = uploaded_file.read()
        encoded_file = base64.b64encode(file_content).decode("utf-8")

        response = requests.post(API_URL, json={
            "input_type": "file",
            "filename": uploaded_file.name,
            "content_base64": encoded_file
        })

        if response.ok:
            result = response.json()
            st.success("✅ Analyse terminée")
            st.json(result)
        else:
            st.error(f"❌ Erreur : {response.status_code} - {response.text}")

elif input_mode == "Texte libre":
    texte = st.text_area("Copiez-collez une annonce immobilière ici", height=300)
    if texte and st.button("Analyser"):
        response = requests.post(API_URL, json={
            "input_type": "text",
            "text": texte
        })
        if response.ok:
            result = response.json()
            st.success("✅ Analyse terminée")
            st.json(result)
        else:
            st.error(f"❌ Erreur : {response.status_code} - {response.text}")

elif input_mode == "Lien URL":
    url = st.text_input("Collez ici l’URL d’une annonce immobilière")
    if url and st.button("Analyser"):
        response = requests.post(API_URL, json={
            "input_type": "url",
            "url": url
        })
        if response.ok:
            result = response.json()
            st.success("✅ Analyse terminée")
            st.json(result)
        else:
            st.error(f"❌ Erreur : {response.status_code} - {response.text}")
