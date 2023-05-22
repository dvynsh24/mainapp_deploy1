import streamlit as st
from streamlit_option_menu import option_menu
from pages.about import display_about
from pages.contact import display_contact
from pages.home import display_home
from pages.login import display_login

# from pages.intialconfig import intial_config
# from pages.detadb_helper import DBManager

# import streamlit_authenticator as stauth
# from streamlit_extras.switch_page_button import switch_page


def hide_all():
    st.set_page_config(initial_sidebar_state="collapsed")

    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 4rem;}
        div[data-testid="stSidebarNav"] {display: none;}
        .css-15zrgzn {display: none}
        .css-1dp5vir {display: none} 
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
        unsafe_allow_html=True,
    )


# hide_all()

navbar = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact", "Login"],
    icons=[
        "broadcast",
        "person-fill",
        "telephone-fill",
        "box-arrow-in-right",
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#000",
        },
        "icon": {"color": "white", "font-size": "16px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "padding": "8px",
            "--hover-color": "#2f2f2f",
        },
        "nav-link-selected": {"background-color": "rgb(250, 30, 55)"},
    },
)

if navbar == "Home":
    display_home()

elif navbar == "About":
    display_about()

elif navbar == "Contact":
    display_contact()

elif navbar == "Login":
    display_login()

else:
    st.write("Settings PAGE")
