import streamlit as st

def apply_glassmorphism():
    st.markdown("""
    <style>
    /* خلفية الموقع المتدرجة */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    
    /* التصميم الزجاجي للكروت */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        color: white;
    }
    
    /* تجميل الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(229, 46, 113, 0.5);
    }
    
    /* نصوص الإدخال */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def render_hero_section():
    st.markdown("""
    <div style='text-align: center; padding: 50px 0;'>
        <h1 style='font-size: 3em; color: #ff8a00;'>Willkommen bei German Camp 🇩🇪</h1>
        <p style='font-size: 1.2em; color: #ccc;'>تعلم الألمانية بذكاء، تفاعل مع المعلم الآلي، واستمع للنطق الصحيح.</p>
    </div>
    """, unsafe_allow_html=True)
