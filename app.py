import streamlit as st
from streamlit_option_menu import option_menu
from register import *
from login import *
from dashboard import *
from home import *


def main():
    nav_bar = option_menu(
        menu_title="Hypertension Risk Prediction",
        menu_icon="heart-pulse",
        options=["Home", "Create Account", "Log In"],
        icons=["house", "person-plus", "person"],
        default_index=0,
        orientation="horizontal",
        styles={"nav-link": {"--hover-color": "#FFCECE"}},
    )

    if nav_bar == "Home":
        home_page()

    elif nav_bar == "Create Account":
        create_account()

    elif nav_bar == "Log In":
        login_page()


st.set_page_config(
    page_title="HyperTraQ", page_icon="👨‍⚕️", layout="centered", menu_items=None
)

# STYLING
st.markdown(
    """
    <style>
    .main {
        background-color: #FFCECE;
        padding: 20px;
    }
    .stButton button {
        border-radius: 30px;
        border: 1px solid #000;
        background: #EE2828;
        width: 145px;
        height: 41px;
        align: center;
        flex-shrink: 0;
    }
    .stButton button:hover {
        background-color: #FFCECE;
    }

        .stContainer {
        background-color: #white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    if not Us.user:
        main()
    else:
        user_dashboard()
