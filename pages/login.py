import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import time
from pages.detadb_helper import DBManager

# from pages.intialconfig import intial_config


def display_login():
    # intial_config()
    # st.title("🔒Login")
    db = DBManager("test_db")
    users_db = db.get_all_users()
    user_usernames: list = [user["key"] for user in users_db]
    user_names: list = [user["name"] for user in users_db]
    user_emails: list = [user["email"] for user in users_db]
    user_passwds: list = [user["password"] for user in users_db]

    data_db: dict = {
        "credentials": {
            "usernames": {
                username: {
                    "email": email,
                    "name": name,
                    "password": password,
                }
                for username, name, email, password in zip(
                    user_usernames, user_names, user_emails, user_passwds
                )
            }
        }
    }

    global authenticator
    global loggedinflag
    loggedinflag = 0

    authenticator = stauth.Authenticate(
        data_db["credentials"],
        cookie_name="login",
        key="mainapp",
        cookie_expiry_days=30,
    )

    user_name, auth_status, user_email = authenticator.login(
        "🔒Login", "main"
    )

    if auth_status is False:
        st.error("⛔ Incorrect username or password. Try Again.")

    elif auth_status is None:
        st.warning("⚠️ Please enter your username and password")

    else:
        st.success("🎉 Successfully logged in!")
        time.sleep(1)
        if auth_status:
            loggedinflag = 1
            switch_page("session")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write("Don't have an account?")
    signup_button = st.button("Signup")
    if signup_button:
        switch_page("signup")
        pass
