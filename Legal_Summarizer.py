import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")

@st.cache_resource
def text_summary(text, maxlength=None):
    #create summary instance
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text



st.subheader("LegalCraft-Legal Summarizer")
input_file = st.file_uploader("Upload your document here", type=['pdf'])
if input_file is not None:
    if st.button("Summarize Document"):
        with open("doc_file.pdf", "wb") as f:
            f.write(input_file.getbuffer())
        col1, col2 = st.columns([1,1])
        with col1:
            st.info("File uploaded successfully")
            extracted_text = extract_text_from_pdf("doc_file.pdf")
            st.markdown("**Extracted Text is Below:**")
            st.info(extracted_text)
        with col2:
            st.markdown("**Summary Result**")
            text = extract_text_from_pdf("doc_file.pdf")
            doc_summary = text_summary(text)
            st.success(doc_summary)
                