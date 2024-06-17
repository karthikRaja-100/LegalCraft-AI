import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import tempfile
import inflect
from datetime import datetime
from fpdf import FPDF
import base64


def parse_date(date_str):
    try:

        date = datetime.strptime(date_str, "%d/%m/%Y")
        return date
    except ValueError:
        return None
def generate_agreement(date, owner_name, owner_father_name,
                             receiver_name,receiver_father_name,product,amount,years):
   

    # Create a PDF document
   


    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)


    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.spaceAfter = 12
    normal_style.leading = 14


    p = inflect.engine()


    amount_words = f"{p.number_to_words(amount)} Rupees" if amount is not None else "N/A"
    

    content = []


    sections = [

        f"DRAFT OF LICENSE TO USE COPYRIGHT AGREEMENT",
f"",
f"I {owner_name}.s/d/o{owner_father_name}., the owner of the copyright of {product}, to", f"Award the LICENCE to {receiver_name}s/or/d{receiver_father_name}for using the said for the",
f"purpose of for a period of {years} years in lieu of the consideration of {amount} already", f"paid to me on {date}, and I hereby acknowledge the receipt of said amount.",
f"",
f"Date.{date}",     

    ]

    for section_text in sections:
        section = Paragraph(section_text, normal_style)
        content.append(section)


    doc.build(content)


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_buffer.getvalue())


    temp_pdf_path = temp_pdf.name
    return temp_pdf_path



   
        
    

   

   

    
    


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{bin_file}">{file_label}</a>'
    return href
    


st.set_page_config(
    page_title="Copyright Agreement Template",
    page_icon="📝"
)
st.header("Copyright Agreement Template")

with st.form("copyright_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    owner_name=st.text_input("Owner Name", placeholder="Enter the owner's name.")
    owner_father_name=st.text_input("Owner Father Name", placeholder="Enter the owner's father name.")
    receiver_name=st.text_input("Receiver Name", placeholder="Enter the receiver's name.")
    receiver_father_name=st.text_input("Receiver Father Name", placeholder="Enter the receiver's father name.")
    product=st.text_input("Product Name", placeholder="Enter the product's name.")
    amount=st.number_input("Amount", value=None,placeholder="Enter the amount.")
    years=st.slider('Number of years', 1, 10, 1)
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_agreement)
        path_name=generate_agreement(date, owner_name, owner_father_name,
                             receiver_name,receiver_father_name,product,amount,years)
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
