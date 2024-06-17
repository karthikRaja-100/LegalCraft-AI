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
def generate_agreement(date,city, party_one, party_one_father_name,party_one_address
                             ,party_two, party_two_father_name,party_two_address,dispute,rule_1,rule_2):
   

    # Create a PDF document
   


    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)


    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.spaceAfter = 12
    normal_style.leading = 14


    p = inflect.engine()


    
    

    content = []


    sections = [

        f"Draft of Simple Compromise Agreement",
f"",
f"This Agreement of compromise made at {city} on this {date} between {party_one} son/daughter of {party_one_father_name} resident of {party_one_address} (hereinafter called Party No. 1) of the", 
f"One Part and {party_two} son/daughter of {party_two_father_name} resident of {party_two_address} (hereinafter called Party No. 2) of the Other Part.",
f"WHEREAS, disputes and differences have arisen between the parties aforementioned regarding {dispute}.",
f"",
f"AND WHEREAS, the parties have agreed to settle their disputes and differences amicably between themselves without recourse to litigation and for that purpose are willing to abandon their",
f"claims in the manner hereinafter appearing.",

f"NOW, this Deed Witnesseth That It Is Hereby Agreed As Follows:",
f"",
f"1.{rule_1}",
f"",
f"2.{rule_2}",
f"",
f"IN WITNESS WHEREOF, the parties have hereunto set and subscribed their respective hands, the day, month and year first above written.",
f"",
f"Signed and delivered by the Withinnamed {party_one}",
f"",
f"Witnesses",
f"",
f"1.",
f"",
f"2.",
f"",
f"Signed and delivered by the Withinnamed {party_two}",
  

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
    page_title="Compromise Agreement Template",
    page_icon="📝"
)
st.header("Compromise Agreement Template")

with st.form("copyright_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    city=st.text_input("City", placeholder="Enter the city.")
    party_one=st.text_input("Party one name", placeholder="Enter the party one's name.")
    party_one_father_name=st.text_input("Party one Father Name", placeholder="Enter the party one's father name.")
    party_one_address=st.text_input("Party one address",placeholder="Enter the party one's address.")
    party_two=st.text_input("Party two name", placeholder="Enter the party two's name.")
    party_two_father_name=st.text_input("Party two Father Name", placeholder="Enter the party two's father name.")
    party_two_address=st.text_input("Party two address",placeholder="Enter the party two's address.")
    dispute=st.text_input("Dispute", placeholder="Enter the dispute.")
    rule_1=st.text_input("Term 1", placeholder="Enter the term.")
    rule_2=st.text_input("Term 2", placeholder="Enter the term.")
    
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_agreement)
        path_name=generate_agreement(date,city, party_one, party_one_father_name,party_one_address
                             ,party_two, party_two_father_name,party_two_address,dispute,rule_1,rule_2)
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
