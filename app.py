import streamlit as st
import requests

st.set_page_config(page_title="Analyse Multi-Support", layout="centered")

st.title("🔍 Analyse multi-support (HTML, Image, Texte, etc.)")

uploaded_file = st.file_uploader("Uploader un fichier (image, HTML, texte, etc.)", type=["png", "jpg", "jpeg", "html", "txt", "pdf"])

if uploaded_file is not None:
    st.info("Fichier chargé : " + uploaded_file.name)

    # Envoi du fichier au backend FastAPI
    with st.spinner("Analyse en cours..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        try:
            response = requests.post("https://back-079x.onrender.com/analyze", files=files)
            response.raise_for_status()
            result = response.json()
            st.success("Analyse terminée ✅")
            st.json(result)
        except Exception as e:
            st.error(f"Erreur lors de l'envoi au serveur : {e}")
else:
    st.warning("Veuillez uploader un fichier à analyser.")
