import streamlit as st

# import cv2
from streamlit_extras.switch_page_button import switch_page
from pages.intialconfig import intial_config

# from pages.login import authenticator, loggedinflag

intial_config()

col1, mid, col2 = st.columns([1, 1, 9])
with col1:
    st.image("alertdrive.ico", width=120)
with col2:
    original_title = '<p style="color:#fff; font-weight:bold; font-size: 80px; //text-align: center; ">AlertDrive</p>'
    st.markdown(original_title, unsafe_allow_html=True)

# st.camera_input("")

start_session = st.button("Start Session?")


if start_session:
    st.write("BRUH")

st.button("Logout")
