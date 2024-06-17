import streamlit as st


st.title("LegalCraft-Legal Document Creator")

st.header("Choose any template")

template_name=st.selectbox(
    'Template Category',
    ("Rental Agreement", "House Sale Agreement", "Loan Agreement","Simple Mortage","Will Draft","Copyright Agreement","Compromise Agreement")) 
if(template_name=="Rental Agreement"):
    st.write("Click Here")
    st.page_link("pages/Rental_Agreement_Template.py", label="Rental Agreement", icon="📝")
if(template_name=="House Sale Agreement"):
    st.write("Click Here")
    st.page_link("pages/House_Sale_Agreement_Template.py", label="House Sale Agreement", icon="📝")
if(template_name=="Loan Agreement"):
    st.write("Click Here")
    st.page_link("pages/Loan_Agreement_Template.py", label="Loan Agreement", icon="📝")
if(template_name=="Simple Mortage"):
    st.write("Click Here")
    st.page_link("pages/Simple_Mortage_Template.py", label="Simple Mortage", icon="📝")
if(template_name=="Will Draft"):
    st.write("Click Here")
    st.page_link("pages/Will_Draft_Template.py", label="Will Draft", icon="📝")
if(template_name=="Copyright Agreement"):
    st.write("Click Here")
    st.page_link("pages/Copyright_Agreement_Template.py", label="Copyright Agreement", icon="📝")
if(template_name=="Compromise Agreement"):
    st.write("Click Here")
    st.page_link("pages/Compromise_Agreement_Template.py", label="Compromise Agreement", icon="📝")    