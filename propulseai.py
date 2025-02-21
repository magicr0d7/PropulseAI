import streamlit as st
from pages import welcome_page, setup_profile_page, chatbot_page, settings_page

if "profile" not in st.session_state:
    st.session_state.profile = {
        "Nom": "",
        "Vision": "",
        "Mission": "",
        "Produit": "",
        "Secteur": "",
        "Fondateur": ""
    }

from preprompts import operationnel, marketing_commercial, finance

if "pre_prompts_templates" not in st.session_state:
    st.session_state.pre_prompts_templates = {
        "operationnel": operationnel,
        "marketing_commercial": marketing_commercial,
        "finance": finance
    }

if "model_selected" not in st.session_state:
    st.session_state.model_selected = "gemini-2.0-flash"

if "pre_prompts_formatted" not in st.session_state:
    st.session_state.pre_prompts_formatted = {}

if "chat_history_operational" not in st.session_state:
    st.session_state.chat_history_operational = []

if "chat_history_finance" not in st.session_state:
    st.session_state.chat_history_finance = []

if "chat_history_marketing" not in st.session_state:
    st.session_state.chat_history_marketing = []
    
if "google_api_key" not in st.session_state:
    st.session_state.google_api_key = ""


st.set_page_config(page_title="PropulseAI", layout="wide", page_icon="assets/71e43043-ac2b-480d-be90-a552442ff4f5 2.png")
st.logo("assets/Group 103199.png", size="large")

pages = {
    "Accueil": [st.Page(welcome_page, icon="🏠", title="Accueil")],
    "Profil": [st.Page(setup_profile_page, icon="👤", title="Profil")],
    "Chatbot expert": [
        st.Page(lambda: chatbot_page('operationnel'), title="Expert Opérationnel", icon="🤖", url_path="chatbot_operational"),
        st.Page(lambda: chatbot_page('finance'), title="Expert Financier", icon="💰", url_path="chatbot_finance"),
        st.Page(lambda: chatbot_page('marketing_commercial'), title="Expert Marketing & Commercial", icon="🎨", url_path="chatbot_marketing")
    ],
    "Paramètres": [st.Page(settings_page, icon="⚙️", title="Paramètres")]
}

pg = st.navigation(pages)
pg.run()
    