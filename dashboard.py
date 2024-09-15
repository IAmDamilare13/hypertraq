import streamlit as st
from streamlit_option_menu import option_menu
from health_status import prediction
from profiles import *
from commons import *


def logout():
    cm.delete("user_id")
    Us.user = None
    st.rerun()


def user_dashboard():
    user = Us.user

    if not user:
        st.error("Login first")
        from app import main

        return

    # PATIENT SECTION STARTS HERE
    if user.role == "Patient":
        nav_bar2 = option_menu(
            menu_title="Hypertension Risk Prediction",
            menu_icon="heart-pulse",
            options=["Profile", "Check Health Status", "Log Out"],
            icons=["person-heart", "search-heart", "box-arrow-left"],
            default_index=0,
            orientation="horizontal",
            styles={"nav-link": {"--hover-color": "#FFCECE"}},
        )

        if nav_bar2 == "Profile":
            st.success(f"Signed in as {user.firstname} {user.lastname}")
            patient_profile()

        # Check user role
        else:
            if nav_bar2 == "Check Health Status":
                prediction()

            if nav_bar2 == "Log Out":
                st.subheader(f"Prioritize your Health {user.firstname} {user.lastname}")

                logout()

                # main_home()

    # PROFESSIONAL SECTION STARTS HERE
    elif user.role == "Professional":
        nav_bar3 = option_menu(
            menu_title="Hypertension Risk Prediction",
            menu_icon="heart-pulse",
            options=[
                "Profile",
                "View Patient History",
                "Check Health Status",
                "Log Out",
            ],
            icons=["person-heart", "calendar-heart", "search-heart", "box-arrow-left"],
            default_index=0,
            orientation="horizontal",
            styles={"nav-link": {"--hover-color": "#FFCECE"}},
        )
        if nav_bar3 == "Profile":
            st.success(f"Signed in as {user.firstname} {user.lastname}")
            professional_profile()

        else:
            if nav_bar3 == "View Patient History":
                # def professional_dashboard(professional_id):
                patients: list[User] = Users.find(
                    dict(professional_id=user.id),
                )

                if patient_history(patients):
                    return

                # Fetch all patients and their medical data

                for patient in patients:
                    st.write(f"Patient: {patient.firstname} {patient.lastname}")

                    medical_datas: list[MedicalData] = MedicalDatas.find(
                        dict(uid=patient.id)
                    )

                    if medical_datas:
                        record = medical_datas[0]
                        # st.write(f" - Date: {record.timestamp}")
                        # st.write(f"   - Gender: {record.gender}")
                        # st.write(f"   - Age: {record.age}")
                        # st.write(f"   - Systolic BP: {record.systolic_bp}")
                        # st.write(f"   - Diastolic BP: {record.diastolic_bp}")
                        # st.write(f"   - BMI: {record.bmi}")
                        st.write(f"   - Predicted Risk: {record.diagnosis}")

            if nav_bar3 == "Check Health Status":
                prediction()

            if nav_bar3 == "Log Out":
                st.subheader(f"Prioritize your Health {user.firstname} {user.lastname}")

                logout()
