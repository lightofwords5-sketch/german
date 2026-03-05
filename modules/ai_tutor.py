import streamlit as st
from groq import Groq

def ai_tutor_page():
    st.markdown('<div class="glass-card"><h2>🤖 المعلم الألماني الذكي</h2><p>اكتب جملة بالألمانية وسأقوم بتصحيحها وشرح الأخطاء.</p></div>', unsafe_allow_html=True)
    
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        client = Groq(api_key=api_key)
    except Exception:
        st.error("⚠️ يرجى إضافة مفتاح GROQ_API_KEY في إعدادات Streamlit Secrets.")
        return

    user_text = st.text_area("أدخل النص هنا:", height=150)
    
    if st.button("صحّح لي (Korrigieren)"):
        if not user_text.strip():
            st.warning("يرجى كتابة نص أولاً.")
            return
            
        with st.spinner("المعلم يقرأ جملتك... ⏳"):
            try:
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "أنت معلم لغة ألمانية محترف. قم بتصحيح الجملة التي يكتبها المستخدم، واشرح القاعدة النحوية ببساطة باللغة العربية، ثم أعطه مثالاً إضافياً."},
                        {"role": "user", "content": user_text}
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.5,
                )
                
                feedback = response.choices[0].message.content
                st.markdown(f'<div class="glass-card"><b>التصحيح والشرح:</b><br><br>{feedback}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال بالذكاء الاصطناعي: {e}")
