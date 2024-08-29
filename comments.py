import streamlit as st
from commons import *


def message():
    ph = "Enter message here..."
    message = st.text_area(
        label=" :orange[+ Send a Message]",
        placeholder=ph,
        height=None,
        max_chars=500,
    )

    if st.button("Send Message", use_container_width=20):
        st.success("Message Sent!!")

    st.divider()

    st.header(" :violet[Message History] ")
    st.info("Sent on Friday 23rd August 2024 at 21:53PM")
    st.text_area("")
