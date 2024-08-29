import streamlit as st
import numpy as np
from commons import *


def display_message(user: User, chat: Chat):
    # Format the datetime
    formatted_time = format_datetime(chat.created_timestamp)

    sender = f"{user.firstname} {user.lastname}"
    message = chat.message

    side = "left" if user == Us.user else "right"

    # Create the chat message layout
    st.markdown(
        f"""
        <div style="margin-bottom: 10px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1); margin-{side}: 50%">
            <div style="text-align: left; font-weight: bold;">{sender}</div>
            <div style="text-align: right; font-weight: normal;">{message}</div>
            <div style="font-size: 12px; color: gray; text-align: right;">{formatted_time}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()


# PATIENT PROFILE STARTS HERE
def patient_profile():
    # st.success(f"Signed in as {user.firstname} {user.lastname}") # ATTENTION: To Show Patient Name

    st.metric(label="Patient ID", value=Us.user.id)  # Display Patient ID

    medical_datas = MedicalDatas.find(
        dict(uid=Us.user.id),
        limit=1,
        descending=True,
    )
    medical_data: MedicalData = medical_datas[0] if medical_datas else None

    st.subheader("Health History", anchor="center")

    if medical_data:
        st.info(f"Last Checked: {format_datetime(medical_data.created_timestamp)}")  #

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Weight (kg)", "70", "1.25")
        col2.metric("Height (cm)", "155", "-3.5")
        col3.metric("BMI (kg/m2)", "19.55", "0.43")
        col4.metric("Systolic BP (mmHg)", "189", "-2")
        col5.metric("Diastolic BP (mmHg)", "74", "4")

    if Us.user.professional_id:
        prof: User = Users.get_child(Us.user.professional_id)

        # Show Assigned Professional, retun 'None' if none.
        container = st.container(
            border=True,
        )
        container.header("Professional Info:")
        container.write(f"Name: {prof.firstname}")
        container.write(f"Contact: {prof.org_phone_number}")
        container.write(f"Organisation: {prof.org_name}")

        chats: list[Chat] = Chats.find(
            dict(
                patient_id=Us.user.id,
                professional_id=prof.id,
            ),
            descending=True,
            sort="created_timestamp",
        )

        st.divider()

        st.subheader("Send Message to Professional")

        if chats:
            # Retrive Professional Last Update
            st.success(f"Last Sent: {format_datetime(chats[0].created_timestamp)}")

        message = st.chat_message("human")
        msg = message.text_area("Drop a Message...")

        if message.button("Send Message"):
            if not msg:
                st.error("Type a message first")
            else:
                Chats.create(
                    patient_id=Us.user.id,
                    professional_id=prof.id,
                    sender="patient",
                    message=msg,
                )

        st.divider()

        # View Previous Chat History
        st.subheader("Conversation History")

        # show the chats in the ui
        for chat in chats:
            display_message(
                Us.user if chat.sender == "patient" else prof,
                chat,
            )

        # st.error("Last Received: Thursday 22nd August 12:15PM")


# PROFESSIONAL PROFILE STARTS HERE
def professional_profile():
    st.metric(
        label="Professional ID",
        value=Us.user.id,
    )  # Refernce -> https://docs.streamlit.io/develop/api-reference/data/st.metric

    count = Users.count_documents(
        dict(professional_id=Us.user.id),
    )
    st.metric(
        label="Total Patients",
        value=count,
        delta_color="normal",
    )

    container = st.container(border=True)
    # Reference -> https://docs.streamlit.io/develop/api-reference/layout/st.container

    container.header("Organisation Info:")
    container.write(f"Name: {Us.user.org_name}")
    container.write(f"Address: {Us.user.org_location}")
    container.write(f"Contact: {Us.user.org_phone_number}")


def patient_history(patients):
    patients_map = {p.id: p for p in patients}

    option = st.selectbox(
        "Select Patient",
        ["Select"] + [f"{p.id} | {p.firstname} {p.lastname}" for p in patients],
        index=None,
        placeholder="Select...",
    )

    if (not option) or option == "Select":
        return

    id = option.split(" | ")[0]

    patient = patients_map[id]

    # Patient Details
    # st.write("You selected:", option)
    container = st.container(border=True)
    container.header("Patient Info:")
    container.write(f"Name: {patient.firstname} {patient.lastname}")
    container.write(f"Contact: {patient.phone_number}")

    medical_datas: list[MedicalData] = MedicalDatas.find(
        dict(uid=id),
        descending=True,
    )

    if medical_datas:
        last_medical_data = medical_datas[0]

        container.write(f"Age: {last_medical_data.age}")  # Retrive Last Inputed Age
        container.write(f"Gender: {last_medical_data.gender}")

        st.subheader("Health History")

        st.info(f"Last Checked: {format_datetime(last_medical_data.created_timestamp)}")

        weight_delta = 0
        height_delta = 0
        bmi_delta = 0
        sbp_delta = 0
        dbp_delta = 0

        if len(medical_datas) > 1:
            s = medical_datas[1]
            weight_delta = s.weight - last_medical_data.weight
            height_delta = s.height - last_medical_data.height
            bmi_delta = s.bmi - last_medical_data.bmi
            sbp_delta = s.systolic_bp - last_medical_data.systolic_bp
            dbp_delta = s.systolic_bp - last_medical_data.systolic_bp

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric(
            "Weight (kg)",
            "70",
            weight_delta,
        )
        col2.metric(
            "Height (cm)",
            "155",
            height_delta,
        )
        col3.metric(
            "BMI (kg/m2)",
            "19.55",
            bmi_delta,
        )
        col4.metric(
            "Systolic BP (mmHg)",
            "189",
            sbp_delta,
        )
        col5.metric(
            "Diastolic BP (mmHg)",
            "74",
            dbp_delta,
        )

        if len(medical_datas) > 1:

            # ATTENTION: I'll like to put the Chart inside the expander

            expander = st.expander("View History")
            expander.write(
                """
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """
            )

            # Chart of Health Record: Ref -> https://docs.streamlit.io/develop/api-reference/layout/st.tabs

            # Multiple Options to View Each History by Day, Week, Month or Selected Duration

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                [
                    "📈 Weight",
                    "📈 Height",
                    "📈 BMI",
                    "📈 Systolic BP",
                    "📈 Diastolic BP",
                    "📈 Diagnosis",
                ]
            )

            weight_s = []
            height_s = []
            bmi_s = []
            sbp_s = []
            dbp_s = []
            diagnosis_s = []

            for medical_data in medical_datas:
                weight_s.append(medical_data.weight)
                height_s.append(medical_data.height)
                bmi_s.append(medical_data.bmi)
                sbp_s.append(medical_data.systolic_bp)
                dbp_s.append(medical_data.diastolic_bp)
                diagnosis_s.append(medical_data.diagnosis)

            tab1.subheader("History of Patient Weight")
            tab1.line_chart(
                weight_s,
                x_label="Selected Duration",
                y_label="Weight in kg",
            )

            tab2.subheader("History of Patient Height")
            # tab2.markdown("xxx")
            tab2.line_chart(
                height_s,
                x_label="Selected Duration",
                y_label="Height in cm",
                color="#FF0000",
            )

            tab3.subheader("History of Patient Body Mass Index")
            tab3.line_chart(
                bmi_s,
                x_label="Selected Duration",
                y_label="BMI in kg/m2",
                color="#FF0000",
            )

            tab4.subheader("History of Patient Systolic Blood Pressure")
            tab4.line_chart(
                sbp_s,
                x_label="Selected Duration",
                y_label="Systolic Blood Pressure in mmHg",
            )

            tab5.subheader("History of Patient Diastolic Blood Pressure")
            tab5.line_chart(
                dbp_s,
                x_label="Selected Duration",
                y_label="Diastolic Blood Pressure in mmHg",
            )

            tab6.subheader("History of Patient Diagnosis")
            tab6.line_chart(
                diagnosis_s,
                x_label="Selected Duration",
                y_label="Diagnosed Outcome",
            )

            # Duration to View Patient History: Ref -> https://docs.streamlit.io/develop/api-reference/widgets/st.date_input

            # date_input = _main.date_input

            today = datetime.datetime.now()
            next_year = today.year + 1
            jan_1 = datetime.date(next_year, 1, 1)
            dec_31 = datetime.date(next_year, 12, 31)

            d = st.date_input(
                "Select Duration to View",
                (jan_1, datetime.date(next_year, 1, 7)),
                jan_1,
                dec_31,
                format="MM.DD.YYYY",
            )

        st.divider()

    chats: list[Chat] = Chats.find(
        dict(
            patient_id=patient.id,
            professional_id=Us.user.id,
        ),
        sort="created_timestamp",
        descending=True,
    )

    st.subheader("Send Message to Patient")

    if chats:
        # Retrive Patient Last Update
        st.success(f"Last Sent: {format_datetime(chats[0].created_timestamp)}")

    message = st.chat_message("human")
    # message.write("Hello human")
    msg = message.text_area("Drop a Message...", value="")

    if message.button("Send Message"):
        if not msg:
            st.error("Type a message first")
        else:
            Chats.create(
                patient_id=patient.id,
                professional_id=Us.user.id,
                sender="professional",
                message=msg,
            )

    st.divider()

    # View Previous Chat History
    st.subheader("Conversation History")

    chats: list[Chat] = Chats.find(
        dict(
            patient_id=patient.id,
            professional_id=Us.user.id,
        ),
        sort="created_timestamp",
        descending=True,
    )

    # write the ui to show the chats
    for chat in chats:
        display_message(
            Us.user if chat.sender == "professional" else patient,
            chat,
        )

    return True
