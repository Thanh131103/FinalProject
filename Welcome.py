import streamlit as st 
import pandas as pd
from pages.kMeans import show_overview
from pages.overview import run_kmeans
st.set_page_config(
    page_title='Welcome',
    page_icon="👋"
)
st.write("# Data Visualization ! 👋")
st.sidebar.success("Select a demo above")
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
temp=st.sidebar.selectbox("Select Page", ("Overview", "K-means"))
# Display selected page
if temp == "Overview":
    show_overview()
elif temp == "K-means":
    run_kmeans()