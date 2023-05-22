import streamlit as st
from markdownlit import mdlit


def display_home():
    hide_image_fullscreen = """
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    """

    st.markdown(hide_image_fullscreen, unsafe_allow_html=True)

    col1, mid, col2 = st.columns([1, 1, 14])
    with col1:
        st.image("alertdrive.ico", width=81)
    with col2:
        original_title = '<p style="color:#fff; font-weight:bold; font-size: 50px;">AlertDrive</p>'
        st.markdown(original_title, unsafe_allow_html=True)

    st.markdown("##### A Deep-Learning Based Driver Alertness Evaluation")
    
    st.write("")
    st.header("Streamlit Page Example")

    # Some text with subheadings
    st.subheader("About")
    st.write(
        "This is a sample Streamlit page demonstrating the usage of headings, \
            text, and buttons."
    )
    mdlit(
        """Tired from [default links](https://extras.streamlit.app)?
    Me too! Discover Markdownlit's `@()` operator. Just insert a link and it
    will figure a nice icon and label for you!
    Example: @(https://extras.streamlit.app)... better, right? You can
    also @(🍐)(manually set the label if you want)(https://extras.streamlit.app)
    btw, and play with a [red]beautiful[/red] [blue]set[/blue] [orange]of[/orange]
    [violet]colors[/violet]. Another perk is those beautiful arrows -> <-
    """
    )
