from streamlit import st

st.title("Contact Us")

st.markdown("""
## Contact Us
Fill out the form below and we will get back to you as soon as possible.
""")

info_section = """
## Information
Here's some information about us:
- Our company is based in Abu Dhabi, UAE.
- We have offices in Dubai and Sharjah.
- Our mission is to promote and develop the UAE's economy through innovative technologies.
- We are always looking for talented individuals to join our team.
"""

st.markdown(info_section, unsafe_allow_html=True)

if st.button("Submit"):
    name = st.text_input("Name")
    email = st.email_input("Email")
    message = st.text_input("Message")
else:
    name = ""
    email = ""
    message = ""

st.markdown("""
## Submit Your Message
Your Name: {}
Your Email: {}
Your Message: {}
""".format(name, email, message))
