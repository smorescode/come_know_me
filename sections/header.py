import streamlit as st
from streamlit_lottie import st_lottie

def render_header(lottie_data_analysis):
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("Hello, I'm Norhanah :wave:")
            st.header("An aspiring student Data Analyst")
            st.write("I'm interested in learning data analysis, and I'm focusing on tools like " \
            "Python for data manipulation, Power BI for visualization, and AWS for cloud-based data processing.")
            st.write("I have experience in the design field, " \
            "working as a UI/UX designer and graphic designer for a start up company and school organizations.")
        with right_column:
            st_lottie(lottie_data_analysis, height=300, key="data_analysis")
    