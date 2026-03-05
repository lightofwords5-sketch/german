import streamlit as st
from gtts import gTTS
import io

def visual_dictionary_page():
    st.markdown('<div class="glass-card"><h2>📚 القاموس البصري الصوتي</h2><p>ابحث عن أي كلمة ألمانية لترى صورتها وتسمع نطقها الصحيح.</p></div>', unsafe_allow_html=True)
    
    word = st.text_input("اكتب كلمة ألمانية (مثال: Hund, Apfel, Haus):")
    
    if st.button("ابحث (Suchen)") and word:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### الصورة (Bild)")
            # نستخدم موقع Unsplash Source لجلب صورة تعبر عن الكلمة
            image_url = f"https://source.unsplash.com/400x400/?{word}"
            st.image(image_url, caption=word.capitalize(), use_container_width=True)
            
        with col2:
            st.markdown(f"### النطق (Aussprache)")
            st.info(f"الكلمة: **{word.capitalize()}**")
            
            with st.spinner("توليد الصوت..."):
                try:
                    # توليد الصوت بالألمانية
                    tts = gTTS(text=word, lang='de')
                    audio_bytes = io.BytesIO()
                    tts.write_to_fp(audio_bytes)
                    st.audio(audio_bytes, format='audio/mp3')
                    st.success("اضغط على زر التشغيل لسماع النطق 🔊")
                except Exception as e:
                    st.error(f"حدث خطأ في توليد الصوت: {e}")
