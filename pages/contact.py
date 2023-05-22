import streamlit as st
import re
from contact_utils.helper import send_email
from contact_utils.constants import (
    SMTP_SERVER_ADDRESS,
    PORT,
    SENDER_PASSWORD,
    SENDER_ADDRESS,
)


def display_contact():
    st.title("📫Have a message?")

    def validate_email(email):
        pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        return re.match(pattern, email)

    def validate_subject(subject):
        if not subject:
            return False

        pattern = r"^[\w\s.-]+$"
        return bool(re.match(pattern, subject)) and len(subject) <= 100

    def validate_body(body):
        return bool(body) and len(body) <= 500

    with st.form("Email Form"):
        receiver_email = "dvynsh24@gmail.com"
        sender_email = st.text_input(
            label="Email Address", placeholder="Your Email Address"
        )
        email_subject = st.text_input(
            label="Subject", placeholder="Your Message is regarding?"
        )
        email_body = st.text_area(
            label="Message", placeholder="Your thoughts here..."
        )
        file_uploaded = st.file_uploader("Attachment")

        if st.form_submit_button(label="Send"):
            if not validate_email(sender_email):
                st.warning("📢Please enter a valid email address.")

            elif not validate_subject(email_subject):
                st.warning(
                    "✍️Subject is not valid. Please make sure it is alphanumeric and does not exceed 100 characters."
                )
            
            elif not validate_body(email_body):
                st.warning("✍️Email Message is not valid. Please make sure it is not empty and does not exceed 500 characters.")

            else:
                email_top_text = f"""
                -------------------------------------
                EMAIL DETAILS:
                Sender's Email Address: {sender_email}
                Subject: {email_subject}
                -------------------------------------
                """

                email_all_text = email_top_text + email_body

                send_email(
                    sender=SENDER_ADDRESS,
                    password=SENDER_PASSWORD,
                    receiver=receiver_email,
                    smtp_server=SMTP_SERVER_ADDRESS,
                    smtp_port=PORT,
                    email_message=email_all_text,
                    subject=email_subject,
                    attachment=file_uploaded,
                )

                st.success("🎉Hooray! Your message was sent successfully!")


# display_contact()
