import streamlit as st
import bcrypt

# قاعدة بيانات وهمية للتجربة (في الواقع تستخدم قواعد بيانات حقيقية)
if 'users_db' not in st.session_state:
    # حساب افتراضي: test / test
    hashed_pw = bcrypt.hashpw("test".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    st.session_state['users_db'] = {"test": hashed_pw}

def render_login_signup():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["تسجيل الدخول (Login)", "حساب جديد (Sign Up)"])
        
        with tab1:
            username = st.text_input("اسم المستخدم", key="login_user")
            password = st.text_input("كلمة المرور", type="password", key="login_pass")
            if st.button("دخول", key="login_btn", use_container_width=True):
                db = st.session_state['users_db']
                if username in db and bcrypt.checkpw(password.encode('utf-8'), db[username].encode('utf-8')):
                    st.session_state['logged_in'] = True
                    st.success("تم تسجيل الدخول بنجاح!")
                    st.rerun()
                else:
                    st.error("بيانات الدخول غير صحيحة.")
                    
        with tab2:
            new_user = st.text_input("اسم مستخدم جديد", key="reg_user")
            new_pass = st.text_input("كلمة مرور جديدة", type="password", key="reg_pass")
            if st.button("إنشاء حساب", key="reg_btn", use_container_width=True):
                if new_user in st.session_state['users_db']:
                    st.warning("اسم المستخدم موجود بالفعل.")
                elif len(new_pass) < 4:
                    st.warning("كلمة المرور قصيرة جداً.")
                else:
                    hashed = bcrypt.hashpw(new_pass.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    st.session_state['users_db'][new_user] = hashed
                    st.success("تم إنشاء الحساب! يمكنك الآن تسجيل الدخول.")
        st.markdown('</div>', unsafe_allow_html=True)
