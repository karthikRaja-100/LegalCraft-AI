import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="LegalCraft",
    page_icon="⚖️"
)



st.title("LegalCraft-AI Powered Tool to ease Legal Documentation Process.") 

st.header("Choose our services")
st.page_link("pages/Document_Creator.py", label="Document Creator", icon="📝")
st.page_link("pages/Legal_Doubt_Resolver.py", label="Legal Doubt Resolver", icon="🤖")
st.page_link("pages/Legal_Summarizer.py", label="Legal Summarizer", icon="📝")
st.page_link("pages/Legal_Assistant_Chatbot.py", label="Legal Assistant Chatbot", icon="🤖")

