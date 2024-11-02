import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
st.write("hi, i am makizhaasri :wave:")

def lottie_loader(filepath):
    with open(filepath,'r',encoding="utf-8",errors="ignore") as f:
        return json.load(f)
    
lottie_coder=lottie_loader("C:\\Users\\L E N O V O\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157\\Animation - 1730538037922.json")
st_lottie=lottie_coder
st_image=("C:\\Users\\L E N O V O\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157\\Animation - 1730538037922.gif")