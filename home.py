import streamlit as st
from PIL import Image

# from streamlit_faker import get_streamlit_faker


def home_page():
    # st.title("Welcome to HyperTraQ")
    st.write("This platform is an undergraduate project, developed to demonstrate the feasibility of a hypertension risk prediction and management system. "
       "With the aid of a preditive model, patients and healthcare professionals can manage and monitor hypertension risk.")

    image = Image.open("images/chart.png")
    st.image(image, use_column_width=True)

    # Patients section
    st.subheader("Patients")

    # Define columns for patient tiles
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Personalized Health Dashboard</h3>
            <p>Display a personalized dashboard where patients can track their most recent health records, including blood pressure readings, BMI, and other vital statistics.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with p_col2:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Direct Communication with Health Professionals</h3>
            <p>Patients can easily communicate directly with their authorized healthcare professional, ensuring timely advice and support.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write("")

    # Additional columns for more patient features
    p_col3, p_col4 = st.columns(2)

    with p_col3:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Secure and Confidential</h3>
            <p>Emphasize the security features that ensure patient data is protected and only accessible by authorized healthcare professionals.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with p_col4:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Real-time Health Monitoring</h3>
            <p>Allow patients to input daily health data and receive immediate feedback on their risk levels for hypertension, along with only authorized healthcare professional.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.divider()

    # Professionals section
    st.subheader("Professionals")

    # Define columns for professional tiles
    pr_col1, pr_col2 = st.columns(2)

    with pr_col1:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Comprehensive Patient Management</h3>
            <p>Professionals can manage multiple patients, view detailed health records, and track patient progress over time.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with pr_col2:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Data-Driven Insights</h3>
            <p>Provide professionals with analytical tools that help them interpret patient data, identify risk trends, and make informed decisions.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write("")

    # Additional columns for more professional features
    pr_col3, pr_col4 = st.columns(2)

    with pr_col3:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Efficient Patient Assignment</h3>
            <p>Highlight how the platform makes it easy to assign patients to professionals based on location, specialization, or other criteria.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with pr_col4:
        st.markdown(
            """
        <div style="background-color: #FF5146; color: white; padding: 20px; border-radius: 5px;">
            <h3>Seamless Integration with Health Records</h3>
            <p>Showcase how the platform integrates with existing electronic health records (EHR) systems, making it easier for professionals to access and update patient information.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.subheader("Feedback 🙏")
    st.write(
        "[Kindly click here to provide your feedback (https://forms.gle/ymNXSg8s48az6uFM7)."
    )
