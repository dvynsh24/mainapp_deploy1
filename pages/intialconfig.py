import streamlit as st


def intial_config():
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
