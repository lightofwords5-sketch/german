# 1. التثبيت الإجباري للمكتبات (لمنع أي أعطال)
import subprocess
import sys
try:
    import groq
    import bcrypt
    from gtts import gTTS
    import plotly.express as px
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "groq", "bcrypt", "gTTS", "requests", "plotly", "pandas"])

import streamlit as st
# استدعاء باقي ملفات المشروع
from modules.ui import apply_glassmorphism, render_hero_section
from modules.auth import render_login_signup
from modules.ai_tutor import ai_tutor_page
from modules.visual_learning import visual_dictionary_page
from modules.dashboard import student_dashboard

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="German Camp AI", page_icon="🇩🇪", layout="wide")

# تطبيق التصميم الزجاجي (Glassmorphism)
apply_glassmorphism()

# تهيئة حالة المستخدم (Session State)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# نظام التوجيه (Routing)
if not st.session_state['logged_in']:
    render_hero_section()
    render_login_signup()
else:
    # القائمة الجانبية (Sidebar)
    st.sidebar.title("🇩🇪 German Camp")
    st.sidebar.markdown("---")
    menu = st.sidebar.radio(
        "القائمة الرئيسية:",
        ["📊 لوحة المتابعة (Dashboard)", "🤖 المعلم الذكي (AI Tutor)", "📚 القاموس البصري (Visual Dictionary)"]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("تسجيل الخروج (Logout)"):
        st.session_state['logged_in'] = False
        st.rerun()

    # فتح الصفحة المختارة
    if menu == "📊 لوحة المتابعة (Dashboard)":
        student_dashboard()
    elif menu == "🤖 المعلم الذكي (AI Tutor)":
        ai_tutor_page()
    elif menu == "📚 القاموس البصري (Visual Dictionary)":
        visual_dictionary_page()
