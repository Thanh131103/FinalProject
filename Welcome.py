import streamlit as st 
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import webbrowser
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
""" 
"""
Product of 

20127327 - Ngô Hữu Nhật Thanh   

20127560 - Phạm Trần Trung Lượng

20127001 - Hà Quốc Anh

"""
)
if st.button("Go to Searching School"):
        url = "https://thanh131103-finalproject-pagessearching-school-iwo4jw.streamlit.app/"
        webbrowser.open_new_tab(url)
if st.button("Go to DataVisualization"):
        url = "https://thanh131103-finalproject-pages1-datavisualize-98pi7v.streamlit.app/"
        webbrowser.open_new_tab(url)
if st.button("Go to Statistic"):
        url = "hhttps://thanh131103-finalproject-pagesoverview-3ox54x.streamlit.app/"
        webbrowser.open_new_tab(url)
if st.button("Go to Regression Analysis"):
        url = "https://thanh131103-finalproject-pages3-phantichhoiquy-9qrccs.streamlit.app/"
        webbrowser.open_new_tab(url)