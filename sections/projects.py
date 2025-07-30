import streamlit as st

def render_header_project():
    st.write("---")
    with st.container():
        st.markdown(
            "<h1 style='text-align: center;'>Projects</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align: center;'>A showcase of the projects I’ve worked on blending " \
            "creativity, technical skills, and purpose-driven solutions to solve real-world " \
            "problems and explore new ideas.</p>",
            unsafe_allow_html=True
        )
        st.write("#")   