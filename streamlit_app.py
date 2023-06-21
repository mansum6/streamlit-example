import streamlit as st

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

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
