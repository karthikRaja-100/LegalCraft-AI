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
def generate_rental_agreement(date, landlord_name, landlord_address,
                               property_address , property_category, no_of_bedroom, no_of_bathroom, no_of_parking, property_area, lease_term,
                               lease_start_date, notice_period, monthly_rent, rent_payment_day, starting_meter_reading,
                               deposit_amount,city_name,state,tenant_name,tenant_address):
   

    # Create a PDF document
   


    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)


    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.spaceAfter = 12
    normal_style.leading = 14


    p = inflect.engine()


    monthly_rent_words = f"{p.number_to_words(monthly_rent)} Rupees" if monthly_rent is not None else "N/A"
    deposit_amount_words = f"{p.number_to_words(deposit_amount)} Rupees" if deposit_amount is not None else "N/A"


    content = []


    sections = [

        f"",
        f"This agreement made at {city_name} on this {date} between {landlord_name}, residing at {landlord_address} hereinafter referred, to as the `LESSOR` of the One Part AND {tenant_name}, residing at ,{tenant_address} hereinafter referred to as, the `LESSEE` of the ther Part;",
        f"",
        f"WHEREAS the Lessor is the lawful owner of, and otherwise, well sufficiently entitled to {property_address}, falling in the category {property_category} and, comprising of {no_of_bedroom} Bedroom ,{no_of_bathroom} Bathrooms,{no_of_parking}  Carparks with an extent of {property_area} sq.ft. hereinafter, referred to as the `said premises`;",
        f"AND WHEREAS at the request of the Lessee the Lessor has agreed, to let the said premises to the tenant for a term of [Lease Term] commencing from {lease_start_date} Lease Start Date, in the manner hereinafter appearing.",
        f"",

        f"NOW THIS AGREEMENT WITNESSETH AND IT IS HEREBY AGREED BY AND BETWEEN ",
        f"THE PARTIES AS UNDER: ",
        f"",
        f"1. That the Lessor hereby grant to the Lessee the right to enter into and use and ,remain in the said premises along with the existing fixtures and fittings listed in ,Annexure 1 to this Agreement and that the Lessee shall be entitled to peacefully , possess, and enjoy possession of the said premises and the other rights herein." ,
        f"2. That the lease hereby granted shall, unless cancelled earlier under any provision of ,this Agreement remain in force for a period of {lease_term} Lease Term. ",
        f"3. That the Lessee will have the option to terminate this lease by giving {notice_period} Notice period, in writing to the Lessor." ,
        f"4. That the Lessee shall have no right to create any sub-lease or assign or transfer in any manner, the lease or give to any one the possession of the said premises or any part thereof.",
        f"5. That the Lessee shall use the said premises only for residential purposes.",
        f"6. That the Lessor shall before handing over the said premises ensure the working of sanitary electrical and water supply connections and other fittings pertaining to the , said premises. It is agreed that it shall be the responsibility of the Lessor for their , return in the working condition at the time of re-possession of the said premises ,(reasonable wear and tear and loss or damage by fire flood rains accident irresistible force, or act of God excepted).",
        f"7. That the Lessee is not authorized to make any alteration in the construction of the ,said premises. The Lessee may however install and remove his own fittings and fixtures provided, this is done without causing any excessive damage or loss to the said premises.",
        f"8. That the day to day repair jobs such as fuse blow out replacement of light bulbs/tubes leakage, of water taps maintenance of the water pump and other minor repairs etc. shall be effected by the, Lessee at its own cost and any major repairs either structural or to the electrical or water connection,  plumbing leaks water seepage shall be attended to by the Lessor. In the event of the Lessor failing to carry, out the repairs on receiving notice from the Lessee, the Lessee shall undertake the necessary repairs and the,Lessor will be liable to immediately reimburse costs incurred by the Lessee.",
        f"9. That the Lessor or its duly authorized agent shall have the right to enter into or upon the said premises or any part thereof at a mutually arranged convenient time for the purpose of inspection.",
        f"10. That the Lessee shall use the said premises along with its fixtures and fitting in careful and responsible manner and shall handover the premises to the Lessor in working condition (reasonable wear and tear and loss or damage by fire, flood, rains, accidents, irresistible force or act of God excepted).",
        f"11. That in consideration of use of the said premises the Lessee agrees that he shall pay to the Lessor during the period of this agreement, a {monthly_rent},{monthly_rent_words} at the rate of [Monthly Rental in Number & Words]. The amount will be paid in advance on or before the date of {rent_payment_day} of every English calendar month.",
        f"12. It is hereby agreed that if default is made by the lessee in payment of the rent for a period of three months, or in observance and performance of any of the covenants and stipulations hereby contained and on the part to be observed and performed by the lessee, then on such default, the lessor shall be entitled in addition to or in the alternative to any other remedy that may be available to him at this discretion, to terminate the lease and eject the lessee from the said premises; and to take possession thereof as full and absolute owner thereof, provided that a notice in writing shall be given by the lessor to the lessee of his intention to terminate the lease and to take possession of the said premises. If the arrears of rent are paid or the lessee comply with or carry out the covenants and conditions or stipulations, within fifteen days from the service of such notice, then the lessor shall not be entitled to take possession of the said premises.",
        f"13. That in addition to the compensation mentioned above, the Lessee shall pay the actual electricity, shared maintenance, water bills for the period of the agreement directly to the authorities concerned. The relevant `start date` meter readings are [Starting Meter Reading].",
        f"14. That the Lessee has paid to the Lessor a sum of {deposit_amount} as deposit, free of interest, which the Lessor does accept and acknowledge. This deposit is for the due performance and observance of the terms and conditions of this Agreement. The deposit shall be returned to the Lessee simultaneously with the Lessee vacating the said premises. In the event of failure on the part of the Lessor to refund the said deposit amount to the Lessee as aforesaid, the Lessee shall be entitled to continue to use and occupy the said premises without payment of any rent until the Lessor refunds the said amount (without prejudice to the Lessee`s rights and remedies in law to recover the deposit).",
        f"15. That the Lessor shall be responsible for the payment of all taxes and levies pertaining to the said premises including but not limited to House Tax, Property Tax, other cesses, if any, and any other statutory taxes, levied by the Government or Governmental Departments. During the term of this Agreement, the Lessor shall comply with all rules, regulations and requirements of any statutory authority, local, state and central government and governmental departments in relation to the said premises.",
        f"IN WITNESS WHEREOF, the parties hereto have set their hands on the day and year first hereinabove mentioned.",
        f"",
        f'{landlord_name}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{tenant_name}',
        f"{landlord_address}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{tenant_address}",
        f"",
        f"",
        f"",
        f"WITNESS ONE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; WITNESS TWO",
        f"[Name & Address]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Name & Address]",

        f"",
        f"",
        f" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- ANNEXURE I  --                                        ",
        f"",
        f"",
        f"List of fixtures and fittings provided in [Lease Property Address Line 1, Address Line 2, City, State, Pin Code]:",
        f"",
        f"1. Item 1 ",
        f"2. Item 2 ",
        f"3. Item 3 ",
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
    page_title="Rental Agreement Template",
    page_icon="📝"
)
st.header("Rental Agreement Template")
with st.form("rent_template"):
    date=st.text_input("Date",placeholder="Enter date in the format DD/MM/YYYY.")
    landlord_name=st.text_input("Landlord Name", placeholder="Enter the landlord's name.")
    landlord_address=st.text_input("Landlord Address", placeholder="Enter the landlord's address.")
    tenant_name=st.text_input("Tenant Name", placeholder="Enter the tenant's name.")
    tenant_address=st.text_input("Tenant Address", placeholder="Enter the tenant's address.")
    city_name=st.text_input("City", placeholder="Enter the city.")
    state=st.text_input("State", placeholder="Enter the state.")
    property_address=st.text_input("Property Address", placeholder="Enter the property address.")
    property_category = st.selectbox(
    'Property Category',
    ("Independent House", "Apartment", "Farm House", "Residential Property","Commercial Property"))
    no_of_bedroom=st.slider('Number of Bedrooms', 1, 7, 1)
    no_of_bathroom=st.slider('Number of Bathrooms', 1, 3, 1)
    no_of_parking=st.slider('Number of Car Parking', 1, 4, 1)
    property_area=st.number_input("Property area",value=None,placeholder="Enter the property area in square feet.")
    lease_term=st.slider('Lease Term(Period of Agreement)', 1, 12, 1)
    lease_start_date=st.text_input("Lease Start Date",placeholder="Enter the lease start date(DD/MM/YYYY)")
    notice_period=st.slider('Choose notice period between 1 and 12', 1, 12, 1)
    monthly_rent=st.number_input("Monthly Rent",value=None,placeholder="Enter Monthly rent.")
    rent_payment_day=st.number_input("Day of Rent Payment", value=None,placeholder="Enter on which day of ever month the rent should be paid")
    starting_meter_reading=st.number_input("Starting Meter Reading", value=None,placeholder="Enter the starting meter reading.")
    deposit_amount=st.number_input("Deposit Amount", value=None,placeholder="Enter the deposit amount.")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted",on_click=generate_rental_agreement)
        path_name=generate_rental_agreement(date, landlord_name, landlord_address,
                               property_address , property_category, no_of_bedroom, no_of_bathroom, no_of_parking, property_area, lease_term,
                               lease_start_date, notice_period, monthly_rent, rent_payment_day, starting_meter_reading,
                               deposit_amount,city_name,state,tenant_name,tenant_address)
        st.markdown(get_binary_file_downloader_html(path_name, "PDF"), unsafe_allow_html=True)
