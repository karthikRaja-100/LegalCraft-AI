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
def generate_rental_agreement(date, vendor_name, vendor_address,vendor_father_name,purchaser_address,purchaser_name,purchaser_father_name,
                               property_address , street_name,property_number,late_interest,amount,fine):
   

    # Create a PDF document
   


    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)


    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.spaceAfter = 12
    normal_style.leading = 14




    content = []


    sections = [

    f"Draft of Agreement for Sale of a House",
    f"",

    f"This Agreement of sale made at {property_address} on this {date}, between {vendor_name} son/daughter of {vendor_father_name} resident of {vendor_address} hereinafter called the vendor of the ONE PART and {purchaser_name} son/daughter of {purchaser_father_name} resident of {purchaser_address} hereinafter called the purchaser of the OTHER PART.",
    f"",
    f"WHEREAS the vendor is absolutely seized and possessed of or well and sufficiently entitled to the house more fully described in the Schedule hereunder:",
    f"AND WHEREAS the vendor has agreed to sell his house to the purchaser on the terms and conditions hereafter set-forth.",
    f"",
    f"NOW this Agreement Witnesseth as Follows",
    f"1.     The vendor will sell and the purchaser will purchase that entire house No {property_number} {street_name} more particularly described in the Schedule hereunder written at a price of Rs {amount} Free from all encumbrances.",
    f"2.     The purchaser has paid a sum of Rs {amount} as earnest money on {amount} (the receipt of which sum, the vendor hereby acknowledges) and the balance amount of consideration will be paid at the time of execution of conveyance deed.",
    f"3.     The sale shall be completed within a period of {notice_period} months from this date and it is hereby agreed that time is the essence of the contract.",
    f"4.     The vendor shall submit the title deeds of the house in his possession or power to the purchaser's advocate within one week from the date of this agreement for investigation of title and the purchaser will intimate about his advocate's report within {notice_period} days after delivery of title deeds to his advocate.",
    f"5.     If the purchaser's Advocate gives the report that the vendor's title is not clear, the vendor shall refund the earnest money, without interest to the purchaser within {notice_period} days from the date of intimation about the advocate's report by the purchasers. If the vendor does not refund the earnest money within {notice_period} days from the date of intimation about the advocate's report, the vendor will be liable to pay interest @ {late_interest} p.m. up to the date of repayment of earnest money.",
    f"6.     The vendor declares that the sale of the house will be without encumbrances.",
    f"7.     The vendor will hand over the vacant possession of the house on the execution and registration of conveyance deed.",
    f"8.     If the purchaser commits breach of the agreement, the vendor shall be entitled to forfeit the earnest money paid by the purchaser to the vendor and the vendor will be at liberty to resell the property to any person.",
    f"9.     It the vendor commits breach of the agreement, he shall be liable to refund earnest money, received by him and a sum of Rs.{fine} by way of liquidated damages.",
    f"10.  The vendor shall execute the conveyance deed in favour of the purchaser or his nominee as the purchaser may require, on receipt of the balance consideration.",
    f"11.  The vendor shall at his own costs obtain clearance certificate under section 230A, Income tax Act, 1961 and other permissions required for the completion of the sale.",
    f"12.  The expenses for, preparation of the conveyance deed, cost of stamp, registration charges and all other cut of pocket expenses shall be borne by the purchaser.",
    f"",
    f"",


    f"Schedule above referred to",
    f"IN WITNESS WHEREOF the parties have set their hands to this Agreement on the day and year first hereinabove written.",
    f"",
    f"Signed and delivered by Shri {vendor_name}",
    f"the within named vendor",
    f"Signed and delivered by Shri  {purchaser_name}",
    f"The within named purchaser",
    f"",
    f"WITNESSES;"
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
    page_title="House Sale Agreement Template",
    page_icon="📝"
)
st.header("House Sale Agreement Template")

with st.form("house_sale_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    vendor_name=st.text_input("Vendor Name", placeholder="Enter the vendors's name.")
    vendor_address=st.text_input("Vendor Address", placeholder="Enter the vendor's address.")
    purchaser_name=st.text_input("Purchaser Name", placeholder="Enter the purchaser's name.")
    purchaser_address=st.text_input("Purchaser Address", placeholder="Enter the purchaser's address.")
    vendor_father_name=st.text_input("Vendor Father Name", placeholder="Enter the vendor's father name.")
    purchaser_father_name=st.text_input("Purchaser Father Name", placeholder="Enter the purchaser's father name.")
    property_address=st.text_input("Property Address", placeholder="Enter the property address.")
    street_name=st.text_input("Street Name", placeholder="Enter the street name.")
    property_number=st.text_input("Property Number",placeholder="Enter the property number.")
    notice_period=st.slider('Choose notice period between 1 and 12', 1, 12, 1)
    late_interest=st.slider('Choose late interest', 1, 10, 1)
    amount=st.number_input("Amount", value=None,placeholder="Enter the amount.")
    fine=st.number_input("fine", value=None,placeholder="Enter the fine amount")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_rental_agreement)
        path_name=generate_rental_agreement(date, vendor_name, vendor_address,vendor_father_name,purchaser_address,purchaser_name,purchaser_father_name,
                               property_address , street_name,property_number,late_interest,amount,fine)
                                
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
