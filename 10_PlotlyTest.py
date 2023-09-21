import streamlit
import plotly.graph_objects as go 

# -    SETTINGS
urls_in = ["General", "Api", "Wordpress"]
urls_remove = ["Out of Scope", "Nothing 2C Here", "Not Applicable"]
prefix = "https://"
page_title = "Recon URL Capture & Track Tool"
page_icon = ":elephant:"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)  