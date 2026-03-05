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
    import streamlit as st
import json
import requests
import os

# دالة لتحميل ملف الـ Lottie من الجهاز
def load_lottie_file(filepath: str):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

# دالة لعرض الرسوم المتحركة
def render_lottie_animation(filepath: str, height=200):
    lottie_json = load_lottie_file(filepath)
    if lottie_json:
        # بنستخدم مكتبة st.lottie لو مثبتها، أو بنستخدم st.components
        try:
            from streamlit_lottie import st_lottie
            st_lottie(lottie_json, height=height, key=filepath)
        except ImportError:
            # لو مش مثبت مكتبة streamlit-lottie، بنستخدم الـ Components كحل بديل
            import streamlit.components.v1 as components
            lottie_url = f"https://assets10.lottiefiles.com/packages/{filepath.split('/')[-1]}"
            components.html(f'<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script><lottie-player src="{lottie_url}" background="transparent" speed="1" style="width: 100%; height: {height}px;" loop autoplay></lottie-player>', height=height)
    else:
        st.error(f"⚠️ ملف Lottie غير موجود: {filepath}")

# مثال: استخدامها في صفحة الـ AI Tutor
def ai_tutor_page():
    render_lottie_animation("assets/lottie/ai_robot.json", height=250)
    st.markdown('<div class="glass-card"><h2>🤖 المعلم الذكي (AI Tutor)</h2></div>', unsafe_allow_html=True)
    # باقي كود الـ AI...
