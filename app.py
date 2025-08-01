import streamlit as st
import requests

API_URL = "https://back-079x.onrender.com/analyze"  # Met ici l’URL de ton backend

st.title("🔍 Analyse annonce immobilière")

uploaded_file = st.file_uploader("Déposez un fichier (PDF, image, HTML, ZIP)", type=["pdf", "jpg", "jpeg", "png", "html", "zip"])

if uploaded_file:
    if st.button("Analyser le fichier"):
        files = {
            "file": (uploaded_file.name, uploaded_file, uploaded_file.type)
        }
        with st.spinner("Analyse en cours..."):
            try:
                response = requests.post(API_URL, files=files)
                if response.ok:
                    st.success("✅ Analyse terminée")
                    st.json(response.json())
                else:
                    st.error(f"❌ Erreur {response.status_code} : {response.text}")
            except Exception as e:
                st.error(f"❌ Erreur réseau ou serveur : {e}")
