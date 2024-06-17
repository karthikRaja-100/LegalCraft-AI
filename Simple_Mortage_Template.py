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
def generate_agreement(date, candidate_name, 
                              candidate_father_name,partner_name,no_of_child,child_names,executor_name,address,property_address,age,location):
   

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

       f"DRAFT OF WILL",
f"",
f"I, {candidate_name} son/daughter of Shri {candidate_father_name}, aged {age} years, resident of {address}, do hereby revoke all my former Wills, Codicils,", f"and Testamentary dispositions made by me. I declare this to be my last will.",
f"I maintain good health and possess a sound mind. This Will is made by me of my own independent decision and free volition. Have not been influenced,", f"cajoled, or coerced in any manner whatsoever.",
f"I hereby appoint my {executor_name}, as the sole Executor of this WILL.",
f"The name of my partner is {partner_name}. We have {no_of_child} children namely, {child_names}, I own the following immovable and movable assets.",
f"1.     {property_address}",
f"2.     Jewellery, ornaments, cash, National Saving Certificate, Public Provident Fund, shares in various companies, cash in hand, and also with certain banks.",
f"All the assets owned by me are self-acquired properties. No one else has any right, title, interest, claim, or demand whatsoever on these assets or", f"properties. I have full right, absolute power, and complete authority on these assets, or in any other property which may be substituted in their place or", f"places which may be Acquired or received by me hereafter.",
f"I hereby give, devise, and bequeath all my properties, whether movable or immovable, whatsoever and wheresoever to my partner 6, absolutely forever.",
f"IN WITNESS WHEREOF I have hereunto set my hands on this {date}at {location}.",
f"",
f"TESTATRIX",
f"SIGNED by the above-named Testatrix as his last will in our presence, who appear to have perfectly understood & approved the contents in the presence of", f"both of us presents, at the same time who in his presence and the presence of each other have hereunto subscribed our names as Witnesses.",
f"WITNESSES:",
f"1.",
f"2.",
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
    page_title="Will Draft Template",
    page_icon="📝"
)
st.header("Will Draft Template")

with st.form("rent_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    mortagagor_name=st.text_input("Mortagagor Name", placeholder="Enter the mortgagor's name.")
    mortagagor_father_name=st.text_input("Mortagagor Father Name", placeholder="Enter the mortagagor's father name.")
    mortagagor_address=st.text_input("Mortagagor Address", placeholder="Enter the mortagagor address.")
    mortagagee_name=st.text_input("Mortagagee Name", placeholder="Enter the mortgagee's name.")
    mortagagee_father_name=st.text_input("Mortagagee Father Name", placeholder="Enter the mortagagee's father name.")
    mortagagee_address=st.text_input("Mortagagee Address", placeholder="Enter the mortagagee address.")
    street_name=st.text_input("Street Name", placeholder="Enter the street's name.")
    house_number=st.text_input("House Number",placeholder="Enter the house number.")
    property_city=st.text_input("Property Address", placeholder="Enter the property address.")
    child_names=st.text_input("Children Names", placeholder="Enter the children names.")
    executor_name=st.text_input("Executor Name", placeholder="Enter the executor's name.")
    no_of_child=st.text_input("Number of children", value=None,placeholder="Enter the amount.")
    
    
    age=st.text_input("Age", placeholder="Enter the age")
    location=st.text_input("Location", placeholder="Enter the location")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_agreement)
        path_name=generate_agreement(date, candidate_name, 
                              candidate_father_name,partner_name,no_of_child,child_names,executor_name,address,property_address,age,location)
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
