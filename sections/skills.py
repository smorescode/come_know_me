import streamlit as st

def render_header_skills():
    st.write("---")
    with st.container():
        st.markdown(
            "<h1 style='text-align: center;'>Interests and Skills</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align: center;'>Throughout my journey as a student, I’ve had the " \
            "opportunity to explore a variety of tools and skills. Some of which I’ve practiced<br> " \
            "hands-on, while others I’m currently learning or gaining familiarity with.</p>",
            unsafe_allow_html=True
        )
        st.write("#")       

def render_data_analysis(img_python, img_powerbi, img_aws):
    st.header("Data Analysis")
    da_col1, da_col2, da_col3 = st.columns(3)
    with da_col1.container(border=True):
        st.image(img_python)
        st.subheader("Python")
        st.write("I have some experience using Python and am currently working on data " \
        "analysis projects with it. I’m continuously learning and exploring " \
        "its full potential.")
    with da_col2.container(border=True):
        st.image(img_powerbi)
        st.subheader("PowerBI")
        st.write("I haven’t used Power BI in a real project yet, but I’m eager to " \
        "learn and apply it for creating insightful data visualizations.")
    with da_col3.container(border=True):
        st.image(img_aws)
        st.subheader("Amazon Web Services")
        st.write("While I haven’t had hands-on experience with AWS yet, I’m willing to " \
        "learn how to use its cloud tools for data processing and analytics.")

def render_design(img_figma, img_canva):
    st.header("Graphic Design")
    gd_col1, gd_col2 = st.columns(2)
    with gd_col1.container(border=True):
        st.image(img_figma)
        st.subheader("Figma")
        st.write("Figma is my main tool for designing UI/UX for a startup I’m part of. I " \
        "use it to create wireframes and prototypes, and collaborate " \
        "with the team in real time.")
    with gd_col2.container(border=True):
        st.image(img_canva)
        st.subheader("Canva")
        st.write("I use Canva to create posters, presentations, and social media content—mainly "
        "for school organizations. It helps me design quickly and effectively using " \
        "its built-in templates.")




            
        



