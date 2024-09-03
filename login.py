from typing import Optional
import streamlit as st
from models import *
from dashboard import *


def main_home():
    st.title("Hypertension Risk Prediction :heart:")


def login_page():
    if Us.user:
        return user_dashboard()

    st.subheader("Login")
    email = st.text_input("Email address")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        try:
            print([a.db_dump for a in Users.find()])

            Us.user = Users.get_one("email", email)

            if Us.user == None:
                return st.error("Account with email does not exists")
            elif Us.user.password != password:
                return st.error("Invalid password")

            # saves the user_id to session state
            cm.set("user_id", Us.user.id)
            st.rerun()

        except Exception as e:
            st.error(f"Login failed: {e}")
