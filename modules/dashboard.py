import streamlit as st
import plotly.express as px
import pandas as pd

def student_dashboard():
    st.markdown('<div class="glass-card"><h2>📊 مستوى تقدمك (Dein Fortschritt)</h2></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="الكلمات المكتسبة", value="120 كلمة", delta="+15 هذا الأسبوع")
    col2.metric(label="الدروس المكتملة", value="8 دروس", delta="+2")
    col3.metric(label="أيام التفاعل المتتالية", value="5 أيام", delta="استمر!")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # رسم بياني تفاعلي يوضح مهارات الطالب
    df = pd.DataFrame(dict(
        المهارة=['القواعد (Grammatik)', 'المفردات (Wortschatz)', 'الاستماع (Hören)', 'القراءة (Lesen)', 'التحدث (Sprechen)'],
        المستوى=[70, 85, 60, 90, 50]
    ))
    
    fig = px.line_polar(df, r='المستوى', theta='المهارة', line_close=True, 
                        template="plotly_dark", title="تحليل المهارات اللغوية")
    fig.update_traces(fill='toself', line_color='#e52e71')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    st.plotly_chart(fig, use_container_width=True)
