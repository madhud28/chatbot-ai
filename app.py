
import streamlit as st
st.title("AI Chatbot")
user = st.text_input("Ask me something")
if st.button("Send"):
    if user.strip():
        st.success(f"You entered: {user}")
    else:
        st.warning("error")

