import streamlit as st
import google.generativeai as genai
import time

def welcome_page():
    # Explication détaillée de l'application et de son fonctionnement
    st.title("Bienvenue dans l'application PropulseAI")
    
    st.write("""
    **PropulseAI** est une plateforme intelligente dédiée aux petites entreprises et aux entrepreneurs. Elle utilise l'intelligence artificielle pour fournir des conseils experts dans les domaines clés de l'entreprise, comme l'opérationnel, la finance, et le marketing. 

    ### Fonctionnement de l'application :
    Cette application est conçue pour vous guider tout au long du parcours de votre entreprise, en vous offrant des outils et des conseils adaptés à votre profil. Vous pourrez interagir avec des **chatbots experts** dans divers domaines pour poser vos questions et obtenir des recommandations personnalisées.

    ### Composants principaux de l'application :
    
    1. **Page de présentation de l'application**  
       Sur cette page, vous trouverez une introduction générale sur PropulseAI et son objectif : vous aider à faire croître votre entreprise grâce à l'IA.

    2. **Page de définition du profil de l'entreprise**  
       Ici, vous définissez votre profil d'entreprise en renseignant des informations essentielles comme la vision, la mission, la taille de votre entreprise et plus encore. Ces informations seront utilisées pour personnaliser les conseils des chatbots et rendre l'expérience plus adaptée à vos besoins.

    3. **Page de chatbot**  
       Sur cette page, vous pouvez interagir directement avec les experts virtuels dans des domaines spécifiques :
       - **Expert Opérationnel** : Pour des conseils sur la gestion quotidienne de l'entreprise.
       - **Expert Finance** : Pour des stratégies et des conseils financiers adaptés.
       - **Expert Marketing et Commerciale** : Pour des recommandations sur la croissance de votre entreprise, la stratégie marketing et la vente.

    Vous pouvez naviguer entre ces différentes pages en utilisant le menu situé en haut de l'écran. 
    """)

    st.write("### Comment ça marche ?")
    st.write("""
    - **Définissez votre profil :** Renseignez les informations sur votre entreprise dans la page dédiée. Ces informations permettront à l'IA de mieux comprendre votre situation.
    - **Posez des questions à nos experts :** Une fois votre profil défini, vous pouvez poser des questions à nos chatbots experts. Ces derniers utiliseront votre profil pour vous fournir des réponses personnalisées.
    - **Obtenez des conseils stratégiques :** Les conseils fournis seront adaptés à votre secteur d'activité, à vos objectifs, à la taille de votre entreprise, et bien plus encore.
    
    **Astuce :** Plus vous renseignez de détails dans votre profil, plus les conseils que vous recevrez seront pertinents et personnalisés.
    """)

    st.write("### Pourquoi utiliser PropulseAI ?")
    st.write("""
    - **Gagner du temps :** Pas besoin de chercher des informations partout, PropulseAI centralise les conseils d'experts en un seul endroit.
    - **Conseils sur-mesure :** L'intelligence artificielle adapte ses recommandations en fonction de votre entreprise et de vos besoins spécifiques.
    - **Accéder à des experts sans coût élevé :** Profitez de l'expertise d'AI dans les domaines essentiels pour les entrepreneurs, sans avoir à engager un consultant coûteux.
    """)

    st.write("### Prêt à commencer ?")
    st.write("Cliquez sur les différentes pages du menu pour commencer à définir votre profil d'entreprise, poser vos questions à nos experts et bien plus encore !")



def setup_profile_page():
    # Page de définition du profil de l'entreprise
    st.title("Définition du profil de l'entreprise")
    st.write("Cette page vous permet de définir le profil de l'entreprise.")

    with st.form(key="profil_form"):
        # Champs basiques
        nom_entreprise = st.text_input("Nom de l'entreprise", value=st.session_state.profile.get("Nom", ""))

        col1, col2 = st.columns(2)
        with col1:
            vision = st.text_area("Vision de l'entreprise", value=st.session_state.profile.get("Vision", ""))
        with col2:
            mission = st.text_area("Mission de l'entreprise", value=st.session_state.profile.get("Mission", ""))

        description_produit = st.text_area("Description du produit/service", value=st.session_state.profile.get("Produit", ""))
        secteur = st.text_input("Secteur d'activité", value=st.session_state.profile.get("Secteur", ""))
        fondateur = st.text_input("Nom du fondateur", value=st.session_state.profile.get("Fondateur", ""))

        st.markdown("---")
        st.markdown("### Informations supplémentaires")

        # Exemples de nouveaux champs
        taille_entreprise = st.selectbox(
            "Taille de l'entreprise (nb. d'employés)",
            ["1-5", "6-10", "11-50", "51-100", "100+"],
            index=0
        )

        stade_de_dev = st.selectbox(
            "Stade de développement de l'entreprise",
            ["Idée", "Lancement", "Croissance", "Établie", "Expansion internationale"],
            index=0
        )

        marche_cible = st.text_area(
            "Marché cible (géographie, type de clients...)",
            value=st.session_state.profile.get("MarcheCible", "")
        )

        valeur_unique = st.text_area(
            "Proposition de valeur unique",
            value=st.session_state.profile.get("ValeurUnique", "")
        )

        concurrents_principaux = st.text_area(
            "Concurrents principaux",
            value=st.session_state.profile.get("ConcurrentsPrincipaux", "")
        )

        principaux_objectifs = st.text_area(
            "Principaux objectifs (6 mois, 1 an, 5 ans)",
            value=st.session_state.profile.get("PrincipauxObjectifs", "")
        )

        defis_cles = st.text_area(
            "Défis clés / points de douleur",
            value=st.session_state.profile.get("DefisCles", "")
        )

        # Soumission du formulaire
        submit = st.form_submit_button("Enregistrer le profil")

        if submit:
            st.session_state.profile = {
                "Nom": nom_entreprise,
                "Vision": vision,
                "Mission": mission,
                "Produit": description_produit,
                "Secteur": secteur,
                "Fondateur": fondateur,
                "TailleEntreprise": taille_entreprise,
                "StadeDev": stade_de_dev,
                "MarcheCible": marche_cible,
                "ValeurUnique": valeur_unique,
                "ConcurrentsPrincipaux": concurrents_principaux,
                "PrincipauxObjectifs": principaux_objectifs,
                "DefisCles": defis_cles
            }

            # Met à jour les pré-prompts en insérant les nouvelles données
            for prompt_type, template in st.session_state.pre_prompts_templates.items():
                st.session_state.pre_prompts_formatted[prompt_type] = template.format(
                    nom=nom_entreprise,
                    secteur=secteur,
                    produit=description_produit,
                    vision=vision,
                    mission=mission,
                    taille_entreprise=taille_entreprise,
                    stade_de_dev=stade_de_dev,
                    marche_cible=marche_cible,
                    valeur_unique=valeur_unique,
                    concurrents_principaux=concurrents_principaux,
                    principaux_objectifs=principaux_objectifs,
                    defis_cles=defis_cles
                )

            st.success("Profil et pré-prompts mis à jour avec succès.")
            st.json(st.session_state.pre_prompts_formatted)
      
def call_gemini(query, pre_prompt, chat_history, profile):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat()
        
        # Envoyer le pré-prompt comme message système
        if pre_prompt:
            system_message = {
                "role": "system",
                "content": pre_prompt
            }
            chat.send_message(system_message["content"])
        
        # Envoyer l'historique avec les rôles appropriés
        for msg in chat_history:
            chat.send_message(msg["content"])
        
        # Envoyer la nouvelle question
        response = chat.send_message(query)
        print(chat)
        return response.text 
        
    except Exception as e:
        st.error(f"Erreur lors de l'appel à Gemini: {e}")
        return None
    
def chatbot_page(chatbot_type):
    st.title(f"Expert {chatbot_type.capitalize()}")
    pre_prompt = st.session_state.pre_prompts_formatted.get(chatbot_type, "")
    st.text(pre_prompt)
    chat_history_key = f"chat_history_{chatbot_type}"
    if chat_history_key not in st.session_state:
        st.session_state[chat_history_key] = []
    chat_history = st.session_state[chat_history_key]

    # Afficher l'historique des messages
    for message in chat_history:
        st.chat_message(message["role"]).write(message["content"])

    # Utilisation de st.chat_input pour saisir la question
    user_input = st.chat_input("Posez votre question", key=f"chat_input_{chatbot_type}")
    if user_input:
        st.chat_message("user").write(user_input)
        
        # Créer un message assistant pour le streaming
        assistant_message = st.chat_message("assistant")
        
        def stream_response():
            answer = call_gemini(user_input, pre_prompt, chat_history, st.session_state.profile)
            if answer:
                # Simuler un streaming mot par mot
                for word in answer.split():
                    yield word + " "
                    time.sleep(0.02)
                
                # Enregistrer la question et la réponse dans l'historique
                chat_history.append({"role": "user", "content": user_input})
                chat_history.append({"role": "assistant", "content": answer})
        
        # Utiliser write_stream pour afficher la réponse
        assistant_message.write_stream(stream_response)

        
def settings_page():
    st.title("Paramètres")
    st.write("Cette page vous permet de configurer les paramètres de l'application.")
    
    # Section API Key
    st.header("Configuration de l'API")
    google_api_key = st.text_input("Clé API Google", type="password", value=st.session_state.google_api_key)
    if st.button("Enregistrer la clé API"):
        if google_api_key:
            genai.configure(api_key=google_api_key)
            st.session_state.google_api_key = google_api_key
            st.success("Clé API enregistrée avec succès.")
        else:
            st.error("Veuillez entrer une clé API valide.")

    # Section Templates des pré-prompts
    st.header("Templates des pré-prompts")
    with st.form(key="templates_form"):
        chatbot_types = ["operationnel", "marketing_commercial", "finance"]
        for chatbot_type in chatbot_types:
            if chatbot_type in st.session_state.pre_prompts_templates:
                template = st.session_state.pre_prompts_templates[chatbot_type]
                st.text_area(
                    f"Template pour l'expert {chatbot_type.capitalize()}", 
                    value=template,
                    height=200,
                    key=f"template_{chatbot_type}"
                )
        
        if st.form_submit_button("Enregistrer les templates"):
            for chatbot_type in chatbot_types:
                template_value = st.session_state[f"template_{chatbot_type}"]
                st.session_state.pre_prompts_templates[chatbot_type] = template_value
                
                # Mettre à jour les prompts formatés avec les nouvelles templates
                try:
                    st.session_state.pre_prompts_formatted[chatbot_type] = template_value.format(
                        nom=st.session_state.profile.get("Nom", ""),
                        secteur=st.session_state.profile.get("Secteur", ""),
                        produit=st.session_state.profile.get("Produit", ""),
                        vision=st.session_state.profile.get("Vision", ""),
                        mission=st.session_state.profile.get("Mission", "")
                    )
                except Exception as e:
                    st.error(f"Erreur de formatage pour {chatbot_type}: {str(e)}")
                    continue
                
            st.success("Templates et pré-prompts mis à jour avec succès.")

    # Section Pré-prompts formatés actuels
    st.header("Pré-prompts formatés actuels")
    for chatbot_type in chatbot_types:
        if chatbot_type in st.session_state.pre_prompts_formatted:
            st.subheader(f"Expert {chatbot_type.capitalize()}")
            st.text_area(
                "Pré-prompt formaté",
                value=st.session_state.pre_prompts_formatted[chatbot_type],
                height=150,
                key=f"formatted_{chatbot_type}",
                disabled=True
            )

    # Section Réinitialisation
    st.header("Gestion de l'historique")
    if st.button("Réinitialiser l'historique des conversations"):
        st.session_state.chat_history_operational = []
        st.session_state.chat_history_finance = []
        st.session_state.chat_history_marketing = []
        st.success("L'historique des conversations a été réinitialisé.")