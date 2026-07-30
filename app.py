import streamlit as st

from views import plug_design
from views import (
    mud_weight,
    rheology,
    hydraulics,
    cement_design,
    results,
    about,
)

st.set_page_config(
    page_title="PyMudCement-Optima",
    page_icon="🛢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image(
    "assets/JEFFY-LOGO.png",
    width=80
)

st.sidebar.title("PyMudCement-Optima")

st.sidebar.markdown("---")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Mud Weight",
        "Rheology",
        "Hydraulics",
        "Cement Design",
        "Plug Design",
        "Results",
        "About",
    ],
)

if page == "Home":
    st.title("🛢 PyMudCement-Optima")

    st.subheader(
        "Drilling Fluid and Cementing Engineering Software"
    )

    st.info(
        """
        This software assists drilling engineers in

        • Mud Weight Design

        • Rheology Analysis

        • Hydraulics

        • Cement Design

        • Plug Design

        Developed using Python and Streamlit.
        """
    )

elif page == "Mud Weight":
    mud_weight.show()

elif page == "Rheology":
    rheology.show()

elif page == "Hydraulics":
    hydraulics.show()

elif page == "Cement Design":
    cement_design.show()

elif page == "Plug Design":
    plug_design.show()

elif page == "Results":
    results.show()

elif page == "About":
    about.show()

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")

st.sidebar.caption("Developed by")

st.sidebar.caption("Donkor Jeffery")