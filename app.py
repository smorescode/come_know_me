import streamlit as st
from PIL import Image

from utils.lottie_loader import load_lottieurl

from sections.header import render_header
from sections.skills import render_header_skills
from sections.skills import render_design
from sections.skills import render_data_analysis
from sections.experiences import render_header_experience
from sections.experiences import render_orgs
from sections.projects import render_header_project

st.set_page_config(page_title="Come and Know Me", page_icon=":tada:", layout="wide")

#------LOAD ASSETS-------
lottie_data_analysis = load_lottieurl("https://lottie.host/fcaa75fd-07b4-4e0a-a0e7-c090af0df412/d0vwd5ONoj.json")

img_figma = Image.open("assets/figma2_logo.png")
img_figma = img_figma.resize((int(img_figma.width * 50 / img_figma.height), 50))
img_canva = Image.open("assets/canva_logo.png")
img_canva = img_canva.resize((int(img_canva.width * 50 / img_canva.height), 50))

img_python = Image.open("assets/python_logo.png")
img_python = img_python.resize((int(img_python.width * 50 / img_python.height), 50))
img_powerbi = Image.open("assets/powerbi_logo.png")
img_powerbi = img_powerbi.resize((int(img_powerbi.width * 50 / img_powerbi.height), 50))
img_aws = Image.open("assets/aws_logo.png")
img_aws = img_aws.resize((int(img_aws.width * 50 / img_aws.height), 50))

img_uccp = Image.open("assets/uccp_logo.png")
img_uccp = img_uccp.resize((int(img_uccp.width * 200 / img_uccp.height), 200))
img_csps = Image.open("assets/csps_logo.png")
img_csps = img_csps.resize((int(img_csps.width * 200 / img_csps.height), 200))
img_skloud = Image.open("assets/skloud_logo.png")
img_skloud= img_skloud.resize((int(img_skloud.width * 200 / img_skloud.height), 200))

#------RENDER SECTION-------
render_header(lottie_data_analysis)
render_header_skills()
render_data_analysis(img_python, img_powerbi, img_aws)
render_design(img_figma, img_canva)
render_header_project()
render_header_experience()
render_orgs(img_uccp, img_csps, img_skloud)

