import streamlit as st


def show():

    st.title("ℹ About")

    st.write(
        """
        ## PyMudCement-Optima

        PyMudCement-Optima is a drilling engineering application developed
        to assist engineers in mud design, rheology analysis,
        hydraulics calculations, cementing design and plug design.

        The software was developed as a final year project using
        Python and Streamlit.
        """
    )

    st.divider()

    st.subheader("Modules")

    st.markdown("""
    - Mud Weight Design
    - Rheology
    - Hydraulics
    - Cement Design
    - Plug Design
    - Results Dashboard
    """)

    st.divider()

    st.subheader("Developer")

    st.write("Name: Donkor Jeffery")

    st.write("Programme: BSc Electrical and Electronic Engineering")

    st.write("University: University of Energy and Natural Resources (UENR)")

    st.write("Technology: Python, Streamlit and Pandas")

    st.divider()

    st.success("Version 1.0")