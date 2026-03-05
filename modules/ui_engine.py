import streamlit as st
import os

def apply_custom_assets():
    # 1. Inject Glassmorphism CSS from External File
    css_path = "assets/css/style.css"
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # 2. Inject Interaction JS from External File
    js_path = "assets/js/script.js"
    if os.path.exists(js_path):
        with open(js_path, "r") as f:
            st.components.v1.html(f"<script>{f.read()}</script>", height=0)

def render_hero():
    st.markdown("""
        <div class='hero-container'>
            <h1>Willkommen bei German Camp 🇩🇪</h1>
            <p>Master German with AI-powered Visual & Audio learning.</p>
        </div>
    """, unsafe_allow_html=True)
