import streamlit as st
import requests

st.set_page_config(page_title="FaceVoiceID Portal", page_icon="🔐")

st.title("🔐 FaceVoiceID Biometric Gateway")
st.markdown("Multi-factor authentication system powered by facial embeddings and speaker verification.")

tab1, tab2 = st.tabs(["Authentication", "System Status"])

with tab1:
    st.subheader("Authenticate User")
    username = st.text_input("Enter Username")
    if st.button("Run Multi-Factor Auth"):
        if username:
            with st.spinner("Running biometric verification..."):
                try:
                    res = requests.post(f"http://localhost:8000/auth/{username}")
                    data = res.json()
                    if res.status_code == 200 and data.get("status") == "success":
                        st.success(f"🎉 {data.get('message')} for '{username}'!")
                    else:
                        st.error(f"❌ Authentication Failed: {data.get('detail', data.get('message'))}")
                except Exception as e:
                    st.error(f"Connection error: {e}")
        else:
            st.warning("Please enter a username.")

with tab2:
    st.subheader("API Health Check")
    if st.button("Check Service Status"):
        try:
            res = requests.get("http://localhost:8000/")
            st.json(res.json())
        except Exception as e:
            st.error(f"API is unreachable: {e}")
