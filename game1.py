import streamlit as st

activity=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\ACITVITY.PY",title="project")
deepak=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\deepak\\deepak.py",title="demo")
app=st.Page(page="C:\\Users\\L E N O V O\\Desktop\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\app.py",title="app",default=True)
pg=st.navigation(pages=[activity,deepak,app])
pg.run()