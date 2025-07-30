import streamlit as st

def render_header_experience():
    st.write("---")
    with st.container():
        st.markdown(
            "<h1 style='text-align: center;'>Experience and Affiliations</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align: center;'>Hands-on involvement through school organizations"
            " and a startup company has given me opportunities to grow, collaborate, and apply " \
            "my skills in real-world scenarios</p>",
            unsafe_allow_html=True
        )
        st.write("#")       

def render_orgs(img_uccp, img_csps, img_skloud):
    org_col1, org_col2, org_col3 = st.columns(3)
    with org_col1:
        st.image(img_uccp)
        st.subheader("University of Cebu Council of Presidents (UCCP)")
        with st.expander("Read More About UCCP"):
            st.markdown(
            "<h4 style='text-align: left;'>Details</h1>",
            unsafe_allow_html=True
            )
            st.write("UCCP is an organization at the University of Cebu, where I currently study. " \
            "It serves as the mother organization of the university, overseeing and leading major " \
            "school events and activities. My current and highest position in UCCP is Undersecretary " \
            "of the Records, Circulation, and Management Unit. This unit is primarily responsible"
            " for drafting and managing official documents, including event permission letters, " \
            "communications, and internal records. I am also part of the media team, which writes" \
            "the captions in social media posts. Through these roles, I have developed strong " \
            "organizational, documentation, and communication skills, while contributing to the " \
            "smooth coordination of university-wide events.")
            st.markdown(
            "<h4 style='text-align: left;'>Positions</h1>",
            unsafe_allow_html=True
            )
            st.write("""
                     - Associate in Records Circulation and Management Unit (2024 - 2025)
                     - Junior Technical Writer (2024-2025)
                     - Undersecretary in Records Circulation and Management Unit (2025 - 2026)
                     - Head Technical Writer (2025-2026)
                     """)
    with org_col2:
        st.image(img_csps)
        st.subheader("Computing Society of the Philippines - Students (CSP-S)")
        with st.expander("Read More About CSP-S"):
            st.markdown(
            "<h4 style='text-align: left;'>Details</h1>",
            unsafe_allow_html=True
            )
            st.write("The Computer Studies Peer Society (CSP-S) is a student organization under the " \
            "College of Computer Studies at the University of Cebu. It focuses on organizing " \
            "department-wide activities and initiatives that enhance student engagement and " \
            "professional development within the field of technology. Throughout my time in CSP-S," \
            " I have taken on various leadership roles, including 2nd Year Representative, " \
            "Vice President - Internal, and eventually, 4th Year Representative. These roles allowed me " \
            "to contribute to the planning and execution of events, represent my peers, and " \
            "collaborate closely with fellow officers and faculty.")
            st.markdown(
            "<h4 style='text-align: left;'>Positions</h1>",
            unsafe_allow_html=True
            )
            st.write("""
                     - 2nd Year Representative (2023 - 2024)
                     - Vice President Internal (2024-2025)
                     - 4th Year Representative (2025 - 2026)
                     """)
    with org_col3:
        st.image(img_skloud)
        st.subheader("SKLoud Software and Development Services")
        with st.expander("Read More About SKLoud SDS"):
            st.markdown(
            "<h4 style='text-align: left;'>Details</h1>",
            unsafe_allow_html=True
            )
            st.write("SKLoud SDS is a start up for the E-Sangguniang Kabataan initiative, I contributed to a platform " \
            "designed to empower the youth through digital innovation. This platform aims to increase" \
            " community engagement by helping young people stay informed about local events, participate"
            " in meaningful activities, and earn rewards for their involvement. Through this project, I" \
            " gained hands-on experience in creating graphic designs for promotion of the app. I also get " \
            "to experience designing the UI/UX of the app")
            st.markdown(
            "<h4 style='text-align: left;'>Position</h1>",
            unsafe_allow_html=True
            )
            st.write("""
                     - Graphics Designer
                     - UI/UX Designer
                    """)
    