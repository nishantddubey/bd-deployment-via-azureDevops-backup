import streamlit as st
from fornt_page import display_front_page
from main_page import main_app

# Set Streamlit app configuration for full-screen
st.set_page_config(layout="wide")

# Initialize session state if it doesn't exist
if 'email_logged' not in st.session_state:
    st.session_state.email_logged = False

# Check if the email is submitted
if not st.session_state.email_logged:
    display_front_page()
else:
    main_app()
