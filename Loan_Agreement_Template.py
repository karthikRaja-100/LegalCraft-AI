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
def generate_agreement(date, lender_name, 
                              borrower_name,amount,starting_date,ending_date,city,years):
   

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

        f"DRAFT OF LOAN AGREEMENT ",

f"",
f"LOAN AGREEMENT BETWEEN",
f"{lender_name}",
f"AND", 
f"{borrower_name}",

f"THIS AGREEMENT made and entered into at {city} this {date} BETWEEN {lender_name}", 
f"hereinafter called the Lender AND {borrower_name} hereinafter called the Borrower and",
f"and reference to the parties hereto shall mean and include their respective heirs,",
f"executors administrators and assigns;",
f"",
f"WHEREAS the Borrower is in need of funds and hence has approached the Lender to ",
f"grant her an interest-free loan of Rs.{amount}/-(Rupees {amount_words} only) for a period", 
f"of {years} years",

f"AND WHEREAS the Lender has agreed to grant a loan to the Borrower, free of interest, as", 
f"the Lender and the Borrower have known each other since several years;",
f"AND WHEREAS the parties hereto are desirous of recording the terms and conditions of this",
f"loan in writing;",
f"NOW THIS AGREEMENT WITNESSETH and it is hereby agreed by and between the parties",
f"hereto as under:",
f"",
f"1.     The Borrower hereto, being in need of money, has requested the Lender to give her", 
f"an interest-free loan of Rs.{amount}/- (Rupees {amount_words} only) to enable her to ",
f"purchase a residential flat, to which the Lender has agreed.",
f"",


f"2.     The said loan is required by the Borrower for a period of {years} years, commencing",
f"from {starting_date} and terminating on {ending_date}.",
f"",
f"3.     The Borrower hereby agrees and undertakes to return the loan of Rs.{amount}/- ",
f"(Rupees {amount_words}only), in instalments, within the aforesaid period of {years} years ",
f"and gives her personal guarantee for the same.",
f"",
f"4.     The terms and conditions of this Agreement are arrived at by the mutual consent of the", 
f"parties hereto.",

f"IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their",
f"respective hands the day and year first hereinabove written.",

f"SIGNED AND DELIVERED by the Within-",
f"named Lender in the presence of", 
f"",
f"SIGNED AND DELIVERED by the Within-",
f"named Borrower in the presence of",
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
    page_title="Loan Agreement Template",
    page_icon="📝"
)
st.header("Loan Agreement Template")

with st.form("rent_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    lender_name=st.text_input("Lender Name", placeholder="Enter the lender's name.")
    borrower_name=st.text_input("Borrower Name", placeholder="Enter the borrower's name.")
    amount=st.number_input("Amount", value=None,placeholder="Enter the amount.")
    starting_date=st.text_input("Starting Date", placeholder="Enter the starting date.")
    ending_date=st.text_input("Ending Date", placeholder="Enter the ending date.")
    city=st.text_input("City", placeholder="Enter the city.")
    years=st.slider('Number of years', 1, 10, 1)
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_agreement)
        path_name=generate_agreement(date, lender_name, 
                              borrower_name,amount,starting_date,ending_date,city,years)
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
