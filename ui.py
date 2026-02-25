# ui.py

import streamlit as st
from email_gen import generate_email, SERVICE_OPTIONS  # pulls from your email_gen.py

st.set_page_config(page_title="Email Generator", page_icon="✉️")

st.title("Service Email Generator")

client_name = st.text_input("Client name")


services = st.multiselect(
    "Select services",
    SERVICE_OPTIONS,
)

if st.button("Generate email", type="primary"):
    if not client_name.strip():
        st.warning("Please enter a client name.")
    elif not services:
        st.warning("Please select at least one service.")
    else:
        email_text = generate_email(services, client_name.strip()) 
        st.text_area("Generated email", email_text, height=320)