import streamlit as st 
import pandas as pd
from pages.Overview import show_overview
from pages.KMeans import run_kmeans
st.set_page_config(
    page_title='Welcome',
    page_icon="👋"
)
st.write("# Data Visualization ! 👋")
st.sidebar.success("Select a demo above")
page = st.sidebar.selectbox("Select Page", ("Overview", "K-means"))

# Display selected page
if page == "Overview":
    show_overview()
elif page == "K-means":
    run_kmeans()
st.markdown(
       """
    ---
    
    ### About Dataset
    This web is about Ranking of university around the World
    ### Author's words
    Hope this dataset helps the data analysis community.

    ---
""""""Product of Ngô Hữu Nhật Thanh 

"""
)