import streamlit as st
from commons import *


def create_account():
    st.subheader("Create New Account")

    firstname = st.text_input(
        "First name",
    )
    lastname = st.text_input(
        "Last name",
    )
    email = st.text_input(
        "Email address",
    )
    password = st.text_input(
        "Password",
        type="password",
    )
    phone_number = st.text_input(
        "Phone number (with country code,)",
    )
    role = st.selectbox(
        "User as",
        ["Select", "Patient", "Professional"],
        index=0,
    )

    professional_id = ""
    if role == "Patient":
        professional_id = st.text_input("Enter Professional ID (optional)")

    # Display additional fields if the user is a Professional
    org_name = ""
    org_location = ""
    org_phone_number = ""

    if role == "Professional":
        org_name = st.text_input(
            "Organization Name",
        )
        org_location = st.text_input(
            "Organization Location (e.g. Ondo State, Nigeria)",
        )
        org_phone_number = st.text_input(
            "Organization Phone Number",
        )

    # Verification Check Box
    verify = st.checkbox("I confirm that all information provided above is correct")

    create_account_button = st.button("Create Account")

    if create_account_button:
        if role == "Select":
            return st.error(f"Choose a role between Patient and Professional")

        if not verify:
            return st.error(f"Check the details confirmation box")

        try:
            if Users.child_exists("email", email):
                return st.error("Account with email already exists")

            user: User = Users.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password,
                phone_number=phone_number,
                role=role,
                org_name=org_name,
                org_location=org_location,
                org_phone_number=org_phone_number,
                professional_id=professional_id,
            )

            # saves the user_id to session state
            session_state.user_id = user.id

            # user.update(lastname='Miracle')
            # user.delete()

            st.success("Account Created Successfully")
            st.info("Proceed to Login")

        except Exception as e:
            st.error(f"Account creation failed: {e}")
