from os import path

import streamlit as st
from utils.components.elements import (Attribute, ListAttribute, SubAttribute,
                                       display)
from utils.components.html import h2, spacer, title
from utils.components.page import st_user
from utils.platform.user import is_superadmin
import streamlit.components.v1 as components

def show(**kwargs):

    title(st,1,"Bienvenidos!", 'home')
    spacer(1)
    st.info(
        "Data CP es un desarrollo en conjunto llevado adelante por Pablo Cerchia (Lic. en Ciencia Politica, UBA) y la Carrera de Ciencia Politica",
        icon="ℹ️",
    )
    container = st.container()
    container.write("This is inside the container")
    st.write("This is outside the container")

    # Now insert some more in the container
    container.write("This is inside too")
    spacer(0.5)
    #st.error("_Streamlit_ version: **1.27.2**", icon="🐙")
    st.divider()
    def on_button_click():
        st.write("The button was clicked!")

    # Define the HTML and CSS for the card (without the button)
    card_html = """
        <style>
            .card-container {
                border: 1px solid #eee;
                border-radius: 10px;
                padding: 2rem;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                transition: 0.3s;
                width: 80%;
                margin: auto;
                background: white;
            }
            .card-container:hover {
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            }
            .card-header {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 1rem;
            }
            .card-header-icon {
                color: #4CAF50; /* Adjust the color as needed */
                font-size: 2rem; /* Adjust the size as needed */
                margin-right: 0.5rem;
            }
            .card-title {
                font-size: 1.5rem; /* Adjust the size as needed */
                font-weight: bold;
                margin: 0;
            }
            .card-text {
                font-size: 1rem; /* Adjust the size as needed */
                color: #333; /* Adjust the text color as needed */
                margin-bottom: 1.5rem;
            }
        </style>
        <div class="card-container">
            <div class="card-header">
                <span class="material-icons card-header-icon">check_circle</span>
                <h2 class="card-title">Análisis electoral</h2>
            </div>
            <p class="card-text">Procesos electorales en la región y su relación con el liderazgo político.</p>
        </div>
    """

    # Render the card HTML in the Streamlit app
    st.markdown(card_html, unsafe_allow_html=True)

    # Add a Streamlit button styled to look like it's part of the card
    if st.button("seguir leyendo"):
        on_button_click()

    # Custom CSS to style the Streamlit button
    st.markdown("""
        <style>
            .stButton>button {
                display: block;
                width: 80%;
                padding: 0.5rem 1rem;
                border: none;
                background: #4CAF50; /* Adjust the background color as needed */
                color: white; /* Adjust the text color as needed */
                text-align: center;
                text-decoration: none;
                font-size: 1rem; /* Adjust the size as needed */
                margin: 0 auto 1.5rem auto;
                cursor: pointer;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)


def settings(**kwargs):
    title(st, 1, "Settings", "settings")
    st.info("This is where **you can change** your settings", icon="ℹ️")


def notifications(**kwargs):
    title(st, 1, "Notifications", "notifications")
    st.warning("You have **3** notifications!", icon="🔔")
